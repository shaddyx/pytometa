from pytometa import tools

class _A(object):
    a=None
    b=1
    c=""

def test_GetAllFields():
    fields = tools.getAllFields(_A)
    assert "a" in fields
    assert "b" in fields
    assert "c" in fields

def test_GetAllFieldItems():
    fields = tools.getAllFieldItems(_A)
    assert ("a", None) in fields
    assert ('b', 1) in fields
    assert ('c', '') in fields