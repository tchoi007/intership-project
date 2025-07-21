from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.options import Options as EdgeOptions



def browser_init(context):
    """
    :param context: Behave context
    """


    username = 'tomas_1aqxVc'
    access_key = 'THbkesv3A4a47JA2HpxE'
    browserstack_url = f"https://{username}:{access_key}@hub-cloud.browserstack.com/wd/hub"

    options = EdgeOptions()

    # Set browser name and version at top level
    options.set_capability("browserName", "Edge")
    options.set_capability("browserVersion", "latest")

    # BrowserStack options inside 'bstack:options'
    options.set_capability("bstack:options", {
        "os": "Windows",
        "osVersion": "11",
        "sessionName": context.scenario.name if hasattr(context, 'scenario') else 'BDD Edge Test',
        "debug": True,
        "networkLogs": True,
        "consoleLogs": "info"
    })

    context.driver = webdriver.Remote(
        command_executor=browserstack_url,
        options=options
    )

    #options = Options()
    #options.add_argument("--headless")
    #driver_path = GeckoDriverManager().install()
    #driver_path = ChromeDriverManager().install()
    #service = Service(driver_path)
    #context.driver = webdriver.Firefox(service=service, options=options)
    #context.driver = webdriver.Chrome(service=service, options=options)

    #context.driver.maximize_window()

    print(f"BrowserStack session started with ID: {context.driver.session_id}")


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
