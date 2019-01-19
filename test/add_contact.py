# -*- coding: utf-8 -*-

from model.contact import contact
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app): #тестовый метод прнимающий в качестве пвараметра фикстуру
    app.session.login("admin", "secret")
    app.Contact.create(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    app.session.logout()



