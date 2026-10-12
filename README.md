# Downloads Tidy-Up

A small Python script that kills a chore I actually hate: a folder full of loose files
(`IMG_2847.jpg`, random PDFs, installers, zips...). It sorts them into category folders
(`Images/`, `Documents/`, `Archives/`, ...) based on file extension.

It has a **dry-run mode** that shows exactly what would happen before anything is moved.

## Requirements

- Python 3.12
- No external packages (standard library only: `argparse`, `pathlib`, `sys`)

## Setup

```bash
# 1. create and activate a virtual environment
python3.12 -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# 2. install dependencies (none needed; requirements.txt is intentionally empty)
pip install -r requirements.txt
```

## Usage

```bash
# Step 1: ALWAYS preview first
python organizer.py <folder> --dry-run

# Step 2: apply for real
python organizer.py <folder>
```

### Try it safely on fake files

```bash
python make_sandbox.py             # creates ./sandbox with 17 fake messy files
python organizer.py sandbox --dry-run
python organizer.py sandbox
```

## Before / After

Before (`python make_sandbox.py`):

```
(.venv) PS C:\Users\chenni jaswanth\Downloads\crunchy-python-core-t1-jashu\crunchy-python-core-t1-jashu>Remove-Item -Recurse -Force sandbox -ErrorAction SilentlyContinue
>> python make_sandbox.py sandbox
>> dir sandbox
Created 17 sample file(s) in 'sandbox'.


    Directory: C:\Users\chenni 
    jaswanth\Downloads\crunchy-python-core-t1-jashu\crunchy-python-core-t1-jashu\sandbox


Mode                 LastWriteTime         Length Name                                                  
----                 -------------         ------ ----                                                  
-a----        12-10-2026     18:41             36 assignment.docx                                       
-a----        12-10-2026     18:41             31 backup.tar                                            
-a----        12-10-2026     18:41             32 budget.xlsx                                           
-a----        12-10-2026     18:41             29 data.xyz                                              
-a----        12-10-2026     18:41             33 holiday.heic                                          
-a----        12-10-2026     18:41             33 IMG_2847.jpg                                          
-a----        12-10-2026     18:41             33 IMG_2848.png                                          
-a----        12-10-2026     18:41             31 index.html                                            
-a----        12-10-2026     18:41             32 lecture.mp4                                           
-a----        12-10-2026     18:41             30 marks.csv                                             
-a----        12-10-2026     18:41             33 mystery_file                                          
-a----        12-10-2026     18:41             30 notes.txt                                             
-a----        12-10-2026     18:41             32 project.zip                                           
-a----        12-10-2026     18:41             31 resume.pdf                                            
-a----        12-10-2026     18:41             30 script.py                                             
-a----        12-10-2026     18:41             30 setup.exe                                             
-a----        12-10-2026     18:41             29 song.mp3 
```

Dry run (nothing changes):

```
(.venv) PS C:\Users\chenni jaswanth\Downloads\crunchy-python-core-t1-jashu\crunchy-python-core-t1-jashu>python organizer.py sandbox --dry-run
[DRY RUN] would move: assignment.docx  ->  Documents\assignment.docx
[DRY RUN] would move: backup.tar  ->  Archives\backup.tar
[DRY RUN] would move: budget.xlsx  ->  Spreadsheets\budget.xlsx
[DRY RUN] would move: data.xyz  ->  Other\data.xyz
[DRY RUN] would move: holiday.heic  ->  Images\holiday.heic
[DRY RUN] would move: IMG_2847.jpg  ->  Images\IMG_2847.jpg
[DRY RUN] would move: IMG_2848.png  ->  Images\IMG_2848.png
[DRY RUN] would move: index.html  ->  Code\index.html
[DRY RUN] would move: lecture.mp4  ->  Video\lecture.mp4
[DRY RUN] would move: marks.csv  ->  Spreadsheets\marks.csv
[DRY RUN] would move: mystery_file  ->  Other\mystery_file
[DRY RUN] would move: notes.txt  ->  Documents\notes.txt
[DRY RUN] would move: project.zip  ->  Archives\project.zip
[DRY RUN] would move: resume.pdf  ->  Documents\resume.pdf
[DRY RUN] would move: script.py  ->  Code\script.py
[DRY RUN] would move: setup.exe  ->  Installers\setup.exe
[DRY RUN] would move: song.mp3  ->  Audio\song.mp3

Done: 17 of 17 file(s) would be moved.
This was a dry run. Re-run without --dry-run to apply.
...
```

After (`python organizer.py sandbox`):

```
(.venv) PS C:\Users\chenni jaswanth\Downloads\crunchy-python-core-t1-jashu\crunchy-python-core-t1-jashu>python organizer.py sandbox
>> dir sandbox
[MOVED]   assignment.docx  ->  Documents\assignment.docx
[MOVED]   backup.tar  ->  Archives\backup.tar
[MOVED]   budget.xlsx  ->  Spreadsheets\budget.xlsx
[MOVED]   data.xyz  ->  Other\data.xyz
[MOVED]   holiday.heic  ->  Images\holiday.heic
[MOVED]   IMG_2847.jpg  ->  Images\IMG_2847.jpg
[MOVED]   IMG_2848.png  ->  Images\IMG_2848.png
[MOVED]   index.html  ->  Code\index.html
[MOVED]   lecture.mp4  ->  Video\lecture.mp4
[MOVED]   marks.csv  ->  Spreadsheets\marks.csv
[MOVED]   mystery_file  ->  Other\mystery_file
[MOVED]   notes.txt  ->  Documents\notes.txt
[MOVED]   project.zip  ->  Archives\project.zip
[MOVED]   resume.pdf  ->  Documents\resume.pdf
[MOVED]   script.py  ->  Code\script.py
[MOVED]   setup.exe  ->  Installers\setup.exe
[MOVED]   song.mp3  ->  Audio\song.mp3

Done: 17 of 17 file(s) moved.


    Directory: C:\Users\chenni 
    jaswanth\Downloads\crunchy-python-core-t1-jashu\crunchy-python-core-t1-jashu\sandbox


Mode                 LastWriteTime         Length Name                                                  
----                 -------------         ------ ----                                                  
d-----        12-10-2026     18:42                Archives                                              
d-----        12-10-2026     18:42                Audio                                                 
d-----        12-10-2026     18:42                Code                                                  
d-----        12-10-2026     18:42                Documents                                             
d-----        12-10-2026     18:42                Images                                                
d-----        12-10-2026     18:42                Installers                                            
d-----        12-10-2026     18:42                Other                                                 
d-----        12-10-2026     18:42                Spreadsheets                                          
d-----        12-10-2026     18:42                Video
```

## How it handles problems

| Situation | What happens |
|---|---|
| Folder doesn't exist | Prints `Error: folder does not exist`, exits with code 1 (no crash) |
| Path is a file, not a folder | Prints `Error: not a folder`, exits with code 1 |
| Empty folder / already organized (run twice) | Prints `Nothing to organize`, changes nothing |
| File with the same name already in the destination | Never overwritten; the new file is saved as `name (1).ext`, `name (2).ext`, ... |
| File is locked / permission denied / folder can't be created | That file is reported as `[SKIPPED]`, the rest continue |
| Hidden files (`.gitignore`, `.DS_Store`) | Left alone |

Only loose files directly inside the folder are touched; existing sub-folders are never entered.

## Project structure

```
organizer.py       # the tool: get_category, unique_destination, collect_files,
                   #           move_file, organize, parse_args, main
make_sandbox.py    # creates fake files for safe testing
requirements.txt   # empty on purpose (no external packages)
README.md
```

All logic lives inside functions; the only top-level call is `main()`.
