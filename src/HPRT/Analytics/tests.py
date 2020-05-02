from PatientPortal.testing_utils import HPRTTestCase


class AnalyticsEndpointTests(HPRTTestCase):
    def test_access_analytics_home(self):
        response = self.client.get('/analytics/')
        self.assertEqual(response.status_code, 200)
