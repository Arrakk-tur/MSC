from pathlib import Path

current_path = Path(".")

def parse_fold(path):
    for el in path.iterdir():
        if el.is_dir():
            print(f"This is folder: {el}")
        else:
            print(f"This is file: {el}")


parse_fold(current_path)

