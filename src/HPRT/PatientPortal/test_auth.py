from django.test import TestCase
from PatientPortal.models import Doctor


class AuthTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.dr_1 = Doctor.objects.create_user(
            username='dr_1', password='password', user_type='D')
        cls.a_1 = Doctor.objects.create_user(
            username='a_1', password='password', user_type='A')

    def log_in(self, user_type):
        if user_type == 'dr':
            login_username = self.dr_1.username
        else:
            login_username = self.a_1.username
        return self.client.login(username=login_username, password='password')

    def test_unauthenticated_root_access(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    def test_authenticated_root_access(self):
        self.log_in('dr')
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
