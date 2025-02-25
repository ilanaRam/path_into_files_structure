from src.unique_directories_names import CreateFoldersSameName
import pytest


def main():
    folders_names_obj = CreateFoldersSameName()
    folder_names_list = ["gta", "gta(1)", "gta(2)", "gta", "avalon"]
    arranged_list = folders_names_obj.arrange_directories_list(folder_names_list)
    print(f"The arranged list of directories is: {arranged_list}")

    folders_names_obj = CreateFoldersSameName()
    folder_names_list = ["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]
    arranged_list = folders_names_obj.arrange_directories_list(folder_names_list)
    print(f"The arranged list of directories is: {arranged_list}")

    folders_names_obj = CreateFoldersSameName()
    folder_names_list = ["pes","fifa","gta","pes(2019)"]
    arranged_list = folders_names_obj.arrange_directories_list(folder_names_list)
    print(f"The arranged list of directories is: {arranged_list}")

if __name__ == '__main__':
    main() # this means first run all tests then run this main()
