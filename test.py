from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import unittest


class WebAppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Set up Chrome options for headless mode
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        # Specify the path to your ChromeDriver executable
        chrome_driver_path = "C:\\browserdrivers\\chromedriver.exe"

        # Initialize WebDriver instance and store it as a class attribute
        cls.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=chrome_options)

        # Note: Ensure that the URL includes the protocol (http/https)
        cls.base_url = "http://localhost/Car_Rental-PHP"

    @classmethod
    def tearDownClass(cls):
        # Close the browser after all tests are done
        cls.driver.quit()

    def setUp(self):
        # Additional setup tasks for each test case (if any)
        pass

    
    def test_login_successful(self):
        # Perform login with valid credentials
        self.driver.get(self.base_url + "/login.php")
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        submit_button = self.driver.find_element_by_css_selector("input[type='submit']")

        username_input.send_keys("admin")
        password_input.send_keys("admin")
        submit_button.click()

        # Verify redirection to the dashboard
        self.assertEqual(self.driver.current_url, "http://localhost/Car_Rental-PHP/dashboard.php")

    def test_login_failed(self):
        self.driver.get(self.base_url + "/login.php")        # Perform login with invalid credentials
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")
        submit_button = self.driver.find_element_by_css_selector("input[type='submit']")

        username_input.send_keys("invalid_username")
        password_input.send_keys("invalid_password")
        submit_button.click()

        # Check if the error message is displayed
        error_message = self.driver.find_element_by_css_selector("p[style='color: red;']").text
        self.assertEqual(error_message, "Invalid username or password. Please try again.")

    def test_empty_login_fields(self):
        self.driver.get(self.base_url + "/login.php")  # Navigate to the login page
        submit_button = self.driver.find_element_by_css_selector("input[type='submit']")
        submit_button.click()

        # Check for the presence of the browser's native validation messages
        username_input = self.driver.find_element_by_name("username")
        password_input = self.driver.find_element_by_name("password")

        # Check for the 'required' attribute in the username and password inputs
        self.assertTrue(username_input.get_attribute("required"))
        self.assertTrue(password_input.get_attribute("required"))


def test_employee_login(self):
        self.driver.get("http://localhost/Car_Rental-PHP/clientlogin.php")

        # Find username and password fields and login button, and perform login
        username_field = self.driver.find_element_by_name("txtuname")
        password_field = self.driver.find_element_by_name("txtpassword")
        login_button = self.driver.find_element_by_name("btnlogin")

        username_field.send_keys("employee_username")  # Replace with the employee's username
        password_field.send_keys("employee_password")  # Replace with the employee's password
        login_button.click()

        # Add assertions or validation steps based on the behavior after login
        # For example, check for successful login by verifying elements on the dashboard page

        # Example validation: Check if the dashboard page title is as expected
        assert "Employee Dashboard" in self.driver.title


if __name__ == "__main__":
    unittest.main()

