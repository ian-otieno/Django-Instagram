from django.test import TestCase
from .models import Profile, Images, Comment

# Create your tests here.
class TestProfile(TestCase):
    def setUp(self):
        self.bio =Profile(bio = "I like instagram")

    def test_instance(self):
        self.assertTrue(isinstance(self.bio, Profile))

    def test_save_method(self):
        self.bio.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile)>0)

    def test_dalete_profile(self):
        self.bio.save_profile()
        profile = Profile.objects.all()
        self.bio.delete_profile()
        self.assertTrue(len(profile)==0)

    def test_update_profile(self):
        self.bio.save_profile()
        profile = Profile.objects.filter(self.bio)
        self.bio.update_profile()
        self.bio.save_profile()
        self.assertTrue(len(profile)==1)

class TestImage(TestCase):
    def setUp(self):
        self.bio = Profile(bio = 'I like instagram')
        self.bio.save_profile()

        self.new_image = Images(image_name='Iano', image_caption = 'you look awesome', profile=self.bio)
        self.new_image.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_image, Images))
        

    def tearDown(self):
        Profile.objects.all().delete()
        Images.objects.all().delete()

    def test_save_image(self):
        self.new_image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images)>0)

    def test_delete_image(self):
        self.new_image.save_image()
        images = Images.objects.all()
        self.new_image.delete_image()
        self.assertTrue(len(images)==0)

    def test_update_caption(self):
        self.new_image.save_image()
        image = Images.objects.filter(self.new_image)
        self.new_image.update_caption()
        self.new_image.save_image()
        self.assertTrue(len(image)==1)
        
class TestComment(TestCase):
    def setUp(self):
        self.bio = Profile(bio = 'I like instagram')
        self.bio.save_profile()

        self.new_image = Images(image_name='Iano', image_caption = 'you look awesome', profile=self.bio)
        self.new_image.save()

        self.new_comment = Comment(comments = 'great',)
        self.new_comment.save

    def test_instance(self):
        self.assertTrue(isinstance(self.new_comment, Comment))

    def tearDown(self):
        Profile.objects.all().delete()
        Images.objects.all().delete()
        Comment.objects.all().delete()

    def test_save_comment(self):
        self.new_comment.save_comment()
        comment = Comment.objects.all()
        self.assertTrue(len(comment)>0)

    def test_delete_comment(self):
        self.new_comment.save_comment()
        comment = Comment.objects.all()
        self.new_comment.delete_commnet()
        self.assertTrue(len(comment)==0)        
