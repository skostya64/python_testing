# -*- coding: utf-8 -*-

from new import New


def test_add_new(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new(New(firstname="Konstantin", middlename="Styagailo", address="Parkovaya, 8"))
    app.session.logout()


def test_empty_new(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_new(New(firstname="", middlename="", address=""))
    app.session.logout()



