from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import time
import allure
from allure_commons.types import AttachmentType



def browser_init(context):
    """
    :param context: Behave context
    """
    mobile_emulation = {"deviceName": "Nexus 5"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")

    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service, options=chrome_options)

    context.driver.implicitly_wait(4)

    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    # #context.driver.maximize_window()
    # context.driver.set_window_size(430, 932)
    # context.driver.implicitly_wait(4)


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

    with open(filename, "rb") as image_file:
        allure.attach(
            image_file.read(),
            name=name,
            attachment_type=AttachmentType.PNG
        )

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        take_screenshot(context, name='failed_step')

def after_scenario(context, feature):
    context.driver.quit()
