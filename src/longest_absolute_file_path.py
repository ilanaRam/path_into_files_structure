import re
from typing import List, Dict
from pathlib import Path


class ArrangePath:
    """ 
    class deals with 'file structure' given us as a string
    Exp for a 'file structure' given us as a string:
    # "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

    returns a length of the longest path to a file

    Look at the README.txt and get the idea of how I accessed to the solution
    """
    def __init__(self):
        print(f"Object to be created ..")
        self.my_path: str = None
        self.files_dict: Dict = {}

    def count_t_chars(self, my_str: str) -> tuple[int, str]:
        print(f"\n\nChecking ...")
        all_matches_list = re.findall(r'\\t+', my_str) # + means 1 or more times
        rest_of_string = re.sub(r'\\t+', # look for this regex
                                '',         # when find, replace with this string (empty string) - means remove the \\t founded by regex
                                my_str)          # in this string
        print(f"The item is: {rest_of_string}")
        # print(f"This is what was found: {all_matches_list}")
        print(f"Number of found '\\t' chars is: {len(all_matches_list)}")
        return len(all_matches_list), rest_of_string

    def find_longest_item_path(self) -> int:
        max_path_len = 0
        for item, path in self.files_dict.items():
            # !!! there is no way to calculate len of the Path type, need to cast back to str !!!!
            if len(str(item)) > max_path_len:
                max_path_len = len(str(item))
        return max_path_len

    def create_database_from_path(self):
        # "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
        root_path = None
        prev_path = None
        item_path = None

        print(f"\n\nCreating data base from the path ...")

        path_lines = self.my_path.split(r'\n')
        for line in path_lines: 
            print(line)

        for index, line in enumerate(path_lines):
            num_of_t, item = self.count_t_chars(line)
            item = Path(item)

            if num_of_t == 0:
                root_path = item
                item_path = prev_path = root_path

            elif num_of_t == 1:
                #if not item.is_file(): # is_file() - returns True if the path 'exists' and is a 'file'. In  this case we will always will get False as this file in this path isnt exisitng!!
                # better way will be to ask if item has suffix
                item_path = root_path / item

                if not item.suffix in [".txt", ".ext"]: # here we look in set (we can replace it also with set {"txt", ".ext"})
                    prev_path = item_path
                else:
                    prev_path = root_path

            elif num_of_t == 2 or num_of_t == 3:
                item_path = prev_path / item

                if not item.suffix in {".txt", ".ext"}:
                    prev_path = prev_path / item
                else:
                    prev_path = prev_path

            # enter into the dictionary (the data base)
            self.files_dict.setdefault(item_path, # key
                                       prev_path) # value
        print(f"\n\nPrinting the dict:")
        for item, path in self.files_dict.items():
            print(f"Item: {item}, path: {path}")

    def set_files_structure_path(self, files_path: str):
        assert self.validate_input(files_path) == True, f"Bad input path: {self.my_path}, App failed"
        self.my_path = files_path

    def validate_input(self, files_structure_path) -> bool:
        print(f"\n\nChecking Validity of the input path ...")
        if files_structure_path is None or len(files_structure_path) == 0:
            print(f"Incorrect path")
            return False
        print(f"Good path")
        return True

    def calculate_longest_file_path(self) -> int:
        """
        This method will calculate the length of the longest file path
        Will be used validation of the path & translation of the path into files structure
        That later length of the longest path will be calculation
        """
        self.create_database_from_path()
        return self.find_longest_item_path()


