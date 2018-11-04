import abc
import logging

from pytometa import loader


class FieldDescriptor(object):
    def __init__(self, name=None, required=True, default=None):
        self.name = name
        self.required = required
        self.default = default

    def _get_value(self, dic):
        assert not self.required or self.name in dic, "field {} is mandatory, given: {}".format(self.name, dic)

        if not self.required and self.name not in dic:
            return self.default

        return dic[self.name]


    @abc.abstractmethod
    def load_function(self, dic):
        raise Exception("Not implemented")

class TypeDescriptor(FieldDescriptor):

    def __init__(self, typ, name=None, required=True, default=None):
        self.type = typ
        super().__init__(name, required, default)

    def load_function(self, dic):
        logging.info("loading: {}".format(self.name))
        return self.type(self._get_value(dic))


class ListDescriptor(FieldDescriptor):

    def __init__(self, typ, name=None, required=True, default=None):
        self.type = typ
        super().__init__(name, required, default)

    def load_function(self, dic):
        assert type(self._get_value(dic)) is list, "list expected, but {} given [{}]: {} ".format(type(self.__get_value(dic)), self.name, self.__get_value(dic))
        result = []
        for k in self._get_value(dic):
            result.append(loader.load_from_dict(k, self.type))
        return result