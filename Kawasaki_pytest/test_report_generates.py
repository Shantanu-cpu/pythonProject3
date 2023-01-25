import pytest


def test_one_01():
    x='regrassion testing'
    y='automation used for retesting and regression '
    assert x==y

@pytest.mark.regression
def test_one_02():
    x='regrassion testing'
    y='automation used for retesting and regression '
    assert x in y


def test_one_03():
    x='regrassion testing'
    y='automation used for retesting and regression '
    assert x is y



def test_one_04():
    x='regrassion testing'
    y='automation used for retesting and regression '
    assert not x==y























































































