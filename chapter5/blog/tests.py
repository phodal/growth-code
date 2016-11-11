from datetime import datetime
from django.core.urlresolvers import resolve
from django.test import TestCase

from blog.models import Blog
from blog.views import blog_detail


class BlogpostTest(TestCase):
    def test_blogpost_url_resolves_to_blog_post_view(self):
        found = resolve('/blog/this_is_a_test.html')
        self.assertEqual(found.func, blog_detail)

    def test_blogpost_create_with_view(self):
        Blog.objects.create(title='hello', author='admin', slug='this_is_a_test', body='This is a blog',
                            posted=datetime.now)
        response = self.client.get('/blog/this_is_a_test.html')
        self.assertIn(b'This is a blog', response.content)
