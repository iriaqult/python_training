

from model.group import group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(group(name = 'test'))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(group(name="new group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(group(name='test'))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(group(header="new header"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
