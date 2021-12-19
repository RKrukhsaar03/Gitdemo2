# fixture when something need to be printed first yield will connect but will print in last
import pytest


@pytest.mark.userfixture("setup")
class TestExample:
    def test_fixtureDemo(self):
        print("I will execute steps in fixtureDemo method")

    def test_fixtureDemo1(self):
        print("I will execute steps in fixtureDemo1 method")

    def test_fixtureDemo2(self):
        print("I will execute steps in fixtureDemo2 method")

    def test_fixtureDemo3(self):
        print("I will execute steps in fixtureDemo3 method")
