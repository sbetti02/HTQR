from PatientPortal.testing_utils import HPRTTestCase


class EndpointTests(HPRTTestCase):
    def test_new_patient_page(self):
        response = self.client.get('/patient/new/')
        self.assertEqual(response.status_code, 200)

    def test_edit_patient(self):
        patient = self.create_patient()
        response = self.client.get(f'/patient/{patient.pk}/edit/')
        self.assertEqual(response.status_code, 200)

    def test_delete_patient(self):
        patient = self.create_patient()
        response = self.client.get(f'/patient/{patient.pk}/delete/')
        self.assertEqual(response.status_code, 200)

    def test_add_existing_page(self):
        response = self.client.get('/patient/addexisting/')
        self.assertEqual(response.status_code, 200)

    def test_dr_cant_access_new_site_page(self):
        response = self.client.get('/site/new/')
        self.assertEqual(response.status_code, 403)

    def test_admin_accesses_new_site_page(self):
        self.log_in('a')
        response = self.client.get('/site/new/')
        self.assertEqual(response.status_code, 200)

    def test_remove_patient_from_list(self):
        pass

    def test_add_patient_to_list(self):
        pass
