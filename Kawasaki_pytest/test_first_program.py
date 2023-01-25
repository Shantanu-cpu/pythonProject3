
def test_validation_01():
    x=10
    y=10
    assert x==y


def test_validation_02():
    x=10
    y=10
    assert not x==y


def test_validation_03():
    x=10
    y=20
    assert not x==y


def test_validation_04():
    name='Shantanu'
    sentance='Shantanu is learning python'
    assert name in sentance


def test_validation_05():
    name='Shantanu'
    sentance='Shantanu is learning python'
    assert name is sentance











































































































