

from model.groupn import Groupn
from random import randrange

def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Groupn(name ='test'))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    Group = Groupn(name="new group")
    Group.id = old_groups[index].id
    app.group.modify_group_by_index(Group, index)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = Group
    assert sorted(old_groups, key=Groupn.id_or_max) == sorted(new_groups, key=Groupn.id_or_max)


#def test_modify_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(group(name='test'))
#    old_groups = app.group.get_group_list()
#    Group = group(header="new header")
#    Group.id = old_groups[0].id
#    app.group.modify_first_group(Group)
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)
#    old_groups[0] = Group
#    assert sorted(old_groups, key=group.id_or_max) == sorted(new_groups, key=group.id_or_max)
