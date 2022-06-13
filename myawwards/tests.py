from django.test import TestCase
from .models import *

class TestUser(TestCase):
    def setUp(self):
        self.e_user = User(username="ray",email="test@gmail.com",password="qwerty")
        self.e_user.save()

    def test_user_instance(self):
        self.assertTrue(isinstance(self.e_user, User))
class TestProfile(TestCase):
    def setUp(self):
        self.e_user = User(username="ray",email="test@gmail.com",password="qwerty")
        self.e_user.save()

        self.e_profile=Profile(user=self.e_user,bio="code eat sleep rewind",image="../images/default.png")

    def test_profile_instance(self):
        self.assertTrue(isinstance(self.e_profile, Profile))

class TestProject(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='ray')
        self.post = Project.objects.create(id=1, title='awesomeness', image='../images/default.png', description='hello world',user=self.user, url='https://drive.google.com/drive/folders/1sl4UGCq-dcmqcPed6DY33YlFxrEym476')

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Project))

    def test_save_post(self):
        self.post.save_project()
        post = Project.objects.all()
        self.assertTrue(len(post) > 0)

    def test_get_posts(self):
        self.post.save()
        posts = Project.all_projects()
        self.assertTrue(len(posts) > 0)

    def test_search_post(self):
        self.post.save()
        post = Project.search_by_title('awesomeness')
        self.assertTrue(len(post) > 0)

    def test_delete_post(self):
        self.post.delete_project()
        post = Project.search_by_title('awesomeness')
        self.assertTrue(len(post) < 1)

class TestRating(TestCase):
    def setUp(self):
        self.user = User.objects.create(id=1, username='ray')
        self.post = Project.objects.create(id=1, title='testing', image='../images/default.png',url="https://meet.google.com/ted-gdcy-vvn?pli=1&authuser=1", description='coding is fun',user=self.user)
        self.rating = Rating.objects.create(id=1,usability=9,content = 9, design=8,user=self.user, post=self.post)

    def test_instance(self):
        self.assertTrue(isinstance(self.rating, Rating))

    def test_save_rating(self):
        self.rating.save_rating()
        rating = Rating.objects.all()
        self.assertTrue(len(rating) > 0)

    def test_get_rating(self,id):
        self.rating.save()
        rating = Rating.get_rating(post_id=id)
        self.assertTrue(len(rating) == 1)


