""" this is a module for lab 4 """
from abc import abstractclassmethod


class Musician:
    """
    super class for musicians that takes name attribute
    and contains the methods to be used by sub-classess
    """

    def __init__(self, name):

        self.name = name

    def __str__(self):
        return "My name is {} and I play {}".format(self.name, self.instrument)

    def __repr__(self):
        return f"{self.__class__.__name__} instance. Name = {self.name}"

    def get_instrument(self):
        return f"{self.instrument}"

    def play_solo(self):
        return f"{self.solo}"


class Guitarist(Musician):
    """
    sub class (child) of Musician that contains methods for Guitarist
    """

    def __init__(self, name):

        super().__init__(name)
        self.instrument = "guitar"
        self.solo = "face melting guitar solo"


class Drummer(Musician):
    """
    sub class (child) of Musician that contains methods for Drummer
    """

    def __init__(self, name):
        super().__init__(name)
        self.instrument = "drums"
        self.solo = "rattle boom crash"


class Bassist(Musician):
    """
    sub class (child) of Musician that contains methods for Bassist
    """

    def __init__(self, name):
        super().__init__(name)
        self.instrument = "bass"
        self.solo = "bom bom buh bom"


class Band:
    """
    a class to create a group of musicians with the name of their band
    """

    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self.name)

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        """
        a class to pass
        """
        return cls.instances
