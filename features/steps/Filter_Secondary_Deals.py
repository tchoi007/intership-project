from behave import given, when, then
from pages.Login_page import LoginPage
from pages.Main_page import MainPage
from pages.secondary_page import SecondaryPage

@given('Open the main page')
def step_open_main_page(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.open()

@when('Log in to the page')
def step_login(context):
    context.login_page.login('kpenvy@gmail.com', 'Tc642531$$$')
    context.main_page = MainPage(context.driver)
    # context.main_page.verify_page_loaded()

@when('Click on off plan')
def step_click_off_plan(context):
    context.main_page.click_off_plan()


@when('Click on the Secondary option')
def step_click_secondary(context):
    context.main_page.click_secondary_option()
    context.secondary_page = SecondaryPage(context.driver)

@when('Verify the right page opens')
def step_verify_page(context):
    context.secondary_page.verify_page_loaded()

@when('Click on filters')
def step_click_filters(context):
    context.secondary_page.click_filters()

@when('Filter the products by "want to sell"')
def step_filter_want_to_sell(context):
    context.secondary_page.apply_filter('want to sell')

@when('click on apply filter')
def step_apply_filter(context):
    context.secondary_page.click_apply_filter()

@then('Verify all cards have for sale tag')
def step_verify_for_sale_tag(context):
    assert context.secondary_page.all_cards_have_tag('For sale')
