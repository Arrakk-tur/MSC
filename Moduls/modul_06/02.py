from pathlib import Path

# new_dir = Path("assigments/grade")

# new_dir.mkdir(exist_ok=True, parents=True)

# new_dir.rmdir()

current_path = Path(".")

file = current_path / "un_ziped" / "main.py"
print(file)