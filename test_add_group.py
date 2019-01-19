# -*- coding: utf-8 -*-
from group import group
from application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.login(username="admin", password="secret")
    app.group_creation(group(name="test", header="fgdjsl", footer="dhjkd"))
    app.logout()


def test_empty_group(app):
    app.login(username="admin", password="secret")
    app.group_creation(group(name="", header="", footer=""))
    app.logout()
