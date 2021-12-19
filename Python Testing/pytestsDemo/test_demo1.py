# Any pytest file should start with test_ or end with _test
# pytest method names should start with test
# any code should be wrapped in method only
# if wants to run code from command prompt then first give path then py.test -v -s, -v stands for information in code -s stands for printing code in command prompt
# methods name should have sense because to find test cases its name is important
# you can run specific file with py.test <filename>
# -k stands for specific method to run ,-m stands for mark or tag method to get run ex-@pytest.mark.smoke
# you can skip tests with @pytest.mark.skip
# fixture are used as setup and tear down methods for test cases - conftest file to generalize fixture and make it
# available to all test cases
# datadriven and parametrization can be done with return statements in tuple format
# when you define fixture scope to class only ,it will run once before class is initiated and at the end

import pytest


@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_Greetcreditcard():
    print("good morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[0])