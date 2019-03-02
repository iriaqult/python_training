# -*- coding: utf-8 -*-

from model.contact_n import Contact_n
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + " "*10 #из каких символов случайно выбираем, чтобы увеличить частоту пробелов, умножили их количество на 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact_n(name="", middle_name="", last_name="", email="")] + [
    Contact_n(name=random_string("name", 10), middle_name = random_string("middle_name", 20),
              last_name= random_string("last_name", 10), email=random_string("last_name", 10))
    for i in range(5)
]

@pytest.mark.parametrize("Contact1", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, Contact1): #тестовый метод прнимающий в качестве пвараметра фикстуру
    old_contacts = app.Contact.get_contact_list()
    app.Contact.create(Contact1)
    assert len(old_contacts) + 1 == app.Contact.count()
    new_contacts = app.Contact.get_contact_list()
    old_contacts.append(Contact1)
    assert sorted(old_contacts, key = Contact_n.id_or_max) == sorted(new_contacts, key = Contact_n.id_or_max)




