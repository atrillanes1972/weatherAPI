import zipfile
import pathlib

def make_archive(filepaths,dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_path, 'w') as archive:
        for filepath in filepaths:
            archive.write(filepath)


if __name__ == "main":
    make_archive(filepaths=["bonus1.py","bonus2.py"],dest_dir="dest")
