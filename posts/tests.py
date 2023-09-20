from django.test import TestCase

from django.contrib.auth import get_user_model # To get our user set in settings

from .models import Post


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = 'testuser',
            email = 'testemail@email.com',
            password = 'testpassword',
        )

        cls.post = Post.objects.create(
            title = 'newpost',
            body = 'This is a new post',
            author = cls.user,

        )


    def test_post_model(self):
        self.assertEqual(self.post.author.username, 'testuser')
        self.assertEqual(self.post.title, "newpost")
        self.assertEqual(self.post.body, "This is a new post")
        self.assertEqual(str(self.post), "newpost")
