#!/usr/bin/python

class Duck(object):
    def __init__(self, string):
        print('do something ' + string)


    def quack(self):
        print('Quaaaaaaack!')


    def feathers(self):
        print('The duck has white and gray feathers.')


class Person(object):
    def quack(self):
        print('The person imitates a duck.')


    def feathers(self):
        print('The person takes a feather from the ground and shows it.')


def in_the_forest(object):
    object.quack()
    object.feathers()


def game():
    donald = Duck('duck')
    john = Person()
    in_the_forest(donald)
    in_the_forest(john)


if __name__ == "__main__":
    game()
