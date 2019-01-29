# -*- coding: utf-8 -*-


def test_del_first_contact(app):
    app.Contact.delete_first_contact()
