from articleService import Article, getArticlesToShow

import unittest 
from unittest.mock import Mock,patch, MagicMock

# class Mock():
#     def __init__(self, request, context):
#         return None

#     def read(self):
#         return self

#     def decode(self, arg):
#         return ''

#     def __iter__(self):
#         return self

#     def __next__(self):
#         raise StopIteration



class articleserviceTest(unittest.TestCase):
    def test_fetch_filters_on_userid(self):
        userId = 2

        result = getArticlesToShow(userId)

        antalFelUserId = 0
        for x in result:
            if x.UserId != userId:
                antalFelUserId = antalFelUserId + 1
        self.assertEqual(0,antalFelUserId)
        self.assertGreater(len(result),0)


    def test_unit_fetch_filters_on_userid(self):
        userId = 2

        open_mock = MagicMock()
        open_mock.getcode.return_value = 200
        #open_mock.read.return_value
        open_mock.__enter__.return_value = open_mock
        open_mock.return_value = open_mock
        open_mock.read.return_value = open_mock
        open_mock.decode.return_value = '[{"userId":1, "id":1, "title":"Stefan"},{"userId":2, "id":2, "title":"Stefan2"},{"userId":2, "id":3, "title":"Stefan3"}]'      
        with patch('articleService.urlopen', new=open_mock):

            result = getArticlesToShow(userId)

        antalFelUserId = 0
        for x in result:
            if x.UserId != userId:
                antalFelUserId = antalFelUserId + 1
        self.assertEqual(0,antalFelUserId)
        self.assertEqual(len(result),2)


unittest.main()