"""Downloads Tidy-Up: sort a messy folder into category sub-folders.

Every loose file in the target folder is moved into a sub-folder chosen by its
extension (Images, Documents, Archives, ...). Use --dry-run first to preview.

Usage:
    python organizer.py <folder> --dry-run
    python organizer.py <folder>
"""

import argparse
import sys
from pathlib import Path

# Extension -> category. Anything not listed goes to "Other".
CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".heic"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".md", ".rtf", ".odt", ".ppt", ".pptx"},
    "Spreadsheets": {".csv", ".xls", ".xlsx", ".ods"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".m4a"},
    "Video": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Code": {".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json", ".ipynb"},
    "Installers": {".exe", ".msi", ".dmg", ".apk", ".deb"},
}
FALLBACK_CATEGORY = "Other"


def get_category(file_path: Path) -> str:
    """Return the category folder name for a file, based on its extension.

    Args:
        file_path: Path of the file to classify.

    Returns:
        A category name such as "Images", or "Other" if the extension is unknown.
    """
    extension = file_path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if extension in extensions:
            return category
    return FALLBACK_CATEGORY


def unique_destination(destination: Path) -> Path:
    """Return a destination path that does not already exist.

    If ``destination`` is taken, a counter is added before the extension
    ("report.pdf" -> "report (1).pdf", "report (2).pdf", ...) so no existing
    file is ever overwritten.

    Args:
        destination: The preferred target path.

    Returns:
        A path that is guaranteed not to exist at the time of the call.
    """
    if not destination.exists():
        return destination
    counter = 1
    while True:
        candidate = destination.with_name(f"{destination.stem} ({counter}){destination.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def collect_files(folder: Path) -> list[Path]:
    """List the loose files directly inside a folder (not sub-folders).

    Hidden files (names starting with a dot) are skipped, so the script
    leaves things like .gitignore or .DS_Store alone.

    Args:
        folder: The folder to scan.

    Returns:
        A sorted list of file paths.
    """
    return sorted(
        item for item in folder.iterdir()
        if item.is_file() and not item.name.startswith(".")
    )


def move_file(file_path: Path, folder: Path, dry_run: bool) -> bool:
    """Move one file into its category sub-folder (or just report, in dry-run).

    Handles name clashes via ``unique_destination`` and reports, instead of
    crashing, when a file is locked/open or permission is denied.

    Args:
        file_path: The file to move.
        folder: The root folder being organized.
        dry_run: If True, print what would happen and change nothing.

    Returns:
        True if the file was (or, in dry-run, would be) moved, False on error.
    """
    category_dir = folder / get_category(file_path)
    destination = unique_destination(category_dir / file_path.name)
    label = f"{file_path.name}  ->  {destination.relative_to(folder)}"

    if dry_run:
        print(f"[DRY RUN] would move: {label}")
        return True

    try:
        category_dir.mkdir(exist_ok=True)
        file_path.rename(destination)
    except (PermissionError, OSError) as error:
        print(f"[SKIPPED] {file_path.name}: {error}")
        return False
    print(f"[MOVED]   {label}")
    return True


def organize(folder: Path, dry_run: bool) -> int:
    """Organize every loose file in ``folder`` and print a summary.

    Args:
        folder: The folder to tidy up.
        dry_run: If True, only preview the changes.

    Returns:
        Process exit code: 0 on success, 1 if the folder is missing/invalid.
    """
    if not folder.exists():
        print(f"Error: folder does not exist: {folder}")
        return 1
    if not folder.is_dir():
        print(f"Error: not a folder: {folder}")
        return 1

    files = collect_files(folder)
    if not files:
        print("Nothing to organize: no loose files found.")
        return 0

    moved = sum(move_file(path, folder, dry_run) for path in files)
    verb = "would be moved" if dry_run else "moved"
    print(f"\nDone: {moved} of {len(files)} file(s) {verb}.")
    if dry_run:
        print("This was a dry run. Re-run without --dry-run to apply.")
    return 0


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments.

    Returns:
        Namespace with ``folder`` (Path) and ``dry_run`` (bool).
    """
    parser = argparse.ArgumentParser(description="Sort loose files into category folders.")
    parser.add_argument("folder", type=Path, help="folder to organize")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="show what would happen without moving anything",
    )
    return parser.parse_args()


def main() -> None:
    """Entry point: read arguments and run the organizer."""
    args = parse_args()
    sys.exit(organize(args.folder.expanduser(), args.dry_run))


if __name__ == "__main__":
    main()
