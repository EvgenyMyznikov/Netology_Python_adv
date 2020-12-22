import pytest
from unittest.mock import patch
from Homework_4.secretary import check_document_existence, get_doc_owner_name, get_all_doc_owners_names, \
    remove_doc_from_shelf, add_new_shelf, append_doc_to_shelf, delete_doc, get_doc_shelf, \
    move_doc_to_shelf, show_document_info, show_all_docs_info, add_new_doc


class TestSecretary:

    def test_check_document_existence(self):
        assert check_document_existence("2207 876234") is True

    @patch('builtins.input', return_value='10006')
    def test_get_doc_owner_name(self, mock_input):
        assert get_doc_owner_name() == "Аристарх Павлов"

    def test_all_doc_owners(self):
        assert get_all_doc_owners_names() == {'Геннадий Покемонов', 'Аристарх Павлов', 'Василий Гупкин'}

    def test_remove_doc_from_shelf(self):
        assert remove_doc_from_shelf("2207 876234") is None

    @patch('builtins.input', return_value='4')
    def test_add_new_shelf(self, mock_input):
        assert add_new_shelf('4') == ('4', True)

    def test_append_doc_to_shelf(self):
        assert append_doc_to_shelf('10006', '3') is None

    @patch('builtins.input', return_value='11-2')
    def test_delete_doc(self, mock_input):
        assert delete_doc() == ("11-2", True)

    @patch('builtins.input', return_value='10006')
    def test_get_doc_shelf(self, mock_input):
        assert get_doc_shelf() == '2'

    @patch('builtins.input', side_effect=['5455 028765', '3'])
    def test_move_doc(self, mock_input):
        assert move_doc_to_shelf() is None

    def test_show_document_info(self):
        assert show_document_info({"type": "passport", "number": "2207 876234",
                                   "name": "Василий Гупкин"}) is None

    @patch('builtins.input', side_effect=["4507 123456", "passport", "Иван Иванов", '2'])
    def test_add_new_doc(self, mock_input):
        assert add_new_doc() == '2'

    def test_show_all_docs(self):
        assert show_all_docs_info() is None


if __name__ == '__main__':
    pytest.main()
