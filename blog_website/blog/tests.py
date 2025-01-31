from django.test import TestCase

from .models import Post
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your tests here.
# TDD => Test-Driven Development

class BlogPostTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='user1')
        self.post1 = Post.objects.create(
            title='Post1',
            text='This is the description of Post1',
            status=Post.STATUS_CHOICES[0],
            auther=self.user
        )

    def test_post_list_url(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

    def test_post_list_url_by_name(self):
        response = self.client.get(reverse('posts_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_title_on_blog_list_page(self):
        response = self.client.get(reverse('posts_list'))
        self.assertContains(response, self.post1.title)

    def test_post_detail_url(self):
        response = self.client.get(f'/blog/{self.post1.id}/')
        self.assertEqual(response.status_code, 200)

    def test_post_detail_url_by_name(self):
        response = self.client.get(reverse('posts_detail', args=[self.post1.id]))
        self.assertEqual(response.status_code, 200)

    def test_post_details_on_blog_detail_page(self):
        # response = self.client.get('/blog/1/')
        response = self.client.get(reverse('posts_detail', args=[self.post1.id]))
        self.assertContains(response, self.post1.title)
        self.assertContains(response, self.post1.text)

    def test_status_404_is_post_id_not_exist(self):
        response = self.client.get(reverse('posts_detail', args=[999]))
        self.assertEqual(response.status_code, 404)

