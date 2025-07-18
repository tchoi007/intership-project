from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context):
    """
    :param context: Behave context
    """
    options = Options()
    options.add_argument("--headless")
    driver_path = GeckoDriverManager().install()
    #driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Firefox(service=service, options=options)
    #context.driver = webdriver.Chrome(service=service, options=options)

    #context.driver.maximize_window()
    context.driver.set_window_size(1920, 1080)
    context.driver.implicitly_wait(4)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)

def take_screenshot(context, name='screenshot'):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{name}_{timestamp}.png"
    context.driver.save_screenshot(filename)
    print(f"Screenshot saved as {filename}")

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        take_screenshot(context, name='failed_step')

def after_scenario(context, feature):
    context.driver.quit()
