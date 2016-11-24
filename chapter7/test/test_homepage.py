from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from blog.models import Blog


class HomepageTestCase(StaticLiveServerTestCase):
    def setUp(self):
        self.selenium = webdriver.Chrome()
        self.selenium.maximize_window()
        self.user = User.objects.create_user(username='phodal', email='h@phodal.com', password='phodal')
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

    def test_should_goto_blog_page_from_homepage(self):
        Blog.objects.create(title='hello', author=self.user, slug='this_is_a_test', body='This is blog detail',
                            posted=datetime.now)
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/")
        )
        self.selenium.find_element_by_link_text('博客').click()

        self.assertIn("This is blog detail",
                      self.selenium.page_source)

    def test_should_goto_blog_detail_page_when_click_blog_title(self):
        Blog.objects.create(title='hello', author=self.user, slug='this_is_a_test', body='This is blog detail',
                            posted=datetime.now)
        self.selenium.get(
            '%s%s' % (self.live_server_url, "/blog")
        )
        self.selenium.find_element_by_link_text('hello').click()

        self.assertIn("/blog/this_is_a_test.html", self.selenium.current_url)
