import os
def rename_files():
        file_list = os.listdir(r"/home/blindness/Documents/python/prank")
        print(file_list)
        #cwd current working directory
        #to check the directory
        saved_path = os.getcwd()
        print saved_path
        os.chdir(r"/home/blindness/Documents/python/prank")
        for file_name in file_list:
                os.rename(file_name,file_name.translate(None, "0123456789"))
        os.chdir(saved_path)
rename_files()    
