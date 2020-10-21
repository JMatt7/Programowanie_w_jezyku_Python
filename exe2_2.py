#!/usr/bin/env python
#Write a recursive transition of the directory tree and list the files that are in the structure being explored

import os
import sys
class DirectoryStructure:

    def __init__(self, path : str):
        """
        :param path: current given directory for transition
        
        :attr one: label for subdirectories in main directory
        :attr padding: indent for subdirectories and files 
        :attr file: indent for files
        :attr last_file: lebal for last file in subdirectory
        """
        
        self.path = path
        self.one = '|->SubDirectory: '
        self.padding = '|  '
        self.file = '|FileName: '
        self.last_file = ''
    

    def treeWalk(self):
        
        #Traverse directory, subdirectory and files in current given directory
        for folder, subs, files in os.walk(self.path):
            tuples.append((folder, subs, files))
            folders.append(self.folderTree(folder))
    
    def folderTree(self, tuples):
        
        #return current directory
        if tuples == self.path:
            return ('Directory: ' + tuples)
        
        #return subdirectory if is the only one
        if tuples.count(os.sep) == 1:
            tuples = tuples.split(os.sep)
            tuples[0] = self.one

            return (''.join(tuples))

        #return subdirectories if there are more than 1 subdirectory
        if tuples.count(os.sep) >= 2:
            tuples = tuples.split(os.sep)
            tuples[-2] = self.one

            for i in range(len(tuples[:-2])):
                tuples[i] = self.padding

            return (''.join(tuples))


    def filesTree(self, *args):
        """
        :param args: args[0] - tuples, args[1] - folders
        """
        tuples = args[0]
        folders_list = args[1]

        for root, subs, files in tuples:
            
            #not files, continue
            if not files:
                continue
            
            #adding padding to root
            sep = root.count(os.sep)

            #if the only directory is root and there are not any subdirectories
            if(root == self.path):
                self.last_file = [self.file+str(x) for x in files]
                continue
            
            #subdirectiores and indexing
            if subs:
                
                index = folders_list.index([x for x in folders_list if x.endswith(subs[-1])][0]) + 1

            else:
                
                folder_name = root.split(os.sep)[-1]
                index = folders_list.index([x for x in folders_list if x.endswith(folder_name)][0]) + 1

            #files in subdirectories
            files = [sep * self.padding + self.file + x for x in files]

           
            for i, a in enumerate(range(index, index+len(files))):
                folders_list.insert(a, files[i])
            
        #merge files in root directory
        if self.last_file:
            folders_list = folders_list + self.last_file
        
        #print tree of directory
        for elm in folders_list:
            print(elm)


if __name__ == "__main__":
    if(sys.argv[1] == "--help"):
        print("Give path to directory")
    else:
        folders = []
        tuples = []
        d = DirectoryStructure(sys.argv[1])
        d.treeWalk()
        d.folderTree(tuples)
        d.filesTree(tuples, folders)