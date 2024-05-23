import pytest
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        print("Test run in Chrome browser")
        driver = webdriver.Chrome()

    elif browser == 'firefox':
        print("Test run in Firefox browser")
        driver = webdriver.Firefox()

    elif browser == 'edge':
        print("Test run in Edge browser")
        driver = webdriver.Edge()

    else:
        driver = webdriver.Chrome(options=chrome_options)
        print("Test run in Headless browser")
    driver.maximize_window()
    url = "https://admin-demo.nopcommerce.com/"
    driver.get(url)
    yield driver
    driver.quit()


@pytest.fixture(params=[
    ("admin@yourstore.com", "admin", "Pass"),
    ("admin@yourstore.com1", "admin", "Fail"),
    ("admin@yourstore.com", "admin1", "Fail"),
    ("admin@yourstore.com1", "admin1", "Fail")
])
def DataForLogin(request):
    return request.param

## pytest -v -s -n=1 --html=HtmlReports/report.html --browser chrome
## pytest -v -s -n=3 --html=HtmlReports/report.html --browser firefox
## pytest -v -s -n=2 --html=HtmlReports/report.html --browser edge


# @pytest.fixture
# def setup():
#     driver = webdriver.Chrome()
#     url = "https://admin-demo.nopcommerce.com/"
#     driver.get(url)
#     driver.maximize_window()
#     driver.implicitly_wait(10)
#     return driver
