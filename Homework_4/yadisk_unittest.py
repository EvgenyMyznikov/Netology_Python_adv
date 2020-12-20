import unittest
from Homework_4.yadisk_folder import token, get_new_folder, ya_disk_status_info, delete_new_folder


class TestYaFolder(unittest.TestCase):

    def setUp(self):
        print('method setup')

    def tearDown(self):
        delete_new_folder('Media')
        print('method teardown')

    def test_ya_disk_status(self):
        self.assertEqual(ya_disk_status_info('disk:/'), 200)

    def test_no_folder(self):
        self.assertEqual(ya_disk_status_info('Media'), 404)

    def test_new_folder(self):
        self.assertEqual(get_new_folder('Media', token), 201)

    def test_ya_disk_wrong_token(self):
        self.assertEqual(get_new_folder('Media', 'wrong_token'), 401)

    def test_sam_folder(self):
        self.assertEqual(get_new_folder('Media', token), 201)
        self.assertEqual(get_new_folder('Media', token), 409)


if __name__ == '__main__':
    unittest.main()
