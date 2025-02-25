from src.files_same_content import FilesSameContent
import pytest


def main():
    file_contant_obj = FilesSameContent()
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)", # here we see a folder: root/a     with 2 files: 1.txt(abcd), 2.txt(efgh)
             "root/c 3.txt(abcd)",             # here we see a folder: root/c     with file:    3.txt(abcd)
             "root/c/d 4.txt(efgh)",           # here we see a folder: root/c/d   with file:    4.txt(efgh)
             "root 4.txt(efgh)"]               # here we see a folder: root       with file:    4.txt(efgh)
    file_contant_obj.find_files_same_content(paths)


    file_contant_obj = FilesSameContent()
    paths = ["root/a 1.txt(abcd) 2.txt(efgh)",
             "root/c 3.txt(abcd)",
             "root/c/d 4.txt(efgh)"]
    file_contant_obj.find_files_same_content(paths)




if __name__ == '__main__':
    main() # this means first run all tests then run this main()
