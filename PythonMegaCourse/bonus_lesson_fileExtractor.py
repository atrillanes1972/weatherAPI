import zipfile

def extract_archive(archivepath,dest_dir):
    with zipfile.ZipFile(archivepath,'r') as archive:
        archive.extractall(dest_dir)

if __name__ == "__main__":
    extract_archive(r"C:\Users\P10145PH1\Desktop\pythonProjects\PythonMegaCourse\dest\compressed.zip",
                    r"C:\Users\P10145PH1\Desktop\pythonProjects\PythonMegaCourse\test")
