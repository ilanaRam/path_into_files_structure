import pytest
from src.longest_absolute_file_path import ArrangePath

@pytest.fixture
def files_obj():
    """
    fixture that will be called per test twice.
    first time to create and yield obj of the ArrangePath class
    second time for teardown
    """
    print("\n++++++++ START TEST +++++++++++++++++++++++")
    my_class_obj = ArrangePath()
    yield my_class_obj  # it is like return
    print("\n+++++++ END TEST ++++++++++++++++++++++++\n")
