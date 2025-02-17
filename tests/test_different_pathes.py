
import pytest


class TestDifferentPathes:

    # Parametrized fixture, single test is being executed per test parameter
    @pytest.mark.parametrize("files_path",
                             # <---- this is a name of the fixture, each time the fixture will hold 1 path to test by a test
                             [
                                 (r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"),
                                 (r"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext\n\tfile3.txt")
                             ])
    def test_build_files_structure_and_return_longest_path(self,
                                                           files_obj,
                                                           files_path):
        print(f"The test param (path) is: {files_path}")
        try:
            files_obj.set_files_structure_path(files_path) is True, "Test failed, the validation of the test folder path"
        except Exception as ee:
            pytest.fail(f"Given bad files path, raised exception: {ee}")

        longest_len = files_obj.calculate_longest_file_path()
        assert longest_len > 0, "Incorrect length result"
        print(f"The longest len is: {longest_len}")






