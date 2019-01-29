

from model.group import group


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(group(name = 'test'))
    app.group.modify_first_group(group(name="new group"))


def test_modify_group_header(app):
    if app.group.count() == 0:
        app.group.create(group(name='test'))
    app.group.modify_first_group(group(header="new header"))
