# -*- coding: utf-8 -*-
from model.group import group


def test_add_group(app):
    old_groups = app.group.get_group_list()
    Group = group(name="test", header="fgdjsl", footer="dhjkd")
    app.group.create(Group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) +1 == len(new_groups)
    old_groups.append(Group)
    assert sorted(old_groups, key = group.id_or_max) == sorted(new_groups, key=group.id_or_max)


def test_empty_group(app):
    old_groups = app.group.get_group_list()
    Group = group(name="", header="", footer="")
    app.group.create(Group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) +1 == len(new_groups)
    old_groups.append(Group)
    assert sorted(old_groups, key = group.id_or_max) == sorted(new_groups, key=group.id_or_max)

