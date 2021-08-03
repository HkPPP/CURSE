# Kevin

import pytest
import sys
sys.path.append(".")

from CURSEBackEnd.student import student

@pytest.fixture
def st():
    return student("Isaac","Newton","10001")

def test_registerCourseByCRN(st):
    assert st.registerCourseByCRN("00030001") == 1
    assert st.registerCourseByCRN("00030001") == 0
    st.dropCourseByCRN("00030001")
    assert st.registerCourseByCRN("123213") == 0