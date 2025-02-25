import pytest
from src.files_same_content import FilesSameContent

class TestDifferentFoldersNames:

    # Parametrized fixture, single test is being executed per test parameter
    @pytest.mark.parametrize("file_contents_list",# <---- this is a name of the fixture, each time the fixture will hold 1 path to test by a test
                             [
                                 (["root/a 1.txt(abcd) 2.txt(efgh)", # here we see a folder: root/a     with 2 files: 1.txt(abcd), 2.txt(efgh)
                                   "root/c 3.txt(abcd)",             # here we see a folder: root/c     with file:    3.txt(abcd)
                                   "root/c/d 4.txt(efgh)",           # here we see a folder: root/c/d   with file:    4.txt(efgh)
                                   "root 4.txt(efgh)"]),

                                 (["root/a 1.txt(abcd) 2.txt(efgh)",
                                   "root/c 3.txt(abcd)",
                                   "root/c/d 4.txt(efgh)"])
                             ])
    def test_build_files_structure_and_return_longest_path(self,
                                                           contents_obj,
                                                           file_contents_list):
        contents_obj.find_files_same_content(file_contents_list)
