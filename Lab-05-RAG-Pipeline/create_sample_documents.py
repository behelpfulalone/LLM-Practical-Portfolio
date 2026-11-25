from pathlib import Path
import pymupdf

output_dir = Path("documents")
output_dir.mkdir(exist_ok=True)

documents = {
    "student_handbook.pdf": (
        "Westbridge University - Student Handbook",
        [
            "Westbridge University is a fictional university used for RAG testing.",
            "Students must maintain a minimum attendance of 80 percent.",
            "The minimum passing mark for undergraduate modules is 40 percent.",
            "Coursework contributes 60 percent and examinations contribute 40 percent to the final grade.",
            "Late coursework submissions receive a penalty of 5 marks per day.",
            "Students may borrow up to 6 library books for 14 days.",
            "The university library operates from 8 AM to 8 PM on weekdays."
        ]
    ),
    "admissions_guide.pdf": (
        "Westbridge University - Admissions Guide",
        [
            "Applications for the September intake close on July 15.",
            "The undergraduate application fee is LKR 2500.",
            "Applicants must submit academic transcripts and identification documents.",
            "The Bachelor of Artificial Intelligence degree lasts four years.",
            "The annual tuition fee for the Artificial Intelligence degree is LKR 450000.",
            "Merit scholarships cover up to 50 percent of tuition fees.",
            "International students must provide evidence of English proficiency."
        ]
    ),
    "campus_services.pdf": (
        "Westbridge University - Campus Services",
        [
            "The university provides free Wi-Fi to all registered students.",
            "The campus medical centre operates from 9 AM to 5 PM.",
            "Student parking permits cost LKR 3000 per semester.",
            "The university gym is open from 6 AM to 9 PM.",
            "Career counselling appointments are free for registered students.",
            "The IT help desk is located in Building C, Room 204.",
            "The student shuttle service operates every 30 minutes."
        ]
    )
}

for filename, (title, paragraphs) in documents.items():
    doc = pymupdf.open()
    page = doc.new_page()

    page.insert_text(
        (50, 60),
        title,
        fontsize=18
    )

    y = 110

    for paragraph in paragraphs:
        page.insert_textbox(
            pymupdf.Rect(50, y, 545, y + 65),
            paragraph,
            fontsize=12
        )
        y += 75

    path = output_dir / filename
    doc.save(str(path))
    doc.close()

    print(f"Created: {path}")

print("All sample PDF documents created successfully.")
