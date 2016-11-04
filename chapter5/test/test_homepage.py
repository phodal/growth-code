from django.test import LiveServerTestCase
from selenium import webdriver


class HomepageTestCase(LiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        super(HomepageTestCase, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(HomepageTestCase, self).tearDown()

    def test_visit_homepage(self):
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/")
        )

        self.assertIn("Growth Studio - Enjoy Create & Share",
                      self.selenium.title)
