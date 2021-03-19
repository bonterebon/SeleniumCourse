import pytest
from selenium import webdriver
    
    
@pytest.fixture(scope="session")
def chrome_driver():
    print("initiating chrome driver")

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()