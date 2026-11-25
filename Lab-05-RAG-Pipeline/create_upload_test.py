import pymupdf
from pathlib import Path

folder = Path.home() / "Downloads"

files = {
    "scholarship_policy.pdf": [
        "Westbridge University - Special Scholarship Policy",
        "The Innovation Excellence Scholarship is worth LKR 175000.",
        "Applicants must maintain a minimum GPA of 3.5.",
        "The scholarship application deadline is August 20."
    ],
    "examination_policy.pdf": [
        "Westbridge University - Examination Policy",
        "Students must arrive 30 minutes before examinations.",
        "The examination resit fee is LKR 7500 per module.",
        "Examination results are released within 21 days."
    ]
}

for filename, lines in files.items():
    doc = pymupdf.open()
    page = doc.new_page()

    for index, line in enumerate(lines):
        page.insert_text(
            (50, 60 + index * 35),
            line,
            fontsize=12
        )

    path = folder / filename
    doc.save(str(path))
    doc.close()
    print(f"Created: {path}")
