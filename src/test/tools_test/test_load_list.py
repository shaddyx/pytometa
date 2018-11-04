import typing

from pytometa import tools, loader
from pytometa.descriptors import TypeDescriptor, ListDescriptor


class _B(object):
    l = ListDescriptor(int)  # type: typing.List[int]


class _A(object):
    a = TypeDescriptor(int)
    b = TypeDescriptor(str)


def test_load_list():

    res = loader.load_from_dict({
        "l":[
            1, 2, 3, 4
        ]
    }, _B())
    assert type(res.l) is list
    assert len(res.l) == 4






