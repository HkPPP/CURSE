import pytest
import sys
sys.path.append(".")

from CURSEBackEnd.admin import admin
from CURSEBackEnd.sql_class import sql_functions

sql = sql_functions()

@pytest.fixture
def adm():
    yield admin("Barack","Obama","30001")

def test_add_and_remove_courses(adm):
    adm.addNewCourse("Test")
    course = sql.select_from_where("COURSE", "*", "CRN", "'00030006'")
    assert len(course) == 1
    adm.removeCourseByCRN("00030006")
    course = sql.select_from_where("COURSE", "*", "CRN", "'00030006'")
    assert len(course) == 0

    

