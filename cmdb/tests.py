from django.test import TestCase
from django.core.urlresolvers import resolve
from cmdb.views import homepage
from django.http import HttpRequest
# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolvess_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func,homepage)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()

        response = homepage(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))