from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successfull(self):
        """test creating a user with an email successfull"""
        email = "test@gmail.com"
        password = "test@123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_with_email_normalized(self):
        """test the email for a user is normalized"""
        email = "test@GMAIL.com"
        password = "test@123"
        user = get_user_model().objects.create_user(email, password)
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with invalid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser_invalid_email(self):
        """test creating new superuser """
        user = get_user_model().objects.create_superuser(
            "test@gmail.com",
            "test@123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
