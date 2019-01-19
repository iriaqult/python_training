# -*- coding: utf-8 -*-

from contact import contact
from appc import AppContact
import pytest

@pytest.fixture
def app(request):
    fixture = AppContact()
    request.addfinalizer(fixture.destroy) #указание на то как д.бразрушена фикстура
    return fixture

def test_add_contact(app): #тестовый метод прнимающий в качестве пвараметра фикстуру
    app.login("admin", "secret")
    app.add_contact(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    app.logout()



