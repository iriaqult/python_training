# -*- coding: utf-8 -*-

from model.contact import contact


def test_add_contact(app): #тестовый метод прнимающий в качестве пвараметра фикстуру
    old_contacts = app.Contact.get_contact_list()
    app.Contact.create(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    new_contacts = app.Contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)




