"""
    Fritz: SkyPortal API

    SkyPortal provides an API to access most of its underlying functionality. To use it, you will need an API token. This can be generated via the web application from your profile page or, if you are an admin, you may use the system provisioned token stored inside of `.tokens.yaml`.  ### Accessing the SkyPortal API  Once you have a token, you may access SkyPortal programmatically as follows.  #### Python  ```python import requests  token = 'ea70a5f0-b321-43c6-96a1-b2de225e0339'  def api(method, endpoint, data=None):     headers = {'Authorization': f'token {token}'}     response = requests.request(method, endpoint, json=data, headers=headers)     return response  response = api('GET', 'http://localhost:5000/api/sysinfo')  print(f'HTTP code: {response.status_code}, {response.reason}') if response.status_code in (200, 400):     print(f'JSON response: {response.json()}') ```  #### Command line (curl)  ```shell curl -s -H 'Authorization: token ea70a5f0-b321-43c6-96a1-b2de225e0339' http://localhost:5000/api/sysinfo ```  ### Response  In the above examples, the SkyPortal server is located at `http://localhost:5000`. In case of success, the HTTP response is 200:  ``` HTTP code: 200, OK JSON response: {'status': 'success', 'data': {}, 'version': '0.9.dev0+git20200819.84c453a'} ```  On failure, it is 400; the JSON response has `status=\"error\"` with the reason for the failure given in `message`:  ```js {   \"status\": \"error\",   \"message\": \"Invalid API endpoint\",   \"data\": {},   \"version\": \"0.9.1\" } ```  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 0.9.dev0+git20201221.76627dd
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import openapi_client
from openapi_client.model.observing_run_no_id import ObservingRunNoID
globals()['ObservingRunNoID'] = ObservingRunNoID
from openapi_client.model.single_observing_run_no_id import SingleObservingRunNoID


class TestSingleObservingRunNoID(unittest.TestCase):
    """SingleObservingRunNoID unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testSingleObservingRunNoID(self):
        """Test SingleObservingRunNoID"""
        # FIXME: construct object with mandatory attributes with example values
        # model = SingleObservingRunNoID()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
