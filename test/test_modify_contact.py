# -*- coding: utf-8 -*-

from model.contact import contact


def test_edit_first_contact_name(app):
    #app.session.login(username="admin", password="secret")
    app.Contact.modify_first_contact(contact(name="Jane"))
    app.session.logout()

def test_edit_first_contact_email(app):
    #app.session.login(username="admin", password="secret")
    app.Contact.modify_first_contact(contact(email="jane@jane.ru"))
    app.session.logout()