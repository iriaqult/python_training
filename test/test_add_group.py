# -*- coding: utf-8 -*-
from model.group import group
import pytest


testdata = [
    group(name="test", header="fgdjsl", footer="dhjkd")
    group(name="", header="", footer="")
]

@pytest.mark.parametrize("Group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, Group):
    pass
    old_groups = app.group.get_group_list()
    app.group.create(Group)
    assert len(old_groups) +1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(Group)
    assert sorted(old_groups, key = group.id_or_max) == sorted(new_groups, key=group.id_or_max)


#def test_empty_group(app):
#    old_groups = app.group.get_group_list()
#    Group = group(name="", header="", footer="")
#    app.group.create(Group)
#    assert len(old_groups) +1 == len(app.group.count())
#    new_groups = app.group.get_group_list()
#    old_groups.append(Group)
#    assert sorted(old_groups, key = group.id_or_max) == sorted(new_groups, key=group.id_or_max)

