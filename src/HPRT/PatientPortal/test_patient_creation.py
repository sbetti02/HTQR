from PatientPortal.testing_utils import HPRTTestCase


class CreatePatientTests(HPRTTestCase):
    def test_simple_create_site(self):
        self.create_site('Lynn')

    def test_simple_create_patient(self):
        self.create_patient()
