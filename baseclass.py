from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from lib.imagecomp import compare_images
import inspect
import os.path


class BaseClass:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.web_object = None
        self.image_dir = "./images/"
        self.test_name = self.get_test_name(inspect.stack())

    def get_test_name(self, stack_object):
        for items in range(0, len(stack_object)):
            print(stack_object[items].filename)
            if "/tests/" in stack_object[items].filename:
                file_name = stack_object[items].filename
                return os.path.splitext(os.path.basename(file_name))[0]
        return "no_name"

    def load_page(self, url_address):
        self.driver.get(url_address)

    def set_elem_by_name(self, elem_name):
        self.web_object = self.driver.find_element(by=By.NAME, value=elem_name)

    def set_elem_by_id(self, elem_id):
        self.web_object = self.driver.find_element(by=By.ID, value=elem_id)

    def send_keys_to_elem(self, keys_to_send):
        self.web_object.clear()
        self.web_object.send_keys(keys_to_send)

    def do_mouseover(self):
        action = ActionChains(self.driver)
        action.move_to_element(self.web_object).perform()

    def take_screenshot(self, test_iteration=1):
        try:
            new_filename = self.test_name + "_" + str(test_iteration) + ".png"
            self.driver.save_screenshot(self.image_dir + new_filename)
            print(f"Screenshot saved as {new_filename}")
        except Exception as e:
            print(f"Error taking screenshot {e}")

    def compare_images(self):
        file1 = self.image_dir + self.test_name + "_1.png"
        file2 = self.image_dir + self.test_name + "_2.png"
        diff = self.image_dir + self.test_name + "_diff.png"
        issue = compare_images(file1, file2, diff, 10)
        assert issue == 0

    def cleanup(self):
        self.driver.close()
