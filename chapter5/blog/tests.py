from datetime import datetime

from django.contrib.auth.models import User
from django.core.urlresolvers import resolve
from django.test import TestCase

from blog.models import Blog
from blog.views import blog_detail, blog_list


class BlogpostListTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='phodal', email='h@phodal.com', password='phodal')

    def test_blogpost_url_resolves_to_blog_list_view(self):
        found = resolve('/blog/')
        self.assertEqual(found.func, blog_list)

    def test_blog_list_page(self):
        Blog.objects.create(title='hello', author=self.user, slug='this_is_a_test', body='This is a blog',
                            posted=datetime.now)
        response = self.client.get('/blog/')
        self.assertIn(b'This is a blog', response.content)


class BlogpostDetailTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='phodal', email='h@phodal.com', password='phodal')

    def test_blogpost_url_resolves_to_blog_post_detail_view(self):
        found = resolve('/blog/this_is_a_test.html')
        self.assertEqual(found.func, blog_detail)

    def test_blogpost_create_with_view(self):
        Blog.objects.create(title='hello', author=self.user, slug='this_is_a_test', body='This is blog detail',
                            posted=datetime.now)
        response = self.client.get('/blog/this_is_a_test.html')
        self.assertIn(b'This is blog detail', response.content)

    def test_not_found_blog(self):
        response = self.client.get('/blog/this_not_a_blog.html')
        self.assertEqual(404, response.status_code)
