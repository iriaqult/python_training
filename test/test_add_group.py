# -*- coding: utf-8 -*-
from model.group import group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="test", header="fgdjsl", footer="dhjkd"))
    app.session.logout()


def test_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(group(name="", header="", footer=""))
    app.session.logout()
