import logging
from django.test import Client, TestCase

# logger object
logger = logging.getLogger(__name__)


class {{class_name}}(TestCase):
    def setUp(self):
        """
            Called before every test function to set up any objects that may be modified by the test
        """
        self.client = Client()
        self.url = ""  # api url
        self.token = "<auth token>"

    def test_auth(self):
        """
            Test authentication without/expired/invalid header in token
        """
        test_post_data = {
            # add post data here
        }
        response = self.client.post(
            self.url, content_type="application/json", data=test_post_data)
        logger.info("AuthJsonResponse %s", response.json())
        self.assertEqual(response.status_code, 401)

    def test_success(self):
        """
            SUCCESS/200/201/OK testcases
        """
        test_post_data = {
            # add post data here
        }
        response = self.client.put(self.url, data=test_post_data, **{
                              "HTTP_AUTHORIZATION": f"Bearer {self.token}"}, content_type="application/json")
        response = response.json()
        logger.info("Json OK Response  %s", response.json())
        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response, {})

    def test_not_found(self):
        """
            NOT_FOUND/404 testcases
        """
        test_post_data = {
            # add post data here
        }
        response = self.client.put(self.url, data=test_post_data, **{
                              "HTTP_AUTHORIZATION": f"Bearer {self.token}"}, content_type="application/json")
        response = response.json()
        logger.info("Json OK Response  %s", response.json())
        self.assertEqual(response.status_code, 404)
        self.assertDictEqual(response, {"message": "", "error": "NOT_FOUND"})

    def test_not_found(self):
        """
            BAD_REQUEST/400 testcases
        """
        test_post_data = {
            # add post data here
        }
        response = self.client.put(self.url, data=test_post_data, **{
                              "HTTP_AUTHORIZATION": f"Bearer {self.token}"}, content_type="application/json")
        response = response.json()
        logger.info("Json OK Response  %s", response.json())
        self.assertEqual(response.status_code, 400)
        self.assertDictEqual(response, {"message": "", "error": "BAD_REQUEST"})

    def test_conflict(self):
        """
            CONFLICT/409 testcases
        """
        test_post_data = {
            # add post data here
        }
        response = self.client.put(self.url, data=test_post_data, **{
                              "HTTP_AUTHORIZATION": f"Bearer {self.token}"}, content_type="application/json")
        response = response.json()
        self.assertEqual(response.status_code, 409)
        self.assertDictEqual(
            response, {"message": "", "error": "CONFLICTING_DATA"})
