# -*- coding: utf-8 -*-
from model.contact import contact


def test_del_first_contact(app):
    if app.Contact.count() == 0:
        app.Contact.create(contact(name = 'test'))
    app.Contact.delete_first_contact()
