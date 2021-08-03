# Kevin 

import pytest
import sys
sys.path.append(".")

from CURSEBackEnd.instructor import instructor
from CURSEBackEnd.sql_class import sql_functions

ins = instructor("Joseph", "Fourier", "20001")


def test_getSchedule():
    courses = ins.getSchedule()
    assert len(courses) == 1

def test_getRosterFromACourse():
    student = ins.getRosterFromACourse("00030001")
    assert len(student) == 2

    student = ins.getRosterFromACourse("21312")
    assert len(student) == 0
