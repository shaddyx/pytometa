def getAllFields(cls):
    items = cls.__dict__.items()
    return [k[0] for k in items]

def getAllFieldItems(cls):
    items = cls.__dict__.items()
    return [(k[0], k[1]) for k in items]