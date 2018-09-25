from pytometa import tools
from pytometa.descriptors import TypeDescriptor

def load_from_dict(dict, obj, raise_on_receiver_absent=False):
    assert obj, "object is empty"
    fields = tools.getAllFieldItems(obj.__class__)
    for k in fields:
        pass
