# -*- coding: utf-8 -*-
from model.group import group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(group(name="test", header="fgdjsl", footer="dhjkd"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) +1 == len(new_groups)


def test_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

