from collections import defaultdict
from typing import List, Dict
from pathlib import Path
from typing import List
import re

class CreateFoldersSameName:
    # __next__ magic method controls class object creation before it's creation, it is called automatically before def __init__(self):
    # def __new__(self):
    #     print(f"Hi here we start - now will be called __init__() magic method of the class !!")

    def __init__(self):
        self.folders_list: List[str] = []

    # __del__ magic method controls class object cleanup, it is called automatically before program ends up
    def __del__(self):
        print(f"List of items will be deleted right now")
        del self.folders_list

    # Defines human-readable string representation of obj
    # if we have a list of objects of same class and we come to print one by one
    # will be called per object
    # else if class has a list = then we can implement the way will get all list elems as a string with coma separated
    def __str__(self):
        items_str = ",".join(self.folders_list) if self.folders_list is not None else "No items in the list yet"
        print(f"The items are: {items_str}")

    def arrange_directories_list(self, dirs_list: List[str]) -> List[str]:
        """
        My approach is to build a dict, where a key is a base dir name without a index (if any).
        Then if index exists in current dir name it will be indicated in the list (value per of this key)
        if dir name without index, in the dict will be added into a list index 0
        if a dir name already has index gpt(1), then a key gpt, a value 1
        eventually I will have:
        [gpt, gpt(1), gpt, alon] -> {gpt: [0,1,2], alon: [0]} then I restore dir folders correct names by running on the dict and comprehending key + values
        result: [gpt,gpt(1),gpt(2), alon]  this is the way the OS deals with duplicated dir names - it gives indexes
        """
        assert isinstance(dirs_list, List) or dirs_list or len(dirs_list) == 0, "Bad directories list ###"

        print(f"\n\nThis is the list of the folder names: ")
        print(dirs_list)
        tmp_dict = {}

        print(f"Start arranging the dir names in the new list with appropriate names")
        for current_dir in dirs_list:
            if "(" in current_dir:
                # here I will use string (iterable) slicing
                base_name = current_dir[: current_dir.index("(")]  # get out only the dir name without (1), if I see this: "gta(1)" I extruct only "gta"

                index = current_dir[current_dir.index("(")+1 : -1] # get out only the number without the (), if I see this: "gta(1)" I extruct only "1"

                # here I update dict
                tmp_dict.setdefault(base_name,[]).append(int(index))
            else:
                if not tmp_dict.get(current_dir, []):
                    tmp_dict.setdefault(current_dir,[]).append(0)
                else:
                    last_index = tmp_dict.get(current_dir, [])[-1]
                    tmp_dict.setdefault(current_dir,[]).append(last_index +1)
            #print(f"Dict: {tmp_dict}")

        # restore the original list with required corrections for folder names (the one that duplicate)
        for folder_name, folder_index_list in tmp_dict.items():
            #print(f"Folder name: {folder_name}, indexes are: {folder_index_list}")

            for index in folder_index_list:
                if index == 0:
                    self.folders_list.append(folder_name)
                else:
                    self.folders_list.append(f"{folder_name}({index})")
        #print(f"Folders are: {self.folders_list} \n")
        return self.folders_list

    def create_directories_by_os(self):
        print(f"Creation and naming of the directories ... started")



