

from model.group import group


def test_modify_group_name(app):
    app.group.modify_first_group(group(name="new group"))


def test_modify_group_header(app):
    app.group.modify_first_group(group(header="new header"))
