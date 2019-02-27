import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.Contact.get_contact_list()[0]
    contact_from_edit_page = app.Contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.all_phones_from_homepage == merge_phones_like_on_homepage(contact_from_edit_page)


def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.Contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.Contact.get_contact_info_from_edit_page(0)
    #доработать обратную проверку по рег.выражению для задания 14
    assert contact_from_view_page.all_phones_from_viewpage == merge_phones_like_on_view_page(contact_from_edit_page)


def clear(s):
    return re.sub("[() -]", "", s)


def merge_phones_like_on_homepage(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear(x),
                                                   filter(lambda x: x is not None,
                                                          [contact.homephone,contact.mobilephone, contact.workphone]))))

def merge_phones_like_on_view_page(contact):
    # доработать обратную проверку по рег.выражению для задания 14
    return "\n".join(filter(lambda x: x != "", filter(lambda x: x is not None,
                                         ["H:",contact.homephone,"M:", contact.mobilephone, "W:", contact.workphone, "F:", contact.secondaryphone])))

