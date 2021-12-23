from rest_framework.test import APITestCase
from account.models import User


class TestModel(APITestCase):

    def test_creates_user(self):
        user = User.objects.create_user(
            'Test', 'test@gmail.com', 1995, 'password123')
        self.assertIsInstance(user, User)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'test@gmail.com')

    def test_creates_super_user(self):
        user = User.objects.create_superuser(
            'Test', 'test@gmail.com', 1995, 'password123')
        self.assertIsInstance(user, User)
        self.assertTrue(user.is_staff)
        self.assertEqual(user.email, 'test@gmail.com')

    def test_raises_error_when_no_username_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username="", email='test@gmail.com', password='password123', birth_year=1995)

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given username must be set'):
            User.objects.create_user(
                username="", email='test@gmail.com', password='password123', birth_year=1995)

    def test_raises_error_when_no_email_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username="Test", email='', password='password123', birth_year=1995)

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given email must be set'):
            User.objects.create_user(
                username="Test", email='', password='password123', birth_year=1995)

    def test_raises_error_when_no_birth_year_is_supplied(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username="Test", email='test@gmail.com', password='password123', birth_year=None)

    def test_raises_error_with_message_when_no_email_is_supplied(self):
        with self.assertRaisesMessage(ValueError, 'The given birth year must be set'):
            User.objects.create_user(
                username="Test", email='test@gmail.com', password='password123', birth_year=None)

    def test_raises_error_when_age_is_under_18(self):
        self.assertRaises(ValueError, User.objects.create_user,
                          username="Test", email='test@gmail.com', password='password123', birth_year=2021)

    def test_raises_error_with_message_when_age_is_under_18(self):
        with self.assertRaisesMessage(ValueError, 'You must be a legacy adult'):
            User.objects.create_user(
                username="Test", email='test@gmail.com', password='password123', birth_year=2021)

    def test_cant_creates_super_user_with_is_staff_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_staff=True.'):
            User.objects.create_superuser(
                username="test", email='test@gmail.com', password='password123', birth_year=1995, is_staff=False)

    def test_cant_creates_super_user_with_super_user_status(self):
        with self.assertRaisesMessage(ValueError, 'Superuser must have is_superuser=True.'):
            User.objects.create_superuser(
                username="test", email='test@gmail.com', password='password123', birth_year=1995, is_superuser=False)
