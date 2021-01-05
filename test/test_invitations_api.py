"""
    Fritz: SkyPortal API

    SkyPortal provides an API to access most of its underlying functionality. To use it, you will need an API token. This can be generated via the web application from your profile page or, if you are an admin, you may use the system provisioned token stored inside of `.tokens.yaml`.  ### Accessing the SkyPortal API  Once you have a token, you may access SkyPortal programmatically as follows.  #### Python  ```python import requests  token = 'ea70a5f0-b321-43c6-96a1-b2de225e0339'  def api(method, endpoint, data=None):     headers = {'Authorization': f'token {token}'}     response = requests.request(method, endpoint, json=data, headers=headers)     return response  response = api('GET', 'http://localhost:5000/api/sysinfo')  print(f'HTTP code: {response.status_code}, {response.reason}') if response.status_code in (200, 400):     print(f'JSON response: {response.json()}') ```  #### Command line (curl)  ```shell curl -s -H 'Authorization: token ea70a5f0-b321-43c6-96a1-b2de225e0339' http://localhost:5000/api/sysinfo ```  ### Response  In the above examples, the SkyPortal server is located at `http://localhost:5000`. In case of success, the HTTP response is 200:  ``` HTTP code: 200, OK JSON response: {'status': 'success', 'data': {}, 'version': '0.9.dev0+git20200819.84c453a'} ```  On failure, it is 400; the JSON response has `status=\"error\"` with the reason for the failure given in `message`:  ```js {   \"status\": \"error\",   \"message\": \"Invalid API endpoint\",   \"data\": {},   \"version\": \"0.9.1\" } ```  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 0.9.dev0+git20201221.76627dd
    Generated by: https://openapi-generator.tech
"""


import unittest

import openapi_client
from openapi_client.api.invitations_api import InvitationsApi  # noqa: E501


class TestInvitationsApi(unittest.TestCase):
    """InvitationsApi unit test stubs"""

    def setUp(self):
        self.api = InvitationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_invitations_get(self):
        """Test case for api_invitations_get

        """
        pass

    def test_api_invitations_invitation_id_delete(self):
        """Test case for api_invitations_invitation_id_delete

        """
        pass

    def test_api_invitations_invitation_id_patch(self):
        """Test case for api_invitations_invitation_id_patch

        """
        pass

    def test_api_invitations_post(self):
        """Test case for api_invitations_post

        """
        pass


if __name__ == '__main__':
    unittest.main()
