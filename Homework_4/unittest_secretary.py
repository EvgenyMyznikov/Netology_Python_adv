import unittest
from unittest.mock import patch
from secretary import check_document_existence, get_doc_owner_name, get_all_doc_owners_names, \
    remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, \
    move_doc_to_shelf, show_document_info, show_all_docs_info, add_new_doc, secretary_program_start


class TestSecretary(unittest.TestCase):

    def setUp(self):
        print('method setup')

    def tearDown(self):
        print('method teardown')

    def test_document_existence(self):
        self.assertEqual(check_document_existence("2207 876234"), True)

    @patch('builtins.input', return_value='10006')
    def test_doc_owner(self, mock_input):
        self.assertEqual(get_doc_owner_name(), "Аристарх Павлов")

    def test_all_doc_owners(self):
        self.assertEqual(get_all_doc_owners_names(),
                         {'Геннадий Покемонов', "Иван Иванов", 'Аристарх Павлов', 'Василий Гупкин'})

    def test_remove_doc(self):
        self.assertEqual(remove_doc_from_shelf("2207 876234"), None)

    @patch('builtins.input', return_value='4')
    def test_add_new_shelf(self, mock_input):
        self.assertEqual(add_new_shelf('4'), ('4', True))

    def test_append_doc_to_shelf(self):
        self.assertEqual(append_doc_to_shelf('10006', '3'), None)

    @patch('builtins.input', return_value='11-2')
    def test_delete_doc(self, mock_input):
        self.assertEqual(delete_doc(), ("11-2", True))

    @patch('builtins.input', return_value='10006')
    def test_get_doc_shelf(self, mock_input):
        self.assertEqual(get_doc_shelf(), '2')

    @patch('builtins.input', side_effect=['5455 028765', '3'])
    def test_move_doc(self, mock_input):
        self.assertEqual(move_doc_to_shelf(), None)

    def test_show_document_info(self):
        self.assertEqual(show_document_info(
            {"type": "passport",
             "number": "2207 876234",
             "name": "Василий Гупкин"}
        ), None)

    def test_show_all_docs(self):
        self.assertEqual(show_all_docs_info(), None)

    @patch('builtins.input', side_effect=["4507 123456", "passport", "Иван Иванов", '2'])
    def test_add_new_doc(self, mock_input):
        self.assertEqual(add_new_doc(), '2')

    # def test_secretary_program_start(self):
    #     self.assertEqual(secretary_program_start(), None)


if __name__ == '__main__':
    unittest.main()
