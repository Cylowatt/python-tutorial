from dataclasses import dataclass

import typing


class Bike:
    ''' Represents a bike '''

    # Class attribute.
    num_passengers = 1

    # Constructor.
    def __init__(self, wheel_size, gear_ratio):
        ''' Createa bike specifying the
        wheel size, and gear ratio'''

        # Instance attributes.
        self.size = wheel_size
        self.ratio = gear_ratio

    def geat_inches(self):
        return self.ratio * self.size


# Subclass.
class Tandem(Bike):
    # Override class attribute.
    num_passengers = 2

    def __init__(self, wheel_size, rings, cogs):
        self.rings = rings
        self.cogs = cogs
        ratio = rings[0] / cogs[0]

        # Call the superclass constructor.
        super().__init__(wheel_size, ratio)

    def shift(self, ring_idx, cog_idx):
        # Use \ for multiline splits of long statements.
        self.ratio = self.rings[ring_idx] \
                     / self.cogs[cog_idx]


INCHES_PER_METER = 39.37


# Class methods.
class MountainBike(Bike):

    # Allows to create alternate constructors.
    @classmethod
    def from_metric(cls, size_meters, ratio):
        return cls(size_meters * INCHES_PER_METER, ratio)


# Static methods.
class Recumbent(Bike):
    @staticmethod
    def is_fast():
        return True


# Properties. Same as in C# or getters and setters in TypeScript.
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        if self._name == 'Richard':
            return 'Ringo'
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name


# Data classes (Python 3.7). Describe the attributes of a class using annotations.
@dataclass
class Bike2:
    num_passengers: typing.ClassVar[int]
    wheel_size: float
    gear_ratio: float

    def gear_inches(self):
        return self.gear_ratio * self.wheel_size
