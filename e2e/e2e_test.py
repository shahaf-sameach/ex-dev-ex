from selenium import webdriver
import unittest

# TODO should selenium be added to the requirements file?
from selenium.webdriver import DesiredCapabilities


class CalculatorE2E(unittest.TestCase):

    def setUp(self):

        # self._driver = webdriver.Remote("http://selenium:4444/wd/hub", DesiredCapabilities.FIREFOX)
        self._driver = webdriver.Firefox(executable_path='./geckodriver')
        self._url = "http://localhost:8080/signup"

    def test_basic_operations(self):
        """
        Tests the all the basic calculator's functions.
        """
        self._driver.get(self._url)
        self._driver.maximize_window()
        self.assertIn("Node Authentication", self._driver.title)

        self._signup()

        # Check addition.
        self._check_addition()
        self._driver.refresh()

        # Check subtraction.
        self._check_subtraction()
        self._driver.refresh()

        # Check multiplication.
        self._check_multiplication()
        self._driver.refresh()

        # Check division.
        self._check_division()

    def test_continuous_operations(self):
        """
        Tests a few basic functions in a row.
        """
        self._driver.get(self._url)
        self._driver.maximize_window()
        self.assertIn("Node Authentication", self._driver.title)

        self._signup()

        # Enter 12 + 43
        digit_1 = self._driver.find_element_by_class_name("digit-1")
        digit_1.click()
        digit_2 = self._driver.find_element_by_class_name("digit-2")
        digit_2.click()
        plus_operator = self._driver.find_element_by_class_name("operator-plus")
        plus_operator.click()
        digit_4 = self._driver.find_element_by_class_name("digit-4")
        digit_4.click()
        digit_3 = self._driver.find_element_by_class_name("digit-3")
        digit_3.click()
        equals_operator = self._driver.find_element_by_class_name("operator-equals")
        equals_operator.click()

        # Check that the display shows 55.
        display = self._driver.find_element_by_class_name("display")
        self.assertEqual("55", display.text)

        # Enter +1
        plus_operator = self._driver.find_element_by_class_name("operator-plus")
        plus_operator.click()
        digit_1.click()
        equals_operator.click()

        # Check that the display shows 56.
        display = self._driver.find_element_by_class_name("display")
        self.assertEqual("56", display.text)

        digit_5 = self._driver.find_element_by_class_name("digit-5")
        digit_5.click()

        # Check that the display shows 5.
        display = self._driver.find_element_by_class_name("display")
        self.assertEqual("5", display.text)

    def _signup(self):
        """
        Performs signup into the site..
        """
        # Fill the email field.
        email = self._driver.find_element_by_name("email")
        email.clear()
        email.send_keys("test123@mail.com")

        # Fill the name field.
        name = self._driver.find_element_by_name("name")
        name.clear()
        name.send_keys("test1")

        # Fill the password field.
        password = self._driver.find_element_by_name("password")
        password.clear()
        password.send_keys("test1")

        # Confirm signup.
        button = self._driver.find_element_by_class_name("btn")
        button.click()

        self.assertIn("Currency Converter", self._driver.title)

    def _check_addition(self):
        """
        Checks the addition function.
        """
        # Perform the calculation 1 + 2 =
        digit_1 = self._driver.find_element_by_class_name("digit-1")
        digit_1.click()
        plus_operator = self._driver.find_element_by_class_name("operator-plus")
        plus_operator.click()
        digit_2 = self._driver.find_element_by_class_name("digit-2")
        digit_2.click()
        equals_operator = self._driver.find_element_by_class_name("operator-equals")
        equals_operator.click()

        # Check that the display shows 3.
        display = self._driver.find_element_by_class_name("display")
        self.assertEqual("3", display.text)

    def _check_subtraction(self):
        """
        Checks the subtraction function.
        """
        # Perform the calculation 15 - 7 =
        digit_1 = self._driver.find_element_by_class_name("digit-1")
        digit_1.click()
        digit_5 = self._driver.find_element_by_class_name("digit-5")
        digit_5.click()
        plus_operator = self._driver.find_element_by_class_name("operator-subtract")
        plus_operator.click()
        digit_7 = self._driver.find_element_by_class_name("digit-7")
        digit_7.click()
        equals_operator = self._driver.find_element_by_class_name("operator-equals")
        equals_operator.click()

        # Check that the display shows 8.
        display = self._driver.find_element_by_class_name("display")
        self.assertEqual("8", display.text)

    def _check_multiplication(self):
        """
        Checks the multiplication function.
        """
        # Perform the calculation 12 * 5 =
        digit_1 = self._driver.find_element_by_class_name("digit-1")
        digit_1.click()
        digit_2 = self._driver.find_element_by_class_name("digit-2")
        digit_2.click()
        multiply_operator = self._driver.find_element_by_class_name("operator-multiply")
        multiply_operator.click()
        digit_5 = self._driver.find_element_by_class_name("digit-5")
        digit_5.click()
        equals_operator = self._driver.find_element_by_class_name("operator-equals")
        equals_operator.click()

        # Check that the display shows 60.
        display = self._driver.find_element_by_class_name("display")
        self.assertEqual("60", display.text)

    def _check_division(self):
        """
        Checks the division function.
        """
        # Perform the calculation 100 / 25 =
        digit_1 = self._driver.find_element_by_class_name("digit-1")
        digit_1.click()
        digit_0 = self._driver.find_element_by_class_name("digit-0")
        digit_0.click()
        digit_0.click()
        multiply_operator = self._driver.find_element_by_class_name("operator-divide")
        multiply_operator.click()
        digit_2 = self._driver.find_element_by_class_name("digit-2")
        digit_2.click()
        digit_5 = self._driver.find_element_by_class_name("digit-5")
        digit_5.click()
        equals_operator = self._driver.find_element_by_class_name("operator-equals")
        equals_operator.click()

        # Check that the display shows 4.
        display = self._driver.find_element_by_class_name("display")
        self.assertEqual("4", display.text)

    def tearDown(self):
        self._driver.quit()


if __name__ == "__main__":
    unittest.main()
