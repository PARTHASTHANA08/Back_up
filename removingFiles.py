import os 
import shutil 
import time

def main():
    deletedFolders = 0
    deletedFiles = 0

    path = "/PATH_TO_DELETE"

    days = 30 
    seconds = time.time() - (days * 24 * 60 * 60)

    if os.path.exists(path):
        for rootFolders , folders ,files in os.walk(path):
            if seconds >= get_files_or_folders_date(rootFolders):
                removeFolders(rootFolders)
                deletedFolders += 1
                break
            else: 
                for folder in folders:
                    folderPath = os.path.join(rootFolders,folders)
                    if seconds >= get_files_or_folders_date(folderPath):
                        removeFolders(folderPath)
                        deletedFolders += 1
                for file in files:
                    filePath = os.path.join(rootFolders,files)
                    if seconds >= get_files_or_folders_date(filePath):
                        removeFiles(filePath)
                        deletedFiles += 1
        else:
            if seconds >= get_files_or_folders_date(path):
                removeFiles(filePath)
                deletedFiles += 1
    else: 
       print(f'"{path}"is not found')   
       deletedFiles += 1
    print(f"Total Folders Deleted : {deletedFolders}")
    print(f"Total Files Deletd : {deletedFiles}")             
def removeFolders(path):
    if not  shutil.rmtree(path):
        print(f"{path} Removed Successfully")
    else :
        print(f"Unable To Delete The " + path)
def removeFiles(path):
    if not os.remove(path):
        print(f"{path} Removed Successfully")
    else:
        print(f"Unable To Delete The " + path )
def get_files_or_folders_date(path):      
    ctime = os.stat(path).st_ctime  
    return ctime

if __name__ == 'main':
    main()
    





