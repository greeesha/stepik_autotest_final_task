import pages.login_page
import pages.main_page

def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = pages.login_page.LoginPage(browser, link)
    page.open()
    #page.should_be_login_page()
    page.should_be_login_url()

def test_guest_should_see_login_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = pages.login_page.LoginPage(browser, link)
    page.open()
    #page.should_be_login_page()
    page.should_be_login_form()

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = pages.main_page.MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = pages.login_page.LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()