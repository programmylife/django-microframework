from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.post = Post.objects.create(
            body="post text",
        )

    def test_post_model(self):
        self.assertEqual(self.post.body, "post text")
