from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
 
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.momoshop.com.tw/main/Main.jsp"

    def open(self):
        self.driver.get(self.url)

    def click_login_icon(self):
        login_icon = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="LOGINSTATUS" and @title="客戶登入"]'))
        )
        login_icon.click()

    def switch_to_login_frame(self):
        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[16]/div[1]/iframe'))
        )
        self.driver.switch_to.frame(iframe)

    def input_credentials(self, username, password):
        user_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div/div/div[1]/form/dl/dd[1]/li/input'))
        )
        pwd_input = self.driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[1]/form/dl/dd[2]/li/input')
        user_input.send_keys(username)
        pwd_input.send_keys(password)

    def submit_login(self):
        login_btn = self.driver.find_element(By.XPATH, '//*[@id="login"]/div/div/div[1]/form/dl/dl/dd[1]/a')
        login_btn.click()
        self.driver.switch_to.default_content()

    def is_logged_in(self):
        chk = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="LOGINSTATUS" and @title="客戶登出"]'))
        )
        return chk.is_displayed()