from model.groupn import Groupn

def test_group_list(app,db):
    ui_list = app.group.get_group_list()
    db_list = db.get_group_list()
    assert sorted(ui_list, key=Groupn.id_or_max()) == sorted(db_list, key=Groupn.id_or_max())