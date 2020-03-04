# from django.test import TestCase, Client
# from django.contrib.auth import get_user_model
# from django.urls import reverse
#
# class AdminSiteTests(TestCase):
#
#     def setup(self):
#         self.client = Client()
#         self.admin_user = get_user_model().objects.create_superuser(
#             email='testadmin@gmail.com',
#             password="test@123"
#         )
#         self.client.force_login(self.admin_user)
#         self.user = get_user_model().objects.create_user(
#             email='test@gmail.com',
#             password="test@123",
#             name="test user full name"
#         )
#
#     # def test_user_listed(self):
#     #     """test that user are listed on user page"""
#     #     url = reverse("admin:core_user_changelist")
#     #     response = self.client.get(url)
#     #     self.assertContains(response, self.user.name)
#     #     self.assertContains(response, self.user.email)
