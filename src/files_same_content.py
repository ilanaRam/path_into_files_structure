from collections import defaultdict
from typing import List, Dict
from pathlib import Path
from typing import List
import re
import zlib

class FilesSameContent:
    # __next__ magic method controls class object creation before it's creation, it is called automatically before def __init__(self):
    # def __new__(self):
    #     print(f"Hi here we start - now will be called __init__() magic method of the class !!")

    def __init__(self):
        self.files_content_list: List[str] = []

    # __del__ magic method controls class object cleanup, it is called automatically before program ends up
    def __del__(self):
        print(f"List of items will be deleted right now")
        del self.files_content_list

    # Defines human-readable string representation of obj
    # if we have a list of objects of same class and we come to print one by one
    # will be called per object
    # else if class has a list = then we can implement the way will get all list elems as a string with coma separated
    # def __str__(self):
    #     items_str = ",".join(self.files_content_list) if self.files_content_list is not None else "No items in the list yet"
    #     print(f"The items are: {items_str}")

    def find_files_same_content(self, files_list: List[str]) -> List[str]:
        """
        """
        assert isinstance(files_list, List) or files_list or len(files_list) == 0, "Bad directories list ###"
        self.files_content_list = files_list.copy()
        print(f"\n\nThis is the list of the files (with content): ")
        print(self.files_content_list)
        tmp_dict = {}
        tmp_file_contents_list = []

        print(f"Start arranging the files by their content in the new list ...")
        for files_content_item in self.files_content_list:
            directory = files_content_item[: files_content_item.index(' ')]
            file_s_names_list = files_content_item[len(directory): ].split()  # get out only the file name without content 1.txt(fjfjfjf) => 1.txt

            for file_content in file_s_names_list:
                file_name = file_content[:file_content.index("(")]
                file_content = file_content[file_content.index("(")+1:-1]
                crc32= zlib.crc32(file_content.encode())
                tmp_dict.setdefault(crc32,[]).append({"dir":directory,
                                                      "file_name":file_name,
                                                      "file_content":file_content })

        print(f"\nThe print by a content is: ")
        for key, val in tmp_dict.items():
            print(f"Files are: {val}")
