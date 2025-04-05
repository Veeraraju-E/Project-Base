import os
import sys
from pathlib import Path

def create_file(path: Path, content: str = ""):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w') as f:
        f.write(content)

def create_project_structure(base_path: Path):
    dirs = [
        "src/models",
        "src/trainers",
        "configs",
        "scripts",
        "data",
        "datasets",
        "outputs/plots",
        "docs"
    ]

    files = {
        "README.md": "# New ML Project\n\nProject description goes here.",
        "requirements.txt": "# Add your project dependencies here",
        "configs/train.yaml": "# Training configuration",
        "src/__init__.py": "",
        "src/models/__init__.py": "",
        "src/trainers/__init__.py": "",
        "scripts/train.py": "# Entry point for training",
        "docs/overview.md": "# Project Documentation\n\nAdd architecture diagrams, methodology, etc."
    }

    for directory in dirs:
        dir_path = base_path / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"Created directory: {dir_path}")

    for file, content in files.items():
        file_path = base_path / file
        create_file(file_path, content)
        print(f"Created file: {file_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python create_project.py <project_name>")
        sys.exit(1)

    project_name = sys.argv[1]
    base_path = Path(project_name).resolve()

    if base_path.exists():
        print(f"Error: Directory '{base_path}' already exists.")
        sys.exit(1)

    create_project_structure(base_path)
    print(f"\nProject '{project_name}' structure created at {base_path}")

if __name__ == "__main__":
    main()
