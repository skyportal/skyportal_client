"""
    Fritz: SkyPortal API

    SkyPortal provides an API to access most of its underlying functionality. To use it, you will need an API token. This can be generated via the web application from your profile page or, if you are an admin, you may use the system provisioned token stored inside of `.tokens.yaml`.  ### Accessing the SkyPortal API  Once you have a token, you may access SkyPortal programmatically as follows.  #### Python  ```python import requests  token = 'ea70a5f0-b321-43c6-96a1-b2de225e0339'  def api(method, endpoint, data=None):     headers = {'Authorization': f'token {token}'}     response = requests.request(method, endpoint, json=data, headers=headers)     return response  response = api('GET', 'http://localhost:5000/api/sysinfo')  print(f'HTTP code: {response.status_code}, {response.reason}') if response.status_code in (200, 400):     print(f'JSON response: {response.json()}') ```  #### Command line (curl)  ```shell curl -s -H 'Authorization: token ea70a5f0-b321-43c6-96a1-b2de225e0339' http://localhost:5000/api/sysinfo ```  ### Response  In the above examples, the SkyPortal server is located at `http://localhost:5000`. In case of success, the HTTP response is 200:  ``` HTTP code: 200, OK JSON response: {'status': 'success', 'data': {}, 'version': '0.9.dev0+git20200819.84c453a'} ```  On failure, it is 400; the JSON response has `status=\"error\"` with the reason for the failure given in `message`:  ```js {   \"status\": \"error\",   \"message\": \"Invalid API endpoint\",   \"data\": {},   \"version\": \"0.9.1\" } ```  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 0.9.dev0+git20201221.76627dd
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from skyportal_client.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
)


class PhotometryMag(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('filter',): {
            'BESSELLUX': "bessellux",
            'BESSELLB': "bessellb",
            'BESSELLV': "bessellv",
            'BESSELLR': "bessellr",
            'BESSELLI': "besselli",
            'STANDARD::U': "standard::u",
            'STANDARD::B': "standard::b",
            'STANDARD::V': "standard::v",
            'STANDARD::R': "standard::r",
            'STANDARD::I': "standard::i",
            'DESG': "desg",
            'DESR': "desr",
            'DESI': "desi",
            'DESZ': "desz",
            'DESY': "desy",
            'SDSSU': "sdssu",
            'SDSSG': "sdssg",
            'SDSSR': "sdssr",
            'SDSSI': "sdssi",
            'SDSSZ': "sdssz",
            'F435W': "f435w",
            'F475W': "f475w",
            'F555W': "f555w",
            'F606W': "f606w",
            'F625W': "f625w",
            'F775W': "f775w",
            'F850LP': "f850lp",
            'NICF110W': "nicf110w",
            'NICF160W': "nicf160w",
            'F098M': "f098m",
            'F105W': "f105w",
            'F110W': "f110w",
            'F125W': "f125w",
            'F127M': "f127m",
            'F139M': "f139m",
            'F140W': "f140w",
            'F153M': "f153m",
            'F160W': "f160w",
            'F218W': "f218w",
            'F225W': "f225w",
            'F275W': "f275w",
            'F300X': "f300x",
            'F336W': "f336w",
            'F350LP': "f350lp",
            'F390W': "f390w",
            'F689M': "f689m",
            'F763M': "f763m",
            'F845M': "f845m",
            'F438W': "f438w",
            'UVF475W': "uvf475w",
            'UVF555W': "uvf555w",
            'UVF606W': "uvf606w",
            'UVF625W': "uvf625w",
            'UVF775W': "uvf775w",
            'UVF814W': "uvf814w",
            'UVF850LP': "uvf850lp",
            'KEPLER': "kepler",
            'CSPB': "cspb",
            'CSPHS': "csphs",
            'CSPHD': "csphd",
            'CSPJS': "cspjs",
            'CSPJD': "cspjd",
            'CSPV3009': "cspv3009",
            'CSPV3014': "cspv3014",
            'CSPV9844': "cspv9844",
            'CSPYS': "cspys",
            'CSPYD': "cspyd",
            'CSPG': "cspg",
            'CSPI': "cspi",
            'CSPK': "cspk",
            'CSPR': "cspr",
            'CSPU': "cspu",
            'F070W': "f070w",
            'F090W': "f090w",
            'F115W': "f115w",
            'F150W': "f150w",
            'F200W': "f200w",
            'F277W': "f277w",
            'F356W': "f356w",
            'F444W': "f444w",
            'F140M': "f140m",
            'F162M': "f162m",
            'F182M': "f182m",
            'F210M': "f210m",
            'F250M': "f250m",
            'F300M': "f300m",
            'F335M': "f335m",
            'F360M': "f360m",
            'F410M': "f410m",
            'F430M': "f430m",
            'F460M': "f460m",
            'F480M': "f480m",
            'F560W': "f560w",
            'F770W': "f770w",
            'F1000W': "f1000w",
            'F1130W': "f1130w",
            'F1280W': "f1280w",
            'F1500W': "f1500w",
            'F1800W': "f1800w",
            'F2100W': "f2100w",
            'F2550W': "f2550w",
            'F1065C': "f1065c",
            'F1140C': "f1140c",
            'F1550C': "f1550c",
            'F2300C': "f2300c",
            'LSSTU': "lsstu",
            'LSSTG': "lsstg",
            'LSSTR': "lsstr",
            'LSSTI': "lssti",
            'LSSTZ': "lsstz",
            'LSSTY': "lssty",
            'KEPLERCAM::US': "keplercam::us",
            'KEPLERCAM::B': "keplercam::b",
            'KEPLERCAM::V': "keplercam::v",
            'KEPLERCAM::R': "keplercam::r",
            'KEPLERCAM::I': "keplercam::i",
            '4SHOOTER2::US': "4shooter2::us",
            '4SHOOTER2::B': "4shooter2::b",
            '4SHOOTER2::V': "4shooter2::v",
            '4SHOOTER2::R': "4shooter2::r",
            '4SHOOTER2::I': "4shooter2::i",
            'ZTFG': "ztfg",
            'ZTFR': "ztfr",
            'ZTFI': "ztfi",
            'UVOT::B': "uvot::b",
            'UVOT::U': "uvot::u",
            'UVOT::UVM2': "uvot::uvm2",
            'UVOT::UVW1': "uvot::uvw1",
            'UVOT::UVW2': "uvot::uvw2",
            'UVOT::V': "uvot::v",
            'UVOT::WHITE': "uvot::white",
        },
        ('magsys',): {
            'JLA1': "jla1",
            'AB': "ab",
            'VEGA': "vega",
            'BD17': "bd17",
            'CSP': "csp",
            'AB-B12': "ab-b12",
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'instrument_id': (int,),  # noqa: E501
            'filter': (str,),  # noqa: E501
            'mjd': (float,),  # noqa: E501
            'limiting_mag': (float,),  # noqa: E501
            'obj_id': (str,),  # noqa: E501
            'magsys': (str,),  # noqa: E501
            'ra': (float, none_type,),  # noqa: E501
            'dec_unc': (float, none_type,),  # noqa: E501
            'magerr': (float, none_type,),  # noqa: E501
            'altdata': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'assignment_id': (int, none_type,),  # noqa: E501
            'mag': (float, none_type,),  # noqa: E501
            'dec': (float, none_type,),  # noqa: E501
            'alert_id': (int, none_type,),  # noqa: E501
            'ra_unc': (float, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'instrument_id': 'instrument_id',  # noqa: E501
        'filter': 'filter',  # noqa: E501
        'mjd': 'mjd',  # noqa: E501
        'limiting_mag': 'limiting_mag',  # noqa: E501
        'obj_id': 'obj_id',  # noqa: E501
        'magsys': 'magsys',  # noqa: E501
        'ra': 'ra',  # noqa: E501
        'dec_unc': 'dec_unc',  # noqa: E501
        'magerr': 'magerr',  # noqa: E501
        'altdata': 'altdata',  # noqa: E501
        'assignment_id': 'assignment_id',  # noqa: E501
        'mag': 'mag',  # noqa: E501
        'dec': 'dec',  # noqa: E501
        'alert_id': 'alert_id',  # noqa: E501
        'ra_unc': 'ra_unc',  # noqa: E501
    }

    _composed_schemas = {}

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, instrument_id, filter, mjd, limiting_mag, obj_id, magsys, *args, **kwargs):  # noqa: E501
        """PhotometryMag - a model defined in OpenAPI

        Args:
            instrument_id (int): ID of the instrument with which the observation was carried out.
            filter (str): The bandpass of the observation.
            mjd (float): MJD of the observation.
            limiting_mag (float): Limiting magnitude of the image in the magnitude system `magsys`.
            obj_id (str): ID of the Object to which the photometry will be attached.
            magsys (str): The magnitude system to which the flux and the zeropoint are tied.

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            ra (float, none_type): ICRS Right Ascension of the centroid of the photometric aperture [deg].. [optional]  # noqa: E501
            dec_unc (float, none_type): Uncertainty on dec [arcsec].. [optional]  # noqa: E501
            magerr (float, none_type): Magnitude error of the observation in the magnitude system `magsys`. Can be null in the case of a non-detection.. [optional]  # noqa: E501
            altdata ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Misc. alternative metadata stored in JSON format, e.g. `{'calibration': {'source': 'ps1', 'color_term': 0.012}, 'photometry_method': 'allstar', 'method_reference': 'Masci et al. (2015)'}`. [optional]  # noqa: E501
            assignment_id (int, none_type): ID of the classical assignment which generated the photometry. [optional]  # noqa: E501
            mag (float, none_type): Magnitude of the observation in the magnitude system `magsys`. Can be null in the case of a non-detection.. [optional]  # noqa: E501
            dec (float, none_type): ICRS Declination of the centroid of the photometric aperture [deg].. [optional]  # noqa: E501
            alert_id (int, none_type): Corresponding alert ID. If a record is already present with identical alert ID, only the groups list will be updated (other alert data assumed identical). Defaults to None.. [optional]  # noqa: E501
            ra_unc (float, none_type): Uncertainty on RA [arcsec].. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        self.instrument_id = instrument_id
        self.filter = filter
        self.mjd = mjd
        self.limiting_mag = limiting_mag
        self.obj_id = obj_id
        self.magsys = magsys
        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
