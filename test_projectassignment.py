import unittest
import os
from mock import patch
import project_assignment
import mock
import sys

TESTDATA_FILENAME = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' '/assets/testfile.txt'))

def suite():
    testsuite = unittest.TestSuite()
    testsuite.addTest(unittest.makeSuite(MyTest))
    return testsuite

class MyTest(unittest.TestCase):

    def setUp(self):
       self.testfile = open(TESTDATA_FILENAME, "r")
       self.testdata = self.testfile.read()

    @patch("project_assignment.create_output")
    @patch("project_assignment.get_input")
    def test_main(self, mock_get_input, mock_create_output):
        mock_get_input.return_value=self.testdata.split('\n')
        project_assignment.main()
        mock_get_input.assert_called()
        mock_create_output.assert_called()

    @patch("project_assignment.get_input")
    def test_main_exception(self, mock_get_input):
        mock_get_input.side_effect = [Exception]
        self.assertRaises(Exception, project_assignment.main())


    @patch("project_assignment.open")
    @patch("project_assignment.sys")
    def test_get_input(self, mock_sys, mock_open):
        test_file = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' '/assets/testfile.txt'))
        file = open(test_file, "r")
        mock_open.return_value=file
        expected = self.testdata.split('\n')
        actual = project_assignment.get_input()
        mock_open.assert_called()
        self.assertEqual(actual, expected, "values are equal")


    def test_create_output(self):
        #Empty List
        unique_list = []
        project_assignment.create_output(unique_list)

        #No match in legal categories
        unique_list = ["test"]
        project_assignment.create_output(unique_list)

        #Actual List
        unique_list = ["PERSON Bob Jones", "PLACE Washington", "PERSON Mary", "COMPUTER Mac", "OTHER Tree", "ANIMAL Dog", "PLACE Texas",
                       "FOOD Steak", "ANIMAL Cat"]
        project_assignment.create_output(unique_list)


    def tearDown(self):
       self.testfile.close()


if __name__ == '__main__':
    unittest.main()