# -*- coding: utf-8 -*-


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.Contact.edit_first_contact()
    app.session.logout()