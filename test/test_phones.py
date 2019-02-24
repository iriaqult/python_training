import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.Contact.get_contact_list()[0]
    contact_from_edit_page = app.Contact.get_contact_info_from_edit_page(0)
    assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)
    assert contact_from_home_page.mobilephone == clear(contact_from_edit_page.mobilephone)
    assert contact_from_home_page.secondaryphone == clear(contact_from_edit_page.secondaryphone)

def clear(s):
    re.sub("[() -]", "", s)