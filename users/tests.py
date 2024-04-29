# from users.models import CustomUser
#
# from django.test import TestCase
# from django.urls import reverse
# class RegistrationTestCase(TestCase):
#     def test_user_account_created(self):
#         self.client.post(reverse('users:register'), data={
#             "username": "abduvohid",
#             'first_name': 'Abduvohid',
#             'last_name': 'Abduvohid',
#             "email": "abdujalilov2629@gmail.com",
#             "password": "2004",
#         })
#
#         user = User.objects.get(username="abduvohid")
#
#         self.assertEqual(user.first_name, 'Abduvohid')
#         self.assertEqual(user.last_name, 'Abduvohid')
#         self.assertEqual(user.email, 'abdujalilov2629@gmail.com')
#         self.assertNotEqual(user.password, '2004')
#         self.assertTrue(user.check_password('2004'))
#
#     def test_required_fields(self):
#         response = self.client.post(
#             reverse('users:register'),
#             data={
#                 'first_name': 'Abduvohid',
#                 'email': 'abdujalilov2629@gmail.com'
#             }
#         )
#         user_count = User.objects.count()
#         self.assertEqual(user_count, 0)
#         self.assertFormError(response, "form", 'username', 'This field is required.')
#         self.assertFormError(response, "form", 'password', 'This field is required.')
#
#     def invalid_email(self):
#         response = self.client.post(reverse('users:register'), data={
#             "username": "abduvohid",
#             'first_name': 'Abduvohid',
#             'last_name': 'Abduvohid',
#             "email": "abdujalilov2",
#             "password": "2004",
#         })
#         user_count = User.objects.count()
#         self.assertEqual(user_count, 0)
#         self.assertEqual(response, 'form', 'email', 'This field is required.')
#
