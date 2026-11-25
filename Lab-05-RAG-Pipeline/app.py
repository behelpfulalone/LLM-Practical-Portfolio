from pathlib import Path
import hashlib
import streamlit as st

from ingest import ingest_pdf, get_vector_store
from rag_pipeline import ask_question

BASE_DIR = Path(__file__).resolve().parent
UPLOAD_DIR = BASE_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

st.set_page_config(
    page_title="Document AI Assistant",
    page_icon="PDF",
    layout="wide"
)

st.title("Document AI Assistant")

st.caption(
    "Local Retrieval-Augmented Generation | "
    "Llama 3.2 | Qwen3 Embedding | ChromaDB"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("Knowledge Base")

    st.success("Local AI models configured")

    st.markdown("**Language model**")
    st.code("llama3.2:3b")

    st.markdown("**Embedding model**")
    st.code("qwen3-embedding:0.6b")

    st.divider()

    st.subheader("Upload PDF documents")

    uploaded_files = st.file_uploader(
        "Select one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button(
        "Process Documents",
        use_container_width=True,
        disabled=not uploaded_files
    ):
        total_chunks = 0

        for uploaded_file in uploaded_files:
            try:
                with st.spinner(
                    f"Processing {uploaded_file.name}..."
                ):
                    content = uploaded_file.getvalue()
                    file_hash = hashlib.sha256(
                        content
                    ).hexdigest()[:12]

                    safe_name = Path(
                        uploaded_file.name
                    ).name

                    file_dir = UPLOAD_DIR / file_hash
                    file_dir.mkdir(exist_ok=True)

                    file_path = file_dir / safe_name
                    file_path.write_bytes(content)

                    count = ingest_pdf(file_path)
                    total_chunks += count

                    st.success(
                        f"{safe_name}: {count} new chunks"
                    )

            except Exception as error:
                st.error(
                    f"Could not process "
                    f"{uploaded_file.name}: {error}"
                )

        st.info(
            f"Total new chunks indexed: {total_chunks}"
        )

    st.divider()

    st.subheader("Database Statistics")

    try:
        vector_store = get_vector_store()
        database_data = vector_store.get(
            include=["metadatas"]
        )

        metadata = database_data["metadatas"] or []

        indexed_sources = sorted({
            item.get("source", "Unknown")
            for item in metadata
        })

        st.metric(
            "Indexed chunks",
            len(database_data["ids"])
        )

        st.metric(
            "Unique source names",
            len(indexed_sources)
        )

        with st.expander("Indexed documents"):
            for source in indexed_sources:
                st.write(source)

    except Exception as error:
        st.error(f"Database error: {error}")

    st.divider()

    if st.button(
        "Clear Conversation",
        use_container_width=True
    ):
        st.session_state.messages = []
        st.rerun()

    st.caption(
        "All document processing and AI inference "
        "are performed locally."
    )


def display_sources(sources):
    if not sources:
        return

    with st.expander("Retrieved document context"):
        for index, source in enumerate(sources, start=1):
            st.markdown(
                f"**{index}. {source['source']} "
                f"- Page {source['page']}**"
            )

            st.write(source["content"])
            st.divider()


if not st.session_state.messages:
    st.info(
        "Ask a question about the indexed documents "
        "or upload your own PDFs using the sidebar."
    )

    st.markdown("### Example questions")

    st.markdown(
        """
        - What is the minimum attendance requirement?
        - How much is the annual AI degree tuition fee?
        - Where is the IT help desk located?
        - What are the library opening hours?
        """
    )

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

        if message["role"] == "assistant":
            display_sources(
                message.get("sources", [])
            )

question = st.chat_input(
    "Ask a question about your documents..."
)

if question:
    st.session_state.messages.append({
        "role": "user",
        "content": question
    })

    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner(
                "Retrieving documents and generating answer..."
            ):
                result = ask_question(question)

            st.markdown(result["answer"])
            display_sources(result["sources"])

            st.session_state.messages.append({
                "role": "assistant",
                "content": result["answer"],
                "sources": result["sources"]
            })

        except Exception as error:
            st.error(f"Unable to generate an answer: {error}")
