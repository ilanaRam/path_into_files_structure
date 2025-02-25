import pytest
from src.longest_absolute_file_path import ArrangePath
from src.unique_directories_names import CreateFoldersSameName


@pytest.fixture
def files_obj():
    """
    fixture that will be called per test twice.
    first time to create and yield obj of the ArrangePath class
    second time for teardown
    """
    print("\n++++++++ Files TEST START +++++++++++++++++++++++")
    my_class_obj = ArrangePath()
    yield my_class_obj  # it is like return
    print("\n+++++++ Files TEST END ++++++++++++++++++++++++\n")

@pytest.fixture
def folders_obj():
    """
    fixture that will be called per test twice.
    first time to create and yield obj of the ArrangePath class
    second time for teardown
    """
    print("\n++++++++ Folders TEST START +++++++++++++++++++++++")
    my_class_obj = CreateFoldersSameName()
    yield my_class_obj  # it is like return
    print("\n+++++++ Folders TEST END ++++++++++++++++++++++++\n")