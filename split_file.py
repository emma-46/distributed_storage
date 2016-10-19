import os
import numpy as np
import shutil


def split_file(path_to_file,n_files=5, ):
    """
    This function aims
    at splitting a file into n_files extracts

    """
    #TODO
    #  if the folder dirname doesnot exists we should create it
    # and create the extracts within this folder

    #a = os.path.join(path_to_file)

    directory, filename = os.path.split(path_to_file)
    filename_basename = os.path.splitext(filename)[0]

    if os.path.exists(os.path.join(directory, filename)):
        with open(os.path.join(directory, filename),'rb') as f:
            shutil.copy(path_to_file, os.path.join(directory,filename_basename+'.txt'))
            print('file .txt created')
        with open(os.path.join(directory, filename),'rb') as f:
            content = f.read()
            print(content[0:15])
            print('##############')
            print(str(content[0:12]))
            n_lines = len(content)
            print(n_lines)
            step = np.ceil(np.float(n_lines)/n_files)
            aa = [int(x*step) for x in range(n_files+1)]
            print(aa)


    for i in range(n_files):
        # result = ''
        print(i)
        # if not os.path.exists(os.path.join(directory, filename_basename+str(i+1))):
        with open(os.path.join(directory, filename_basename+str(i+1)),'wb') as f:
            print(content[aa[i]:aa[i+1]])
            f.write(content[aa[i]:aa[i+1]])
                # result += str(content[aa[i]:aa[i+1]])
                # f.write(bytearray(content[aa[i]:aa[i+1]]))
        # f.write(bytes(result))

path_to_file = "C:/Users/emma/Documents/GitHub/distributed_storage/photo_couchsurfing.jpg"
path_to_file2 = "C:/Users/emma/Documents/GitHub/distributed_storage/lol1.docx"
split_file(path_to_file2, 5)