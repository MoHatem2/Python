import unittest
from app import app, create_table, get_db_connection 

class TestIntegration(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()
        create_table()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_add_task_route(self):
        response = self.client.post('/add', data={'title': 'Test Task'})
        self.assertEqual(response.status_code, 302)  # Redirect status code

        # Check if the task was added to the database
        conn = get_db_connection()
        task = conn.execute('SELECT * FROM tasks WHERE title=?', ('Test Task',)).fetchone()
        conn.close()
        self.assertIsNotNone(task)

if __name__ == '_main_':
    unittest.main()