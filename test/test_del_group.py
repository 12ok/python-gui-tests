from random import randrange


def test_delete_group(app):
    if len(app.groups.get_group_list()) == 0:
        app.groups.add_new_group("group")
    old_groups = app.groups.get_group_list()
    print(old_groups)
    app.groups.delete_group(randrange(len(old_groups)))
    new_groups = app.groups.get_group_list()
    old_groups.remove(old_groups[0])
    assert sorted(old_groups) == sorted(new_groups)