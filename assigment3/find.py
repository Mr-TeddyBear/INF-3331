import sys
import os


name, location = sys.argv[1],sys.argv[2]
def recursive_folder_search(path,file_name):
    for dirName,subDirList,fileList in os.walk(path,name):
        # print ("Found Directory %s, starting recursive search" % dirName)
        for files in fileList:
            if name in files:
                print (os.getcwd() + files)
        if len(subDirList) < 0:
            print ("Shit Hapcpns")
            for dirs in subDirList:
                recursive_folder_search(dirs,file_name)
recursive_folder_search(location,name)
