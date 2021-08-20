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


from ddt import data
from ddt import ddt
from ddt import unpack
from Task3 import get_ranges
import unittest


@ddt
class GetRangesTestCase(unittest.TestCase):
    @data(
        (get_ranges([0, 1, 2, 3, 4, 7, 8, 10]), "0-4, 7-8, 10"),
        (get_ranges([4, 7, 10]), "4, 7, 10"),
        (get_ranges([2, 3, 8, 9]), "2-3, 8-9"),
    )
    @unpack
    def test_main(self, input_name, output):
        self.assertEqual(input_name, output)

    def test_string(self):
        with self.assertRaises(TypeError):
            get_ranges('1, 2, 3')

    def test_int(self):
        with self.assertRaises(TypeError):
            get_ranges(1)

    def test_set(self):
        with self.assertRaises(TypeError):
            get_ranges({1, 2, 3})

    def test_empty_list(self):
        with self.assertRaises(IndexError):
            get_ranges([])


if __name__ == '__main__':
    unittest.main()
