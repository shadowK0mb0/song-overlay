class InMemoryCache:
    __slots__ = ['__cache']

    def __init__(self):
        self.__cache = dict()

    def get(self, key):
        return self.__cache.get(key)

    def set(self, key, value):
        self.__cache[key] = value

    def delete(self, key):
        if key in self.__cache:
            del self.__cache[key]