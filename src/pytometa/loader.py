from descriptors import TypeDescriptor


def load_from_dict(dict, type_descriptor: TypeDescriptor, raise_on_receiver_absent=False):
    for k in type_descriptor:

