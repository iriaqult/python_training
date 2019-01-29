from fixture.application import Application
from fixture.session import SessionHelper
import pytest

@pytest.fixture(scope= 'session')
def app(request):
    #global fixture
    #if fixture is None:
    fixture = Application()
    #else:
    #    if not fixture
    fixture.session.ensure_login(username="admin", password="secret")
    request.addfinalizer(fixture.destroy)
    return fixture