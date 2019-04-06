"""

This is the project to  segregate the different
file type in to separate folders

created by Sumit Kumar Bhowmick
"""

import os
import shutil

destination_folder = {  # This dictionary contains all the file types and their corresponding file name
    '.txt': 'Text',
    '.doc': 'Document',
    '.pdf': 'PDF',
    '.png': 'Image',
    '.img': 'Image',
    '.jpeg': 'Image',
    '.jpg': 'Image',
    '.zip': 'Zip_Files',
    '.mp4': 'Videos',
    '.mp3': 'Music',
    '.pptx': 'PPT',
    '.ppt': 'PPT',
    '.iso': 'OS',
    '.exe': 'Software',
    '.msi': 'Software',
    '.torrent': 'Torrent'}


class FileManager:
    """docstring for FileManager"""

    def __init__(self, filetype, source=os.path.expanduser("~/Downloads"),
                 destination=os.path.expanduser("~/Downloads")):
                # initialize the diractor and file type
        self.source = source
        self.destination = destination
        self.filetype = filetype
        self.destination_fix()

    def destination_fix(self):
        for key in destination_folder:

            if key == self.filetype:
                if destination_folder[key] in os.listdir(self.destination):
                    os.chdir(os.path.join(self.destination, destination_folder[key]))
                    self.destination = os.path.join(self.destination, destination_folder[key])
                    self.search_file()

                else:
                    os.chdir(self.destination)
                    os.mkdir(destination_folder[key])
                    os.chdir(os.path.join(self.destination, destination_folder[key]))
                    self.destination = os.path.join(self.destination, destination_folder[key])
                    self.search_file()

    def search_file(self):
        for fl in os.listdir(self.source):
            if fl.endswith(self.filetype):
                self.move_file(fl)

    def move_file(self, filename):
        # moving the file code
        file_location = os.path.join(self.source, filename)
        shutil.move(file_location, self.destination)


for i in destination_folder.keys():

    obj = FileManager(i)
    del obj