#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed = 'Mutt'):
        self.name = name
        self.breed = breed

    def bark(self):
        print('Woof!')

    def show_self(self):
        return self
    
    def get_adopted(self, owner_name):
        self.owner = owner_name


snoopy = Dog('Snoopy', 'Beagle')
snoopy.bark()

print(snoopy is snoopy.show_self())

print(snoopy.name)

snoopy.owner = 'Charlie Brown'

print(snoopy.owner)

snoopy.get_adopted('Linus')

print(snoopy.owner)

print(snoopy.breed)

