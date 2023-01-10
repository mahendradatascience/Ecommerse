import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome(executable_path="E:\\Software_Testing\\software\\chromedriver.exe")
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox(executable_path="E:\\Software_Testing\\software\\chromedriver.exe")
        print("Launching firefox browser.........")
    return driver

def pytest_addoption(parser): # This will get the value(browser) from CLI(command line) /hooks
    parser.addoption("--browser") #and whatever browser we passing it get that browser

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### pytest HTML Report ################

# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Pavan'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None) # JAVA_HOME, Plugins by defaault display in report 
    metadata.pop("Plugins", None) # so these details no need so used metadata.pop
