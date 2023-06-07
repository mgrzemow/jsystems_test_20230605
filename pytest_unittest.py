import pytest
import unittest


class Test1():
    @classmethod
    def setup_class(cls):
        """setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        print('\nsetup_class\n')

    @classmethod
    def teardown_class(cls):
        """teardown any state that was previously setup with a call to
        setup_class.
        """
        print('\nteardown_class\n')

    def setup_method(self, method):
        """setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        print(f'\nsetup_method test {method}\n')

    def teardown_method(self, method):
        """teardown any state that was previously setup with a call to
        setup_class.
        """
        print(f'\nteardown_method test {method}\n')

    def test1(self):
        print('\ntest1\n')
        assert 1 == 1

    def test2(self):
        print('\ntest2\n')
        assert 1 == 1
