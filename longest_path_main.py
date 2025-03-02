from src.longest_absolute_file_path import ArrangePath
import pytest


def main():
    my_path = r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tfile3.txt"

    path_obj = ArrangePath()
    path_obj.set_files_structure_path(my_path)
    longest_len = path_obj.calculate_longest_file_path()
    print(f"The longest len is: {longest_len}")

if __name__ == '__main__':
    main()