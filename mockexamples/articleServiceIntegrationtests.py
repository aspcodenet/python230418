from articleService import Article, getArticlesToShow

import unittest 


class articleserviceTest(unittest.TestCase):
    def test_fetch_filters_on_userid(self):
        userId = 2
        result = getArticlesToShow(userId)
        self.assertGreater(len(result),0)
