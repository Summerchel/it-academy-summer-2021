"""Оформите указанную задачу из прошлых домашних в виде функции и покройте
тестами. Учтите, что в функцию могут быть переданы некорректные значения,
здесь может пригодится ‘assertRaises’.
Не нужно переделывать функцию для того чтобы она ловила все возможные
ситуации сама.

ДЗ 5 задача 3

Реализовать функцию get_ranges которая получает на вход непустой список
неповторяющихся целых чисел, отсортированных по возрастанию, которая этот
список “сворачивает”
 get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) // "0-4,7-8,10"
 get_ranges([4,7,10]) // "4,7,10"
 get_ranges([2, 3, 8, 9]) // "2-3,8-9"""

import unittest
from Task3 import get_ranges


class TestGetRanges(unittest.TestCase):

    def test_area(self):
        self.assertEqual(get_ranges([0, 1, 2, 3, 4, 7, 8, 10]), "0-4, 7-8, 10")
        self.assertEqual(get_ranges([4, 7, 10]), "4, 7, 10")
        self.assertEqual(get_ranges([2, 3, 8, 9]), "2-3, 8-9")

    def test_type(self):
        with self.assertRaises(TypeError):
            get_ranges('1, 2, 3')
        with self.assertRaises(TypeError):
            get_ranges(1)
        with self.assertRaises(TypeError):
            get_ranges({1, 2, 3})

    def test_index(self):
        with self.assertRaises(IndexError):
            get_ranges([])

    def test_value(self):
        with self.assertRaises(ValueError):
            get_ranges([0, 3, 2, 4, 7, 8, 10])
        with self.assertRaises(ValueError):
            get_ranges([0, 2, 2])
