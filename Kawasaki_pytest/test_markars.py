import pytest


@pytest.mark.skip
def test_method_01():
    x='terminal and command promt work as same'
    y='command promt and terminal work as same'
    assert x in y


@pytest.mark.skip(reason='it is a defect')
def test_method_02():
    x = 'terminal and command promt work as same'
    y = 'command promt and terminal work as same'
    assert x is y


@pytest.mark.skipif(False,reason="both are not same")
def test_method_03():
    x = 'terminal and command promt work as same'
    y = 'command promt and terminal work as same'
    assert x == y


def test_method_04():
    x = 'terminal and command promt work as same'
    y = 'command promt and terminal work as same'
    assert not x == y


@pytest.mark.xfail
def test_method_05():
    x = 'terminal '
    y = 'command promt and terminal work as same'
    assert x in y


def test_method_06():
    x = ' command promt '
    y = 'command promt and terminal work as same'
    assert x in y


@pytest.mark.parametrize("username,password",[("Shantanu","python"),
                                              ("yes","no")
                                                     ])
def test_method_07(username,password):
    print(username+' is learnig '+password)
















































