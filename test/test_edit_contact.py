# -*- coding: utf-8 -*-

from model.contact import contact


def test_edit_first_contact(app):
    app.session.login(username="admin", password="secret")
    app.Contact.edit_first_contact(contact(name="Jane", middle_name="Petrovna", last_name="Air", email="jane@jane.ru"))
    app.session.logout()