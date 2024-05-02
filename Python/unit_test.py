import unittest
from app import get_db_connection, create_table 

class TestApp(unittest.TestCase):

    def test_get_db_connection(self):
        # Test if get_db_connection returns a valid connection
        conn = get_db_connection()
        self.assertIsNotNone(conn)
        conn.close()

    def test_create_table(self):
        # Test if create_table function creates the 'tasks' table
        create_table()
        conn = get_db_connection()
        tables = conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        table_names = [table['name'] for table in tables]
        self.assertIn('tasks', table_names)
        conn.close()

if __name__ == '_main_':
    unittest.main()