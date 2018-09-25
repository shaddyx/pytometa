from pytometa import tools
from pytometa.descriptors import TypeDescriptor


def load_field(obj, dic, meta: TypeDescriptor):
    setattr(obj, meta.name, dic[meta.name])

def load_from_dict(dic, obj):
    assert obj, "object is empty"
    fields = tools.getAllFieldItems(obj.__class__)
    for k in fields:
        meta = k[1]
        name = k[0]
        if isinstance(meta, TypeDescriptor):
            if not meta.name:
                meta.name = name
            load_field(obj, dic, meta)
    return obj
