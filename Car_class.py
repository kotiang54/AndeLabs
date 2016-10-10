# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:13:55 2016

@author: skotiang
"""

class Car(object):
    """This class object takes in arguments that depict the type, model, and name of the vehicle, ...
    provided they are set."""

    def __init__(self, *args):  # initialize the class with empty arguments

        if len(args) == 0:
            self.name = "General"  # The car should be called `General` if no name was passed as an argument
            self.model = "GM"   # The car's model should be called `GM` if no model was passed as an argument

        if len(args) >= 1:
            self.name = args[0]
            self.model = args[1]
            self.car_type = args[2]

        if self.name is "Koenigsegg" or  self.name is "Porshe": 
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4  # The car shoud have four (4) doors except its a Porshe or Koenigsegg

        if self.car_type == "trailer":
            self.num_of_wheels = 8
        else:
            self.car_type = "saloon"   # The car type should be saloon if it is not a trailer
            self.num_of_wheels = 4   # The car shoud have four (4) wheels except its a type of trailer

        self.speed = 0

    def is_saloon(self):
        return self.car_type is 'saloon'
        

    def drive(self, knots):
        if self.car_type is 'trailer':
            self.speed = knots * 11     # calculates the speed of the trailer while on move
        else:
            self.speed = 10**knots

        return self