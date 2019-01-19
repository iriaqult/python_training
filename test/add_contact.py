# -*- coding: utf-8 -*-

from model.contact import contact
from fixture.appc import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app): #тестовый метод прнимающий в качестве пвараметра фикстуру
    app.login("admin", "secret")
    app.add_contact(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    app.logout()



