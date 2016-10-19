import os
import numpy as np
import shutil

def merge_files(path_to_file, n_files=5):

    directory, filename = os.path.split(path_to_file)
    filename_basename = os.path.splitext(filename)[0]

    new_file = b''
    for i in range(n_files):
        if(os.path.exists(os.path.join(directory, filename_basename) + str(i + 1)) ):
            with open(os.path.join(directory, filename_basename + str(i + 1)), 'rb') as f:
                new_file += f.read()

    with open('new_file2.docx', 'wb') as f:
        f.write(new_file)

path_to_file = "C:/Users/emma/Documents/GitHub/distributed_storage/lol1.docx"
merge_files(path_to_file, 5)

path2 = "C:/Users/emma/Documents/GitHub/distributed_storage/new_file2.docx"
with open(path_to_file, 'rb') as f1:
    text1 = f1.read()
    print(text1[0:10])
    with open(path2, 'rb') as f2 :
        text2 = f2.read()
        print(text2[0:10])
        print(text2==text1)


# merge_files(path_to_file, 5)
