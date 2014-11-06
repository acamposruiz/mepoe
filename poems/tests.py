from django.test import TestCase
from django.contrib.auth.models import User
from .models import *
from django.core.urlresolvers import reverse


class TestPoems(TestCase):

    def setUp(self):
        # import ipdb; ipdb.set_trace()
        self.user = User.objects.create_user(
            'test', 'lennon@thebeatles.com', 'testpassword')
        self.client.login(username='test', password='testpassword')
        self.author = Author.objects.create(name='testauthor')
        self.book = Book.objects.create(name='testbook')
        self.body = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit. \
        Quisquam officia alias nostrum quae nemo ab aliquam ipsam fugiat \
        sapiente, veritatis similique non, hic praesentium delectus \
        voluptatibus consectetur aperiam, cum, culpa!'
        self.poem = Poem(
            user=self.user, author=self.author, book=self.book,
            body=self.body, title="testpoem")
        self.poem.save()

    def test_view_exist(self):
        res = self.client.get(reverse(
            'poems:poem_detail', kwargs={'pk': self.poem.pk, 'list': 'all'}))
        self.assertEqual(res.status_code, 200)
        self.assertTrue(self.poem.title in res.content)
