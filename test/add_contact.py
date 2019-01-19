# -*- coding: utf-8 -*-

from model.contact import contact


def test_add_contact(app): #тестовый метод прнимающий в качестве пвараметра фикстуру
    app.session.login("admin", "secret")
    app.Contact.create(contact(name="Ivan", middle_name="Ivanovich", last_name="Ivanov", email="ivan@ivan.ru"))
    app.session.logout()



