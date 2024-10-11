from pathlib import Path

file_content = Path("README.md").read_text()
print(f"======\n{file_content}\n======")

