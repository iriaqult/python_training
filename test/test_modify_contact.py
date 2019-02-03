# -*- coding: utf-8 -*-

from model.contact import contact


def test_edit_first_contact_name(app):
    if app.Contact.count() == 0:
        app.Contact.create(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    old_contacts = app.Contact.get_contact_list()
    app.Contact.modify_first_contact(contact(name="Jane"))
    new_contacts = app.Contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)

def test_edit_first_contact_email(app):
    if app.Contact.count() == 0:
        app.Contact.create(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    old_contacts = app.Contact.get_contact_list()
    app.Contact.modify_first_contact(contact(email="jane@jane.ru"))
    new_contacts = app.Contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
