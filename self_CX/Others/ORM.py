#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = "panda  84305510@qq.com"

from peewee import *

BATABASE = MySQLDatabase('pandatest', user='root', password='panda2013', host='localhost', port=3306)


class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = BATABASE


# Person.create_table()
# p=Person(name='panda',birthday=('1993,05,28'),is_relative=True)
# p.save()
w = Person.get(Person.name == 'panda')
print(w.name)
print(w.is_relative)
