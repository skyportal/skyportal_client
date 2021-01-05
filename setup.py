"""
    Fritz: SkyPortal API

    SkyPortal provides an API to access most of its underlying functionality. To use it, you will need an API token. This can be generated via the web application from your profile page or, if you are an admin, you may use the system provisioned token stored inside of `.tokens.yaml`.  ### Accessing the SkyPortal API  Once you have a token, you may access SkyPortal programmatically as follows.  #### Python  ```python import requests  token = 'ea70a5f0-b321-43c6-96a1-b2de225e0339'  def api(method, endpoint, data=None):     headers = {'Authorization': f'token {token}'}     response = requests.request(method, endpoint, json=data, headers=headers)     return response  response = api('GET', 'http://localhost:5000/api/sysinfo')  print(f'HTTP code: {response.status_code}, {response.reason}') if response.status_code in (200, 400):     print(f'JSON response: {response.json()}') ```  #### Command line (curl)  ```shell curl -s -H 'Authorization: token ea70a5f0-b321-43c6-96a1-b2de225e0339' http://localhost:5000/api/sysinfo ```  ### Response  In the above examples, the SkyPortal server is located at `http://localhost:5000`. In case of success, the HTTP response is 200:  ``` HTTP code: 200, OK JSON response: {'status': 'success', 'data': {}, 'version': '0.9.dev0+git20200819.84c453a'} ```  On failure, it is 400; the JSON response has `status=\"error\"` with the reason for the failure given in `message`:  ```js {   \"status\": \"error\",   \"message\": \"Invalid API endpoint\",   \"data\": {},   \"version\": \"0.9.1\" } ```  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 0.9.dev0+git20201221.76627dd
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "skyportal-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = [
  "urllib3 >= 1.25.3",
  "python-dateutil",
  "nulltype",
]

setup(
    name=NAME,
    version=VERSION,
    description="Fritz: SkyPortal API",
    author="OpenAPI Generator community",
    author_email="team@openapitools.org",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Fritz: SkyPortal API"],
    python_requires=">=3.6",
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    SkyPortal provides an API to access most of its underlying functionality. To use it, you will need an API token. This can be generated via the web application from your profile page or, if you are an admin, you may use the system provisioned token stored inside of &#x60;.tokens.yaml&#x60;.  ### Accessing the SkyPortal API  Once you have a token, you may access SkyPortal programmatically as follows.  #### Python  &#x60;&#x60;&#x60;python import requests  token &#x3D; &#39;ea70a5f0-b321-43c6-96a1-b2de225e0339&#39;  def api(method, endpoint, data&#x3D;None):     headers &#x3D; {&#39;Authorization&#39;: f&#39;token {token}&#39;}     response &#x3D; requests.request(method, endpoint, json&#x3D;data, headers&#x3D;headers)     return response  response &#x3D; api(&#39;GET&#39;, &#39;http://localhost:5000/api/sysinfo&#39;)  print(f&#39;HTTP code: {response.status_code}, {response.reason}&#39;) if response.status_code in (200, 400):     print(f&#39;JSON response: {response.json()}&#39;) &#x60;&#x60;&#x60;  #### Command line (curl)  &#x60;&#x60;&#x60;shell curl -s -H &#39;Authorization: token ea70a5f0-b321-43c6-96a1-b2de225e0339&#39; http://localhost:5000/api/sysinfo &#x60;&#x60;&#x60;  ### Response  In the above examples, the SkyPortal server is located at &#x60;http://localhost:5000&#x60;. In case of success, the HTTP response is 200:  &#x60;&#x60;&#x60; HTTP code: 200, OK JSON response: {&#39;status&#39;: &#39;success&#39;, &#39;data&#39;: {}, &#39;version&#39;: &#39;0.9.dev0+git20200819.84c453a&#39;} &#x60;&#x60;&#x60;  On failure, it is 400; the JSON response has &#x60;status&#x3D;\&quot;error\&quot;&#x60; with the reason for the failure given in &#x60;message&#x60;:  &#x60;&#x60;&#x60;js {   \&quot;status\&quot;: \&quot;error\&quot;,   \&quot;message\&quot;: \&quot;Invalid API endpoint\&quot;,   \&quot;data\&quot;: {},   \&quot;version\&quot;: \&quot;0.9.1\&quot; } &#x60;&#x60;&#x60;  # Authentication  &lt;!-- ReDoc-Inject: &lt;security-definitions&gt; --&gt;  # noqa: E501
    """
)