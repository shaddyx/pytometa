import typing

from pytometa import tools, loader
from pytometa.descriptors import TypeDescriptor, ListDescriptor, DictDescriptor

class _A(object):
    a = TypeDescriptor(int)
    b = TypeDescriptor(str)

class _C(object):
    inner = DictDescriptor(TypeDescriptor(_A))  # type: typing.List

class _D(object):
    inner = DictDescriptor(_A)  # type: typing.List


def test_load_dict_object():

    res = loader.load_from_dict({
        "inner":[
            {
                "a": 1,
                "b": 2,
            },
            {
                "a": 3,
                "b": 4,
            }
        ]
    }, _C())
    assert type(res.inner) is list
    assert len(res.inner) == 2
    assert res.inner[0].a == 1
    assert res.inner[1].a == 3
    assert res.inner[0].b == '2'
    assert res.inner[1].b == '4'



def test_load_list_object_no_typedescriptor():

    res = loader.load_from_dict({
        "inner":[
            {
                "a": 1,
                "b": 2,
            },
            {
                "a": 3,
                "b": 4,
            }
        ]
    }, _D())
    assert type(res.inner) is list
    assert len(res.inner) == 2
    assert res.inner[0].a == 1
    assert res.inner[1].a == 3
    assert res.inner[0].b == '2'
    assert res.inner[1].b == '4'