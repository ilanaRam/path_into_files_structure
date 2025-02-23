import pytest
from src.longest_absolute_file_path import ArrangePath
from src.folders_creation_with_same_name_added_number import CreateFoldersSameName


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

@pytest.fixture
def folders_obj():
    """
    fixture that will be called per test twice.
    first time to create and yield obj of the ArrangePath class
    second time for teardown
    """
    print("\n++++++++ START TEST +++++++++++++++++++++++")
    my_class_obj = CreateFoldersSameName()
    yield my_class_obj  # it is like return
    print("\n+++++++ END TEST ++++++++++++++++++++++++\n")