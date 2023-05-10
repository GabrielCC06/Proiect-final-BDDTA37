from browser import Browser
from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.forgot_password_page = ForgotPasswordPage()

def after_all(context):
    context.browser.close()
    