class LikeString:
    def __init__(self, internalStr=""):
        self.iStr = internalStr

    def __eq__(self, other):
        return other.lower() in self.iStr.lower()

    def __str__(self):
        return self.iStr

    def __repr__(self):
        return "ls'" + self.iStr + "'"


class LikeDict:
    def __init__(self):
        self.__keys = []
        self.__values = []

    def keys(self):
        return self.__keys

    def values(self):
        return self.__values

    def items(self):
        return [[self.__keys[x], self.__values[x]] for x in range(len(self.__keys))]

    def __getitem__(self, key):
        for x, elem in enumerate(self.__keys):
            if key == elem:
                return self.__values[x]
        raise KeyError(key)

    def __setitem__(self, key, value):
        for x, elem in enumerate(self.__keys):
            if key == elem:
                self.__values[x] = value
                return
        key = LikeString(key)
        self.__keys.append(key)
        self.__values.append(value)

    def __str__(self):
        if len(self.__keys):
            ans = "ld{ "
            for x, elem in enumerate(self.__keys):
                ans += repr(elem) + " : " + repr(self.__values[x]) + (", " if x != len(self.__keys) - 1 else "")
            return ans + " }"
        return "{}"
    __repr__ = __str__


class Component:
    def __init__(self, name="undefined name", descr="", img="http://leeford.in/wp-content/uploads/2017/09/image-not-found.jpg"):
        self.name = name
        self.descr = descr
        self.img = img


class Actor(Component):
    def __init__(self, name="undefined name", descr="", img="http://leeford.in/wp-content/uploads/2017/09/image-not-found.jpg"):
        Component.__init__(self, name, descr, img)

    def __str__(self):
        return "<Actor>(" + self.name + ")"

    __repr__ = __str__


class Character(Component):
    def __init__(self, name="undefined name", descr="", actor=Actor()):
        Component.__init__(self, name, descr)
        self.actor = actor

    def __str__(self):
        return "<Character>(" + self.name + ")"

    __repr__ = __str__


class Movie(Component):
    def __init__(self, name="undefined name", descr="", img="http://leeford.in/wp-content/uploads/2017/09/image-not-found.jpg", characters=[]):
        Component.__init__(self, name, descr, img)
        self.characters = characters

    def __str__(self):
        return "<Movie>(" + self.name + ")"

    __repr__ = __str__
