import pages.login_page

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

def test_guest_should_see_reg_form(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = pages.login_page.LoginPage(browser, link)
    page.open()
    #page.should_be_login_page()
    page.should_be_register_form()