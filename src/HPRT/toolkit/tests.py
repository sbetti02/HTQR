from PatientPortal.testing_utils import HPRTTestCase


class ToolkitEndpointTests(HPRTTestCase):
    def setUp(self):
        super().setUp()
        self.patient = self.create_patient()

    def test_access_toolkit_home(self):
        response = self.client.get(f'/toolkit/{self.patient.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_generic_toolkit_info(self):
        endpoints = [
            'ask',
            'identify',
            'diagnose&treat',
            'refer',
            'reinforce&teach',
            'recommend',
            'reduce_risks',
            'culturally_attuned',
            'prescribe',
            'close&schedule',
            'prevent_burnout'
        ]
        for endpoint in endpoints:
            response = self.client.get(f'/toolkit/{self.patient.pk}/{endpoint}/')
            self.assertEqual(response.status_code, 200)

    def test_screening_page_access(self):
        response = self.client.get(f'/toolkit/screenings/{self.patient.pk}')
        self.assertEqual(response.status_code, 200)

    def test_new_diagnostic_page_access(self):
        pages = [
            'new_htq',
            'new_dsmv',
            'new_th',
            'new_hp1',
            'new_hp2',
            'new_gh'
        ]
        for page in pages:
            response = self.client.get(f'/toolkit/{page}/{self.patient.pk}')
            self.assertEqual(response.status_code, 200)

