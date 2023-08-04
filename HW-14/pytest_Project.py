import json
import os
import pytest

from class_exceptions import AccessError, LevelError, LevelValueError
from class_user import User
from class_project import Project


@pytest.fixture
def get_file(tmpdir_factory):
    users = { "4": {"444": "Max"},
            "5": {"555": "Denis"},
            "7": {"722": "Kira"}}
    file_name = tmpdir_factory.mktemp("data").join("test_file.json")
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(users, f, indent=4)
    yield file_name
    os.remove(file_name)


def test_users_equal():
    user_1 = User('test', 1, 5)
    user_2 = User('test', 1, 5)
    assert user_1 == user_2


def test_user_login_in_list(project):
    user_1 = User('test1', 1, 1)
    project.login(user_1)
    assert project.admin == user_1


def test_user_login_not_in_list(project):
    with pytest.raises(AccessError):
        user_1 = User('test', 1, 1)
        project.login(user_1)


def test_add_user_success(project):
    admin = User('test1', 1, 1)
    user_to_add = User('test', 2, 1)
    project.login(admin)
    project.add_user(user_to_add)
    assert user_to_add in project.users_lst


def test_add_user_fail(project):
    with pytest.raises(LevelError):
        admin = User('test3', 3, 2)
        user_to_add = User('test', 2, 1)
        project.login(admin)
        project.add_user(user_to_add)


def test_remove_user_success(project):
    admin = User('test1', 1, 1)
    user_to_del = User('test2', 2, 1)
    project.login(admin)
    project.remove_user(user_to_del)
    assert user_to_del not in project.users_lst


def test_remove_user_fail(project):
    with pytest.raises(LevelError):
        admin = User('test4', 4, 2)
        user_to_del = User('test1', 1, 1)
        project.login(admin)
        project.remove_user(user_to_del)


