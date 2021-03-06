# -*- coding: utf-8 -*-
from model.groupn import Groupn
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #из каких символов случайно выбираем, чтобы увеличить частоту пробелов, умножили их количество на 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

#testdata = [group(name=name, header=header, footer=footer) #либо None либо случайный , всего 8 комбинаций
#            for name in ["",random_string("name", 10)]
#            for header in ["",random_string("header", 20)]
#            for footer in ["",random_string("footer", 20)]
#]

testdata = [Groupn(name="", header="", footer="")] + [
    Groupn(name=random_string("name", 10), header = random_string("header", 20), footer= random_string("footer", 20))
    for i in range(5)
]

@pytest.mark.parametrize("Group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app, Group):
    old_groups = app.group.get_group_list()
    app.group.create(Group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(Group)
    x = old_groups
    assert sorted(old_groups, key = Groupn.id_or_max) == sorted(new_groups, key=Groupn.id_or_max)




