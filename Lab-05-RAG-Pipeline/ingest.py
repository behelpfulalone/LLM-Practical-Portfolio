from pathlib import Path
import hashlib
import pymupdf

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma

BASE_DIR = Path(__file__).resolve().parent
DOCUMENT_DIR = BASE_DIR / "documents"
DB_DIR = BASE_DIR / "chroma_db"

EMBEDDING_MODEL = "qwen3-embedding:0.6b"
COLLECTION_NAME = "rag_documents"


def get_vector_store():
    embeddings = OllamaEmbeddings(
        model=EMBEDDING_MODEL
    )

    return Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=str(DB_DIR)
    )


def load_pdf(file_path):
    file_path = Path(file_path)
    documents = []

    with pymupdf.open(str(file_path)) as pdf:
        for page_number, page in enumerate(pdf, start=1):
            text = page.get_text().strip()

            if text:
                documents.append(
                    Document(
                        page_content=text,
                        metadata={
                            "source": file_path.name,
                            "page": page_number
                        }
                    )
                )

    return documents


def ingest_pdf(file_path):
    documents = load_pdf(file_path)

    if not documents:
        raise ValueError("No readable text found in the PDF.")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    file_hash = hashlib.sha256(
        Path(file_path).read_bytes()
    ).hexdigest()

    ids = [
        hashlib.sha256(
            f"{file_hash}:{Path(file_path).name}:{index}".encode()
        ).hexdigest()
        for index in range(len(chunks))
    ]

    vector_store = get_vector_store()

    existing_ids = set(
        vector_store.get(ids=ids)["ids"]
    )

    new_chunks = []
    new_ids = []

    for chunk, chunk_id in zip(chunks, ids):
        if chunk_id not in existing_ids:
            new_chunks.append(chunk)
            new_ids.append(chunk_id)

    if new_chunks:
        vector_store.add_documents(
            documents=new_chunks,
            ids=new_ids
        )

    return len(new_chunks)


def main():
    pdf_files = sorted(DOCUMENT_DIR.glob("*.pdf"))

    if not pdf_files:
        print("No PDF documents found.")
        return

    total_chunks = 0

    for file_path in pdf_files:
        print(f"Processing: {file_path.name}")

        count = ingest_pdf(file_path)
        total_chunks += count

        print(f"New chunks indexed: {count}")

    print(f"Total new chunks: {total_chunks}")
    print("PDF ingestion completed successfully.")


if __name__ == "__main__":
    main()
