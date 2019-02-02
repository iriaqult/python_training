# -*- coding: utf-8 -*-

from model.contact import contact


def test_edit_first_contact_name(app):
    if app.Contact.count() == 0:
        app.Contact.create(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    app.Contact.modify_first_contact(contact(name="Jane"))

def test_edit_first_contact_email(app):
    if app.Contact.count() == 0:
        app.Contact.create(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    app.Contact.modify_first_contact(contact(email="jane@jane.ru"))
