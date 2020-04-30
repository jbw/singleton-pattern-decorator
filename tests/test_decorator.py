import unittest

from singleton_decorator_pattern.decorator import singleton


@singleton
class SingletonDecoratedClass:
    def __init__(self):
        pass


class TestSingletonDecorator(unittest.TestCase):
    def setUp(self):
        self.singleton_instance_a = SingletonDecoratedClass()
        self.singleton_instance_b = SingletonDecoratedClass()

    def test_instances_are_the_same(self):

        self.assertEqual(self.singleton_instance_a, self.singleton_instance_b)

    def test_both_instances_are_the_same(self):

        self.assertEqual(
            SingletonDecoratedClass.instance, SingletonDecoratedClass.instance
        )

    def test_both_instances_are_not_none(self):
        self.assertIsNotNone(self.singleton_instance_a)
        self.assertIsNotNone(self.singleton_instance_b)

    def test_inner_wrapper_is_accessible(self):

        self.assertEqual(
            self.singleton_instance_a.__class__, SingletonDecoratedClass.wrapper
        )
