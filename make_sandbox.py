"""Create a throwaway 'sandbox' folder full of fake messy files for safe testing.

Usage:
    python make_sandbox.py            # creates ./sandbox
    python make_sandbox.py my_folder  # creates ./my_folder
"""

import sys
from pathlib import Path

SAMPLE_NAMES = [
    "IMG_2847.jpg", "IMG_2848.png", "holiday.heic",
    "resume.pdf", "notes.txt", "assignment.docx",
    "marks.csv", "budget.xlsx",
    "project.zip", "backup.tar",
    "song.mp3", "lecture.mp4",
    "script.py", "index.html",
    "setup.exe", "mystery_file", "data.xyz",
]


def create_sandbox(folder: Path) -> int:
    """Create fake files inside ``folder`` (made if missing).

    Existing files are left untouched, so running this twice is safe.

    Args:
        folder: Where to create the sample files.

    Returns:
        The number of files actually created.
    """
    folder.mkdir(parents=True, exist_ok=True)
    created = 0
    for name in SAMPLE_NAMES:
        target = folder / name
        if not target.exists():
            target.write_text(f"sample content for {name}\n", encoding="utf-8")
            created += 1
    return created


def main() -> None:
    """Entry point: build the sandbox in the folder given on the command line."""
    folder = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("sandbox")
    count = create_sandbox(folder)
    print(f"Created {count} sample file(s) in '{folder}'.")


if __name__ == "__main__":
    main()
