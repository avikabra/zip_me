import zipfile 
import os

zip = zipfile.ZipFile('test_file_2.zip', 'w')
print(os.getcwd())
for file in os.listdir(os.getcwd()):
    if file.endswith(".txt"):
        zip.write(os.path.join(os.getcwd(), file), file, compress_type = zipfile.ZIP_DEFLATED)

zip.close()