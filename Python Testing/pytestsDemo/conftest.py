import pytest



@pytest.fixture(scope="class")
def setup():
    print("I will be executing first")
    yield
    print("I will executed lasts")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return["Rahul","shetty","rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","rahul","shetty"),("firefox","play"),("IE","ss")])
def crossBrowser(request):
    return request.param