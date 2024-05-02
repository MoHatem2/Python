import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestAppUI(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()  # You need to have Chrome WebDriver installed
        self.driver.get('http://localhost:5000')  # Assuming your Flask app runs on localhost:5000
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_add_task_ui(self):
        task_input = self.driver.find_element(By.ID, 'task')
        task_input.send_keys('Sample task')
        add_button = self.driver.find_element(By.XPATH, "//button[text()='Add Task']")
        add_button.click()
        # Assuming your Flask app returns a success message after adding a task
        success_message = self.driver.find_element(By.ID, 'success-message')
        self.assertEqual(success_message.text, 'Task added successfully.')

    def test_view_tasks_ui(self):
        # Assuming there's a button or link to view tasks
        view_tasks_button = self.driver.find_element(By.XPATH, "//a[text()='View Tasks']")
        view_tasks_button.click()
        # Assuming your Flask app displays tasks in a list
        tasks_list = self.driver.find_element(By.ID, 'tasks-list')
        tasks = tasks_list.find_elements(By.TAG_NAME, 'li')
        self.assertGreater(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()