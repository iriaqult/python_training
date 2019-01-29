# -*- coding: utf-8 -*-
from model.group import group


def test_add_group(app):
    app.group.create(group(name="test", header="fgdjsl", footer="dhjkd"))


def test_empty_group(app):
    app.group.create(group(name="", header="", footer=""))

