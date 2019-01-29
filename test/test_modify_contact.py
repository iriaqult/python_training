# -*- coding: utf-8 -*-

from model.contact import contact


def test_edit_first_contact_name(app):
    app.Contact.modify_first_contact(contact(name="Jane"))

def test_edit_first_contact_email(app):
    app.Contact.modify_first_contact(contact(email="jane@jane.ru"))
