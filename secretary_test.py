import unittest
from Secretary import  check_document_existance, get_doc_owner_name, \
    get_all_doc_owners_names, add_new_doc, append_doc_to_shelf, documents, delete_doc

class TestSomething(unittest.TestCase):
    def setUp(self):
        print("method setUp")

    def tearDown(self):
        print("method tearDown")

    def test_get_doc_owner_name(self):
        print('Номера документов для проверки: 2207 876234, 11-2, 10006')
        self.assertEqual(get_doc_owner_name(), 'Василий Гупкин')
        self.assertEqual(get_doc_owner_name(), 'Геннадий Покемонов')
        self.assertEqual(get_doc_owner_name(), 'Аристарх Павлов')


    def test_new_doc(self):
        print('Номера документa для проверки: 123; тип: Passport, имя: Andrey Andreev, номер полки: 3')
        new_doc_shelf_number = '3'
        self.assertEqual(add_new_doc(), new_doc_shelf_number)


    def test_delete_doc(self):
        new_doc = {
            "type": 'INN',
            "number": '123',
            "name": 'Andrey Andreev'
        }

        doc_number = '123'
        doc_shelf_number = '3'

        documents.append(new_doc)
        append_doc_to_shelf(doc_number, doc_shelf_number)

        self.assertTrue(check_document_existance(doc_number))

        print('Номера документa для проверки: 123')
        self.assertTrue(delete_doc(), '10006')

    def test_get_all_doc_owners_names(self):
        self.assertEqual(get_all_doc_owners_names(), {'Василий Гупкин', 'Геннадий Покемонов', 'Аристарх Павлов'})


    def test_show_all_docs_info(self):
        test_doc_number = '2207 876234'
        test_doc_number2 = '11-2'
        test_doc_number3 = '10006'

        self.assertTrue(check_document_existance(test_doc_number))
        self.assertTrue(check_document_existance(test_doc_number2))
        self.assertTrue(check_document_existance(test_doc_number3))

if __name__ == '__main__':
    unittest.main()


