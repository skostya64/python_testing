# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from new import New


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_new(app):
    app.login(username="admin", password="secret")
    app.create_new(New(firstname="Konstantin", middlename="Styagailo", address="Parkovaya, 8"))
    app.logout()


def test_empty_new(app):
    app.login(username="admin", password="secret")
    app.create_new(New(firstname="", middlename="", address=""))
    app.logout()



