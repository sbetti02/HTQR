from django.test import TestCase
from PatientPortal.models import Doctor, Patient, Site


class HPRTTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.dr_1 = Doctor.objects.create_user(
            username='dr_1', password='password', user_type='D')
        cls.a_1 = Doctor.objects.create_user(
            username='a_1', password='password', user_type='A')

    def setUp(self):
        self.log_in('dr')

    def log_in(self, user_type):
        if user_type == 'dr':
            login_username = self.dr_1.username
        else:
            login_username = self.a_1.username
        return self.client.login(username=login_username, password='password')

    def create_site(self, name):
        self.log_in('a')
        num_sites = len(Site.objects.all())
        response = self.client.post('/site/new/', {
            'name': name
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Site.objects.all()), num_sites + 1)
        return Site.objects.get(name=name)

    def create_patient(self, name=None, site=None):
        if not name:
            name = 'Scott'
        if not site:
            random_site = Site.objects.first()
            if random_site:
                site = random_site
            else:
                site = self.create_site('Lynn')

        num_patients = len(Patient.objects.all())

        response = self.client.post('/patient/new/', {
            'name': name,
            'gender': 'Male',
            'DOB': '10/18/1995',
            'blood_type': 'O',
            'height': 1,
            'weight': 2,
            'site': site.pk,
            'allergies': 'None',
            'current_medications': 'f',
            'phone_number': 2403806668,
            'email': 'scott.bettigole@gmail.com'
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Patient.objects.all()), num_patients + 1)
        return Patient.objects.get(name=name)
