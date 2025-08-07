import pytest
import allure
from pages.login_page import LoginPage
 
@allure.feature("Momo 登入流程")
@allure.title("成功登入後應顯示『客戶登出』狀態")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_should_show_logout(driver):
    login = LoginPage(driver)

    with allure.step("開啟首頁"):
        login.open()

    with allure.step("點擊登入按鈕"):
        login.click_login_icon()

    with allure.step("切換至登入 iframe 並輸入帳密"):
        login.switch_to_login_frame()
        login.input_credentials("testid456", "testpwd456")
        login.submit_login()

    with allure.step("驗證登入成功，畫面出現『客戶登出』"):
        assert login.is_logged_in(), "登入後未出現『客戶登出』按鈕"