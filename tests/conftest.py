import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

driver = None

def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):

    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path='../source/chromedriver.exe')
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path='../source/geckodriver.exe')
    elif browser_name == "headless":
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--window-size=1920x1080')
        driver = os.getcwd() + '/chromedriver.exe'
        driver = webdriver.Chrome(options = options, executable_path='../source/chromedriver.exe')
    elif browser_name == "remote":
        capabilities = {
            "browserName": "chrome",
            "browserVersion": "89.0",
            "selenoid:options": {"enableVNC": True, "enableVideo": False}
        }
        driver = webdriver.Remote(command_executor="http://136.243.89.21:4445//wd/hub",
                                  desired_capabilities=capabilities)

    driver.get('http://automationpractice.com/')
    driver.implicitly_time = 30
    driver.implicitly_wait(driver.implicitly_time)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(f'../HTMLReports/{name}')
    # allure.attach(driver.get_screenshot_as_png(), name=f'error-screenshot+{name}', attachment_type=AttachmentType.PNG)