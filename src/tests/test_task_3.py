import io
import unittest.mock
import unittest
from src.task_3 import Node, lca


class TestTask3(unittest.TestCase):

    def setUp(self):
        self.node1 = Node(1, None)
        self.node2 = Node(2, self.node1)
        self.node3 = Node(3, self.node1)
        self.node4 = Node(4, self.node2)
        self.node5 = Node(5, self.node2)
        self.node6 = Node(6, self.node3)
        self.node7 = Node(7, self.node3)
        self.node8 = Node(8, self.node4)
        self.node9 = Node(9, self.node4)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n1, n2, expected_output, mock_stdout):
        lca(n1, n2)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test__when_root_node_is_passed__should_return_itself(self):
        self.assert_stdout(self.node1, self.node1, '1\n')

    def test__when_same_nodes_are_passed__should_return_itself(self):
        self.assert_stdout(self.node4, self.node4, '4\n')

    def test__when_leaf_nodes_are_passed__should_return_1(self):
        self.assert_stdout(self.node5, self.node7, '1\n')

    def test__when_root_and_leaf_nodes_are_passed__should_return_1(self):
        self.assert_stdout(self.node9, self.node1, '1\n')

    def test__when_siblings_node8_9_are_passed__should_return_4(self):
        self.assert_stdout(self.node8, self.node9, '4\n')

    def test__when_node8_5_are_passed__should_return_2(self):
        self.assert_stdout(self.node8, self.node5, '2\n')

    def test__when_node5_2_are_passed__should_return_2(self):
        self.assert_stdout(self.node5, self.node2, '2\n')

    def test__when_node9_2_are_passed__should_return_2(self):
        self.assert_stdout(self.node9, self.node2, '2\n')


if __name__ == '__main__':
    unittest.main()