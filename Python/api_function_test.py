import unittest
import json
from app import app, get_db_connection, create_table

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        create_table()

    def tearDown(self):
        conn = get_db_connection()
        conn.execute("DROP TABLE IF EXISTS tasks")
        conn.commit()
        conn.close()

    def test_add_task(self):
        response = self.app.post('/add_task', json={"task": "Sample task"})
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertTrue(data['success'])
        self.assertIsNotNone(data['task_id'])

    def test_get_tasks(self):
        # Add a task first
        self.app.post('/add_task', json={"task": "Sample task"})
        response = self.app.get('/tasks')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)
        self.assertGreater(len(data), 0)
        self.assertIn('Sample task', [task['task'] for task in data])

if __name__ == '__main__':
    unittest.main()