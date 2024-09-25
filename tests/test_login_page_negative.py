import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


class TestNegativeScenarios:
    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_username(self):
        #Open page
        driver = webdriver.Chrome()

        #go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        #Type username incorrectUser into Username field
        username_locator=driver.find_element(By.ID,"username")
        username_locator.send_keys("incorrectUser")
        #Type password Password123 into Password field
        password_locator=driver.find_element(By.NAME,"password")
        password_locator.send_keys("Password123")
        #Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        #Verify error message is displayed
        error_message=driver.find_element(By.ID,"error")

        assert error_message.is_displayed(), 'Error message is not displayed, but it should be'
        #Verify error message text is Your username is invalid!"""
        actual_error_text = error_message.text
        assert actual_error_text=="Your username is invalid!"

        driver.close()

    @pytest.mark.login
    @pytest.mark.negative
    def test_negative_password(self):
        #Open page
        driver = webdriver.Chrome()

        #go to webpage
        driver.get("https://practicetestautomation.com/practice-test-login/")

        #Type username student into Username field
        username_locator=driver.find_element(By.ID,"username")
        username_locator.send_keys("student")
        #Type password incorrectPassword into Password field
        password_locator=driver.find_element(By.NAME,"password")
        password_locator.send_keys("incorrectPassword")
        #Push Submit button
        submit_button_locator = driver.find_element(By.XPATH, "//button[@id='submit']")
        submit_button_locator.click()
        #Verify error message is displayed
        error_message=driver.find_element(By.ID,"error")
        assert error_message.is_displayed(), 'Error message is not displayed, but it should be'
        #Verify error message text is Your username is invalid!"""
        actual_error_text = error_message.text
        assert actual_error_text=="Your password is invalid!"
        driver.close()