# -*- coding: utf-8 -*-

from model.group import group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(group(name="changed", header="lalala", footer="ololol"))
    app.session.logout()