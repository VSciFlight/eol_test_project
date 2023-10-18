import pytest

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser")

@pytest.fixture
def get_browser(request):
    return request.config.getoption("--browser")
