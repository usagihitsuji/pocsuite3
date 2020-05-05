import unittest
from pocsuite3.api import crawl


class TestCase(unittest.TestCase):
    def setUp(self):
        self.url = 'http://demo.digitallib.com/mediaDetail.action/'

    def tearDown(self):
        pass

    def verify_result(self, urls):
        links = urls['url']
        self.assertTrue(len(links) > 0)
        url = links.pop()
        url = url.split('?')[0]
        self.assertTrue(url.endswith(('.action', '.do')))

    def xtest_import_run(self):
        urls = crawl(self.url, url_ext=('.action', '.do'))
        self.verify_result(urls)
