"""
For creating file structure for AI projects
"""
import os
from pathlib import Path

project_dir = input("Enter Project name: ")

while True:
    prompt = input("Do you want to use a custom file structure?: ")
    if prompt == 'yes':
        sub_dirs_input = input("Enter Sub directories separated by a delimiter: ")
        delimiter = input("Enter delimiter: ")
        sub_dirs = sub_dirs_input.split(delimiter)
    elif prompt == 'no':
        print("Utilizing standard sub directories")
        sub_dirs = ['data', 'src', 'models', 'notebooks', 'references', 'reports', 'docs', 'tests']
    else:
        print("Please enter 'yes' or 'no'")
    prompt_2 = input("Do you want to make another choice?: ")
        
    if prompt_2 != 'yes':
        break

def directory_setup(project_dir: str, sub_dirs: list) -> None:
    """
    Creates the directory structure for the project.

    The structure includes the main project directory, files and its subdirectories:
    - 'src' for source code
    - 'models' for model files
    - 'data' for data files
    - 'references'
    - 'reports'
    - 'docs'
    - 'tests'
    - 'notebooks'
    - 'requirements.txt'
    - 'README.md'
    - 'setup.cfg'
    - 'pyproject.toml'

    Returns:
        None
    """

    # Create the project directory
    directory_path = Path(project_dir)
    directory_path.mkdir(parents=True, exist_ok=True)

    # Create subdirectories
    for sub in sub_dirs:
        (directory_path / sub).mkdir(parents=True, exist_ok=True)

    # Create files in project directory
    project_files = ["README.md", "requirements.txt", "LICENSE", "setup.cfg", "pyproject.toml"]
    for project_file in project_files:
        (directory_path / f"{project_file}").touch()
    
    # Create ".py" files in the 'src' directory
    py_files = ["download_data", "setup_data", "engine", "create_model", "train",
                "save_model", "plot_loss", "predict", "__init__"]
    for py_file in py_files:
        (directory_path / "src" / f"{py_file}.py").touch()

if __name__ == "__main__":
    directory_setup(project_dir, sub_dirs)
