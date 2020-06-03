from django.test import TestCase
from .models import Profile,Image,Comment
from djsngo.contrib.auth.models import User

# Create your tests here.
class ProfileTestClass(TestCase):
    '''
    Test class for the profile class
    '''
    def setUp(self):
        self.kamau = User(username = "kamau", email = "kamau@gmail.com",password = "123password")
        self.kamau.save()
        

    def tearDown(self):
        Profile.objects.all().delete()
        User.objects.all().delete()
     
    def test_image_instance(self):
        self.assertTrue(isinstance(self.kamau.profile , Profile))

    def test_search_user(self):
        self.kamau.save()
        user = Profile.search_user(self.kamau)
        self.assertEqual(len(user), 1)

class ImageTestClass(TestCase):
    '''
    Test class for the Image class.
    '''
    def setUp(self):
        self.kamau = User(username = "kamau", email = "kamau@gmail.com",password = "123password")
        self.potrait = Image(image = 'imageurl', name ='potrait', caption = 'Potraits are more official than landscape images.', profile = self.kamau)

        self.kamau.save()
        self.potrait.save_image()

    def tearDown(self):
        Image.objects.all().delete()
     
    def test_image_instance(self):
        self.assertTrue(isinstance(self.potrait, Image))

    def test_save_image_method(self):
        self.potrait.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)> 0)

    def test_delete_image(self):
        self.potrait.save_image()
        images1 = Image.objects.all()
        self.assertEqual(len(images1),1)
        self.potrait.delete_image()
        images2 = Image.objects.all()
        self.assertEqual(len(images2),0)

    def test_update_caption(self):
        self.potrait.save_image()
        self.potrait.update_caption('Business photography.')
        self.assertEqual(self.potrait.caption, 'Business photography')

    def test_get_profile_image_(self):
        self.potrait.save_image
        self.kamau.save()
        profile_image = Image.get_profile_images(self.kamau)
        self.assertEqual(len(profile_image),1 )

class CommentTestClas(TestCase):
    '''
    Test class for the comments
    '''
    def setUp(self):
        self.kamau = User(username = "kamau", email = "kamau@gmail.com",password = "123password")
        self.potrait = Image(image = 'imageurl', name ='potrait', caption = 'Potraits are more official than landscape images.', profile = self.kamau)
        self.comment = Comment(image=self.potrait, content= 'Professional', user = self.kamau)

        self.kamau.save()
        self.potrait.save_image()
        self.comment.save_comment()

    def tearDown(self):
        Image.objects.all().delete()
        Comment.objects.all().delete()

    def test_comment_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment_method(self):
        self.comment.save_comment()
        comments = Comment.objects.all()
        self.assertTrue(len(comments)> 0)

    def test_delete_comment(self):
        self.comment.save_comment()
        comments1 = Comment.objects.all()
        self.assertEqual(len(comments1),1)
        self.comment.delete_comment()
        comments2 = Comment.objects.all()
        self.assertEqual(len(comments2),0)

    def test_get_image_comments(self):
        comments = Comment.get_image_comments(self.potrait)
        self.assertTrue(len(comments) > 0)