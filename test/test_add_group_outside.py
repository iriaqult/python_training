# -*- coding: utf-8 -*-
from model.groupn import Groupn
import pytest
from data.add_group import constant as testdata

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(group)
    x = old_groups
    assert sorted(old_groups, key = Groupn.id_or_max) == sorted(new_groups, key=Groupn.id_or_max)