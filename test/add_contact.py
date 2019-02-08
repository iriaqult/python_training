# -*- coding: utf-8 -*-

from model.contact import contact


def test_add_contact(app): #тестовый метод прнимающий в качестве пвараметра фикстуру
    old_contacts = app.Contact.get_contact_list()
    Contact = contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru")
    app.Contact.create(Contact)
    new_contacts = app.Contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(Contact)
    assert sorted(old_contacts, key = contact.id_or_max) == sorted(new_contacts, key = contact.id_or_max)




