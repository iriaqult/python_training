# -*- coding: utf-8 -*-

from model.contact_n import Contact_n
from random import randrange

def test_edit_first_contact_name(app):
    if app.Contact.count() == 0:
        app.Contact.create(Contact_n(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    old_contacts = app.Contact.get_contact_list()
    index = randrange(len(old_contacts))
    Contact = Contact_n(name="Jane", last_name="Birkin")
    Contact.id = old_contacts[index].id
    app.Contact.modify_contact_by_index(Contact, index)
    assert len(old_contacts) == app.Contact.count()
    new_contacts = app.Contact.get_contact_list()
    old_contacts[index] = Contact
    assert sorted(old_contacts, key=Contact_n.id_or_max) == sorted(new_contacts, key=Contact_n.id_or_max)

#def test_edit_first_contact_email(app):
#    if app.Contact.count() == 0:
#        app.Contact.create(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
#    old_contacts = app.Contact.get_contact_list()
#    Contact = contact(email="jane@jane.ru")
#    Contact.id = old_contacts[0].id
#    app.Contact.modify_first_contact(Contact)
#    new_contacts = app.Contact.get_contact_list()
#    assert len(old_contacts) == len(new_contacts)
#    old_contacts[0] = Contact
#    assert sorted(old_contacts, key=contact.id_or_max) == sorted(new_contacts, key=contact.id_or_max)
