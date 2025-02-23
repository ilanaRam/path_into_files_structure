import pytest
from src.folders_creation_with_same_name_added_number import CreateFoldersSameName

class TestDifferentFoldersNames:

    # Parametrized fixture, single test is being executed per test parameter
    @pytest.mark.parametrize("folders_names_list",# <---- this is a name of the fixture, each time the fixture will hold 1 path to test by a test
                             [
                                 (["gta", "gta(1)", "gta(2)", "gta", "avalon"]),
                                 (["onepiece","onepiece(1)","onepiece(2)","onepiece(3)","onepiece"]),
                                 (["pes","fifa","gta","pes(2019)"]),
                                 (["gta"]),
                                 ([""]),
                                 ([])
                             ])
    def test_build_files_structure_and_return_longest_path(self,
                                                           folders_obj,
                                                           folders_names_list):

        arranged_list = folders_obj.arrange_directories_list(folders_names_list)
        assert len(folders_names_list) == len(arranged_list) or not arranged_list , "incorrect length of the resulted list"
        print(f"The arranged list of directories is: {arranged_list}")
