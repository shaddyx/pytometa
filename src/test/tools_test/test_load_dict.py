import typing

from pytometa import tools, loader
from pytometa.descriptors import TypeDescriptor, ListDescriptor, DictDescriptor

class _A(object):
    a = TypeDescriptor(int)
    b = TypeDescriptor(str)

class _C(object):
    inner = DictDescriptor(TypeDescriptor(_A))  # type: typing.Dict[str, int]

class _D(object):
    inner = DictDescriptor(_A)  # type: typing.Dict


def test_load_dict_object():

    res = loader.load_from_dict({
        "inner":{
            "zz":{
                "a": 1,
                "b": 2,
            },
            "xx": {
                "a": 3,
                "b": 4,
            }
        }
    }, _C())
    assert type(res.inner) is dict
    assert len(res.inner) == 2
    assert res.inner["zz"].a == 1
    assert res.inner["zz"].b == "2"
    assert res.inner["xx"].a == 3
    assert res.inner["xx"].b == '4'


