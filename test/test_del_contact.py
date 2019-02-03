# -*- coding: utf-8 -*-
from model.contact import contact


def test_del_first_contact(app):
    if app.Contact.count() == 0:
        app.Contact.create(contact(name = 'test'))
    old_contacts = app.Contact.get_contact_list()
    app.Contact.delete_first_contact()
    new_contacts = app.Contact.get_contact_list()
    assert len(old_contacts)-1 == len(new_contacts)
