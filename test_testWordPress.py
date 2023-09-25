# PlugIn Test For the WordPress for WPPool

import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium import webdriver

class YourTestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\path\to\chromedriver.exe')


class TestTestWordPress():
  
 
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testWordPress(self):

    # Test name: Test_WordPress
    # Step # | name | target | value
    # 1 | open | /myWordPress/wp-login.php | 

    self.driver.get("http://localhost/myWordPress/wp-login.php")

    # 2 | type | id=user_login | test
    self.driver.find_element(By.ID, "user_login").send_keys("test")

    # 3 | type | id=user_pass | Test@1122
    self.driver.find_element(By.ID, "user_pass").send_keys("Test@1122")

    # 4 | click | css=.forgetmenot | 
    self.driver.find_element(By.CSS_SELECTOR, ".forgetmenot").click()

    # 5 | click | id=loginform | 
    self.driver.find_element(By.ID, "loginform").click()

    # 6 | click | id=rememberme | 
    self.driver.find_element(By.ID, "rememberme").click()

    # 7 | click | id=wp-submit | 
    self.driver.find_element(By.ID, "wp-submit").click()

    # 8 | click | linkText=Installed Plugins | 
    self.driver.find_element(By.LINK_TEXT, "Installed Plugins").click()
    
    # 9 | click | id=activate-wp-dark-mode | 
    self.driver.find_element(By.ID, "activate-wp-dark-mode").click()

    # 10 | click | css=#wp_dark_mode_general-tab > span | 
    self.driver.find_element(By.CSS_SELECTOR, "#wp_dark_mode_general-tab > span").click()

    # 11 | click | css=.enable_backend .wp-dark-mode-ignore | 
    self.driver.find_element(By.CSS_SELECTOR, ".enable_backend .wp-dark-mode-ignore").click()

    # 12 | click | css=.enable_backend .wp-dark-mode-ignore | 
    self.driver.find_element(By.CSS_SELECTOR, ".enable_backend .wp-dark-mode-ignore").click()

    # 13 | click | id=save_settings | 
    self.driver.find_element(By.ID, "save_settings").click()

    # 14 | click | css=.modes:nth-child(2) > .light | 
    self.driver.find_element(By.CSS_SELECTOR, ".modes:nth-child(2) > .light").click()

    # 15 | click | css=.modes:nth-child(2) > .dark | 
    self.driver.find_element(By.CSS_SELECTOR, ".modes:nth-child(2) > .dark").click()

    # 16 | click | css=#wp_dark_mode_switch-tab > span | 
    self.driver.find_element(By.CSS_SELECTOR, "#wp_dark_mode_switch-tab > span").click()
    
    # 17 | click | css=.switch_style .image-choose-opt:nth-child(3) > .image-choose-img | 
    self.driver.find_element(By.CSS_SELECTOR, ".switch_style .image-choose-opt:nth-child(3) > .image-choose-img").click()
    
    # 18 | click | css=#wp_dark_mode_switch #save_settings | 
    self.driver.find_element(By.CSS_SELECTOR, "#wp_dark_mode_switch #save_settings").click()

    # 19 | click | css=span:nth-child(7) | 
    self.driver.find_element(By.CSS_SELECTOR, "span:nth-child(7)").click()

    # 20| Save | The setting all 
    # 21 | click | css=.switcher_scale > td | 
    self.driver.find_element(By.CSS_SELECTOR, ".switcher_scale > td").click()

    # 22 | click | css=.switcher_scale .description:nth-child(3) | 
    self.driver.find_element(By.CSS_SELECTOR, ".switcher_scale .description:nth-child(3)").click()

    # 23 | mouseDownAt | css=.ui-state-hover | 29.54998779296875,21
    element = self.driver.find_element(By.CSS_SELECTOR, ".ui-state-hover")

    actions = ActionChains(self.driver)
    actions.move_to_element(element).click_and_hold().perform()

    # 24 | mouseMoveAt | css=.ui-state-hover | 29.54998779296875,21
    element = self.driver.find_element(By.CSS_SELECTOR, ".ui-state-hover")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()

    # 25 | mouseUpAt | css=.ui-state-hover | 29.54998779296875,21
    element = self.driver.find_element(By.CSS_SELECTOR, ".ui-state-hover")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).release().perform()

    # 26 | click | css=.ui-state-hover | 
    self.driver.find_element(By.CSS_SELECTOR, ".ui-state-hover").click()

    # 27 | click | css=#wp_dark_mode_switch #save_settings | 
    self.driver.find_element(By.CSS_SELECTOR, "#wp_dark_mode_switch #save_settings").click()

    # 28 | click | css=td > .description:nth-child(4) | 
    self.driver.find_element(By.CSS_SELECTOR, "td > .description:nth-child(4)").click()

    # 29 | click | id=wp_dark_mode_switch[switcher_position] | 
    self.driver.find_element(By.ID, "wp_dark_mode_switch[switcher_position]").click()

    # 30 | select | id=wp_dark_mode_switch[switcher_position] | label=Left Bottom
    dropdown = self.driver.find_element(By.ID, "wp_dark_mode_switch[switcher_position]")
    dropdown.find_element(By.XPATH, "//option[. = 'Left Bottom']").click()

    # 31 | click | css=#wp_dark_mode_switch #save_settings | 
    self.driver.find_element(By.CSS_SELECTOR, "#wp_dark_mode_switch #save_settings").click()

    # 32 | click | css=#wp_dark_mode_accessibility-tab > span | 
    self.driver.find_element(By.CSS_SELECTOR, "#wp_dark_mode_accessibility-tab > span").click()

    # 33 | click | css=.font_size_toggle .wp-dark-mode-ignore | 
    self.driver.find_element(By.CSS_SELECTOR, ".font_size_toggle .wp-dark-mode-ignore").click()

    # 34 | click | css=.close-promo | 
    self.driver.find_element(By.CSS_SELECTOR, ".close-promo").click()

    # 35 | click | css=.keyboard_shortcut .wp-dark-mode-ignore | 
    self.driver.find_element(By.CSS_SELECTOR, ".keyboard_shortcut .wp-dark-mode-ignore").click()

    # 36 | click | css=#wp_dark_mode_accessibility #save_settings | 
    self.driver.find_element(By.CSS_SELECTOR, "#wp_dark_mode_accessibility #save_settings").click()

    # 37 | click | linkText=Visit Site | 
    self.driver.find_element(By.LINK_TEXT, "Visit Site").click()

    # 38 | click | css=.sun-light | 
    self.driver.find_element(By.CSS_SELECTOR, ".sun-light").click()

    # 39 | click | css=.moon-light | 
    self.driver.find_element(By.CSS_SELECTOR, ".moon-light").click()

    # 40 | click | css=.sun-light | 
    self.driver.find_element(By.CSS_SELECTOR, ".sun-light").click()

    # 41 | click | css=.moon-light | 
    self.driver.find_element(By.CSS_SELECTOR, ".moon-light").click()
 
# Your test functions and setup code here

if __name__ == "__main__":
    pytest.main()
