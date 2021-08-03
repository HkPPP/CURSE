import pytest
import sys
sys.path.append(".")

from CURSEBackEnd.userLogin import userLogin
from CURSEBackEnd.user import user

@pytest.fixture
def ul():
    ul = userLogin()
    yield ul
    del ul

def test_logIn_logOut(ul):
    
    u = ["Admin", "30001", "obamab"]
    a = ul.logIn(u[0], u[1], u[2])
    assert a == 1

    u = ["Instructor", "20002", "mandelan"]
    b = ul.logIn(u[0], u[1], u[2])
    assert b == 1

    u = ["Student", "10007", "jemisonm"]
    c = ul.logIn(u[0], u[1], u[2])
    assert c == 1

    u = ["Admin", "AGB", "12"]
    d = ul.logIn(u[0], u[1], u[2])
    assert d == 0

    ul.logOut(a)
    assert isinstance(a, user) == 0
    
    ul.logOut(b)
    assert isinstance(b, user) == 0

    ul.logOut(c)
    assert isinstance(c, user) == 0

    ul.logOut(d)
    assert isinstance(d, user) == 0
