from pytometa import tools, loader
from pytometa.descriptors import TypeDescriptor


class _A(object):
    a = TypeDescriptor(int)
    b = TypeDescriptor(str)

    def __str__(self):
        fields = ["{}={}".format(k[0], k[1]) for k in tools.getAllFieldItems(self)]
        return "_A[{}]".format(", ".join(fields))


def test_load():
    res = loader.load_from_dict({
        "a": 1,
        "b": "123123123",
        "c": {}
    }, _A())

    print(res)



