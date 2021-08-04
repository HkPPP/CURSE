# Hank 

import pytest
import sys
sys.path.append(".")

from CURSEBackEnd.user import user

@pytest.fixture
def user_class():
    return user("TestFirst","TestLast","00000")
    

def test_searchAllCourse(user_class):
    courses = user_class.searchAllCourse()
    assert len(courses) == 5

def test_searchCourseByCRN(user_class):
    # Test correct input
    courses = user_class.searchCourseByCRN("00030001")
    assert len(courses) == 1

    # Wrong ID format
    courses = user_class.searchCourseByCRN("ab")
    assert len(courses) == 0

    # Out of bound
    courses = user_class.searchCourseByCRN("00030000")
    assert len(courses) == 0

def test_searchCourseByName(user_class):
    # Test correct input
    courses = user_class.searchCourseByName("Signals & Systems")
    assert len(courses) == 1

    # Test partial input (currently only work with full inputs)
    courses = user_class.searchCourseByName("Signals & ")
    assert len(courses) == 0

    # Test unregistered name
    courses = user_class.searchCourseByName("ABC")
    assert len(courses) == 0


def test_searchCoursebyYear(user_class):
    # Test correct input
    courses = user_class.searchCoursebyYear("2021")
    assert len(courses) == 5

    # Test wrong year
    courses = user_class.searchCoursebyYear("2000")
    assert len(courses) == 0

    # Test string input
    courses = user_class.searchCoursebyYear("ABC")
    assert len(courses) == 0


def test_searchCoursebySem(user_class):
    # Test correct input
    courses = user_class.searchCoursebySem("Su")
    assert len(courses) == 5

    # Test numerical input
    courses = user_class.searchCoursebySem("1212")
    assert len(courses) == 0

    # Test all uppercased input
    courses = user_class.searchCoursebySem("SU")
    assert len(courses) == 0


def test_searchCoursebyDept(user_class):
    courses = user_class.searchCoursebyDept("BSCO")
    assert len(courses) == 5

    # Test numerical input
    courses = user_class.searchCoursebyDept("1212")
    assert len(courses) == 0

    # Test all lowercased input
    courses = user_class.searchCoursebyDept("bsco")
    assert len(courses) == 0

