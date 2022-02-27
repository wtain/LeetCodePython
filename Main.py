import os
import subprocess
from sys import path
from typing import List, Set


def walk_root(dir: str, ignore_list: Set[str]):

    old_files = []

    def visit_file(file: str):
        nonlocal old_files
        print(f'*** Running {file}')
        command_line = f"python {file}"
        # subprocess.call(f"python {file}", shell=True)
        proc = subprocess.Popen(command_line, stdout=subprocess.PIPE)
        output = proc.stdout.read()
        pos = str(output).find("OVERALL")
        if -1 == pos:
            # print(f"Old: {file}")
            old_files.append(file)
        # print(output)

    def visit_dir(dir: str):
        for file in os.listdir(dir):
            if file in ignore_list:
                continue
            full_path = os.path.join(dir, file)
            if os.path.isdir(full_path):
                visit_dir(full_path)
            else:
                visit_file(full_path)

    visit_dir(dir)

    print("Old files:")
    print(old_files)


if __name__ == '__main__':
    walk_root('.', {'__pycache__', '.git', '.', '.idea', '.gitignore', 'Common', 'Main.py'})
