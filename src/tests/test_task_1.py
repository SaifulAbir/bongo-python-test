import io
import unittest.mock
import unittest
from src.task_1 import print_depth


class TestTask1(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, data, expected_output, mock_stdout):
        print_depth(data)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test__when_dict_is_empty__should_pass(self):
        data = {}
        self.assert_stdout(data, '')

    def test__when_dict_has_one_element__should_pass(self):
        data = {
            "key1": 1
        }
        self.assert_stdout(data, 'key1 1\n')

    def test__when_dict_has_multiple_element__should_pass(self):
        data = {
            "key1": 1,
            "key2": 2,
            "key3": 3,
        }
        self.assert_stdout(data, 'key1 1\nkey2 1\nkey3 1\n')

    def test__when_dict_has_nested_empty_dict__should_pass(self):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {}
            }
        }
        self.assert_stdout(data, 'key1 1\nkey2 1\nkey3 2\nkey4 2\n')

    def test__when_dict_has_multiple_nested_dict__should_pass(self):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4
                }
            }
        }
        self.assert_stdout(data, 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\n')


if __name__ == '__main__':
    unittest.main()