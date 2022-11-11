# Here, this is a simple implementation of a file system.
# Each object of either File class or Folder class has there specific methods
# Using those, you can:
#   ->print file/folder names
#   ->Add files to folders
#   ->Remove files from folder


import collections

class File:
    def __init__(self, file_name) -> None:
        self.file_name = file_name
    def print_file_name(self):
        print("The current file is: ", self.file_name)
    
class Folder:
    def __init__(self, folder_name) -> None:
        self.folder = collections.defaultdict(list)
        self.folder_name = folder_name

    def print_folder_name(self):
        print("The curent folder is: ", self.folder_name, "\n")

    def add_file_to_folder(self, file_name):
        self.folder[self.folder_name +"/" +file_name].append(file_name)
        print(file_name , "is added to",self.folder_name,"folder and the path is: ", self.folder_name +"/" +file_name)
        print("The files or folders in ",self.folder_name," are:",self.folder, "\n")

    def remove_file_from_folder(self, file_name):
        self.folder[self.folder_name +"/" +file_name].remove(file_name)
        print(file_name , "is deleted from",self.folder_name,"folder and the path is: ", self.folder_name +"/" +file_name)
        print("The files or folders in ",self.folder_name," are:",self.folder, "\n")

    def add_folder_to_folder(self, folder_name, folder):
        self.folder[self.folder_name + "/" + folder_name].append(folder)
        print("The files or folders in ", self.folder_name, "are",self.folder, "\n")

    def remove_folder_from_folder(self, folder_name, folder):
        pass
    
movies = Folder("movies")
avatar = File("avatar.mp4")

#These lines are used to print folder and file names
avatar.print_file_name()
movies.print_folder_name()

#In these lines, I added files to a folder and deleted form the folder
movies.add_file_to_folder("test_movie.mp4")
movies.remove_file_from_folder("test_movie.mp4")

#Here, I created a folder named "romance" romance and added a file named "love.mp4"
romance = Folder("romance")
romance.add_file_to_folder("love.mp4")

# Here, I added the folder "romance" in the folder "movies"
movies.add_folder_to_folder("romance", romance.folder)
