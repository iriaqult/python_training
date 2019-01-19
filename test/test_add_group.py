# -*- coding: utf-8 -*-
from model.group import group
from fixture.application import Application
import pytest

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="test", header="fgdjsl", footer="dhjkd"))
    app.session.logout()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="", header="", footer=""))
    app.session.logout()
