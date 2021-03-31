import io
import unittest.mock
import unittest
from src.task_2 import print_depth, Person


class TestTask2(unittest.TestCase):

    def setUp(self):
        self.person_a = Person("Barbara", "Fain", None)
        self.person_b = Person("Saiful", "Islam", self.person_a)

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
            "saiful": 1,
            "abir": {}
        }
        self.assert_stdout(data, 'saiful 1\nabir 1\n')

    def test__when_dict_has_single_nested_dict__should_pass(self):
        data = {
            "saiful": 1,
            "abir": {
                "mahmud": 1
            }
        }
        self.assert_stdout(data, 'saiful 1\nabir 1\nmahmud 2\n')

    def test__when_dict_has_multiple_nested_dict__should_pass(self):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": 4,
                }
            },
        }
        self.assert_stdout(data, 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser 3\n')

    def test__when_single_person_data_passed__should_pass(self):
        data = self.person_a
        self.assert_stdout(data, 'first_name 1\n'
                                 'last_name 1\n'
                                 'father 1\n')

    def test__when_nested_person_data_passed__should_pass(self):
        data = self.person_b
        self.assert_stdout(data, 'first_name 1\n'
                                 'last_name 1\n'
                                 'father 1\n'
                                 'first_name 2\n'
                                 'last_name 2\n'
                                 'father 2\n')

    def test__when_dict_has_person_data__should_pass(self):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": self.person_a,
                }
            },
        }
        self.assert_stdout(data, 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser 3\n'
                                 'first_name 4\n'
                                 'last_name 4\n'
                                 'father 4\n')

    def test__when_dict_has_nested_person_data__should_pass(self):
        data = {
            "key1": 1,
            "key2": {
                "key3": 1,
                "key4": {
                    "key5": 4,
                    "user": self.person_b,
                }
            },
        }
        self.assert_stdout(data, 'key1 1\nkey2 1\nkey3 2\nkey4 2\nkey5 3\nuser 3\n'
                                 'first_name 4\n'
                                 'last_name 4\n'
                                 'father 4\n'
                                 'first_name 5\n'
                                 'last_name 5\n'
                                 'father 5\n')

if __name__ == '__main__':
    unittest.main()