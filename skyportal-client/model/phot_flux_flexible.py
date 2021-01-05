"""
    Fritz: SkyPortal API

    SkyPortal provides an API to access most of its underlying functionality. To use it, you will need an API token. This can be generated via the web application from your profile page or, if you are an admin, you may use the system provisioned token stored inside of `.tokens.yaml`.  ### Accessing the SkyPortal API  Once you have a token, you may access SkyPortal programmatically as follows.  #### Python  ```python import requests  token = 'ea70a5f0-b321-43c6-96a1-b2de225e0339'  def api(method, endpoint, data=None):     headers = {'Authorization': f'token {token}'}     response = requests.request(method, endpoint, json=data, headers=headers)     return response  response = api('GET', 'http://localhost:5000/api/sysinfo')  print(f'HTTP code: {response.status_code}, {response.reason}') if response.status_code in (200, 400):     print(f'JSON response: {response.json()}') ```  #### Command line (curl)  ```shell curl -s -H 'Authorization: token ea70a5f0-b321-43c6-96a1-b2de225e0339' http://localhost:5000/api/sysinfo ```  ### Response  In the above examples, the SkyPortal server is located at `http://localhost:5000`. In case of success, the HTTP response is 200:  ``` HTTP code: 200, OK JSON response: {'status': 'success', 'data': {}, 'version': '0.9.dev0+git20200819.84c453a'} ```  On failure, it is 400; the JSON response has `status=\"error\"` with the reason for the failure given in `message`:  ```js {   \"status\": \"error\",   \"message\": \"Invalid API endpoint\",   \"data\": {},   \"version\": \"0.9.1\" } ```  # Authentication  <!-- ReDoc-Inject: <security-definitions> -->  # noqa: E501

    The version of the OpenAPI document: 0.9.dev0+git20201221.76627dd
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

import nulltype  # noqa: F401

from skyportal-client.model_utils import (  # noqa: F401
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


class PhotFluxFlexible(ModelNormal):
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
            'instrument_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'filter': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'fluxerr': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'mjd': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'zp': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'obj_id': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'magsys': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ra': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'dec_unc': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'altdata': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'assignment_id': (int, none_type,),  # noqa: E501
            'origin': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'flux': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'group_ids': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'dec': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
            'ra_unc': (bool, date, datetime, dict, float, int, list, str, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'instrument_id': 'instrument_id',  # noqa: E501
        'filter': 'filter',  # noqa: E501
        'fluxerr': 'fluxerr',  # noqa: E501
        'mjd': 'mjd',  # noqa: E501
        'zp': 'zp',  # noqa: E501
        'obj_id': 'obj_id',  # noqa: E501
        'magsys': 'magsys',  # noqa: E501
        'ra': 'ra',  # noqa: E501
        'dec_unc': 'dec_unc',  # noqa: E501
        'altdata': 'altdata',  # noqa: E501
        'assignment_id': 'assignment_id',  # noqa: E501
        'origin': 'origin',  # noqa: E501
        'flux': 'flux',  # noqa: E501
        'group_ids': 'group_ids',  # noqa: E501
        'dec': 'dec',  # noqa: E501
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
    def __init__(self, instrument_id, filter, fluxerr, mjd, zp, obj_id, magsys, *args, **kwargs):  # noqa: E501
        """PhotFluxFlexible - a model defined in OpenAPI

        Args:
            instrument_id (bool, date, datetime, dict, float, int, list, str, none_type): ID of the `Instrument`(s) with which the photometry was acquired. Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values are not allowed.
            filter (bool, date, datetime, dict, float, int, list, str, none_type): The bandpass of the observation(s). Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values not allowed. Allowed values: `bessellux`, `bessellb`, `bessellv`, `bessellr`, `besselli`, `standard::u`, `standard::b`, `standard::v`, `standard::r`, `standard::i`, `desg`, `desr`, `desi`, `desz`, `desy`, `sdssu`, `sdssg`, `sdssr`, `sdssi`, `sdssz`, `f435w`, `f475w`, `f555w`, `f606w`, `f625w`, `f775w`, `f850lp`, `nicf110w`, `nicf160w`, `f098m`, `f105w`, `f110w`, `f125w`, `f127m`, `f139m`, `f140w`, `f153m`, `f160w`, `f218w`, `f225w`, `f275w`, `f300x`, `f336w`, `f350lp`, `f390w`, `f689m`, `f763m`, `f845m`, `f438w`, `uvf475w`, `uvf555w`, `uvf606w`, `uvf625w`, `uvf775w`, `uvf814w`, `uvf850lp`, `kepler`, `cspb`, `csphs`, `csphd`, `cspjs`, `cspjd`, `cspv3009`, `cspv3014`, `cspv9844`, `cspys`, `cspyd`, `cspg`, `cspi`, `cspk`, `cspr`, `cspu`, `f070w`, `f090w`, `f115w`, `f150w`, `f200w`, `f277w`, `f356w`, `f444w`, `f140m`, `f162m`, `f182m`, `f210m`, `f250m`, `f300m`, `f335m`, `f360m`, `f410m`, `f430m`, `f460m`, `f480m`, `f560w`, `f770w`, `f1000w`, `f1130w`, `f1280w`, `f1500w`, `f1800w`, `f2100w`, `f2550w`, `f1065c`, `f1140c`, `f1550c`, `f2300c`, `lsstu`, `lsstg`, `lsstr`, `lssti`, `lsstz`, `lssty`, `keplercam::us`, `keplercam::b`, `keplercam::v`, `keplercam::r`, `keplercam::i`, `4shooter2::us`, `4shooter2::b`, `4shooter2::v`, `4shooter2::r`, `4shooter2::i`, `ztfg`, `ztfr`, `ztfi`, `uvot::b`, `uvot::u`, `uvot::uvm2`, `uvot::uvw1`, `uvot::uvw2`, `uvot::v`, `uvot::white`
            fluxerr (bool, date, datetime, dict, float, int, list, str, none_type): Gaussian error on the flux in counts. Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values not allowed.
            mjd (bool, date, datetime, dict, float, int, list, str, none_type): MJD of the observation(s). Can be a given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values not allowed.
            zp (bool, date, datetime, dict, float, int, list, str, none_type): Magnitude zeropoint, given by `zp` in the equation `m = -2.5 log10(flux) + zp`. `m` is the magnitude of the object in the magnitude system `magsys`. Can be given as a scalar or a 1D list. Null values not allowed.
            obj_id (bool, date, datetime, dict, float, int, list, str, none_type): ID of the `Obj`(s) to which the photometry will be attached. Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values are not allowed.
            magsys (bool, date, datetime, dict, float, int, list, str, none_type): The magnitude system to which the flux, flux error, and the zeropoint are tied. Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values not allowed. Allowed values: `jla1`, `ab`, `vega`, `bd17`, `csp`, `ab-b12`

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
            ra (bool, date, datetime, dict, float, int, list, str, none_type): ICRS Right Ascension of the centroid of the photometric aperture [deg]. Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values allowed.. [optional]  # noqa: E501
            dec_unc (bool, date, datetime, dict, float, int, list, str, none_type): Uncertainty on dec [arcsec]. Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values allowed.. [optional]  # noqa: E501
            altdata (bool, date, datetime, dict, float, int, list, str, none_type): Misc. alternative metadata stored in JSON format, e.g. `{'calibration': {'source': 'ps1', 'color_term': 0.012}, 'photometry_method': 'allstar', 'method_reference': 'Masci et al. (2015)'}`. [optional]  # noqa: E501
            assignment_id (int, none_type): ID of the classical assignment which generated the photometry. [optional]  # noqa: E501
            origin (bool, date, datetime, dict, float, int, list, str, none_type): Provenance of the Photometry. If a record is already present with identical origin, only the groups list will be updated (other data assumed identical). Defaults to None.. [optional]  # noqa: E501
            flux (bool, date, datetime, dict, float, int, list, str, none_type): Flux of the observation(s) in counts. Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values allowed, to accommodate,e.g., upper limits from ZTF1, where flux is not provided for non-detections. For a given photometry point, if `flux` is null, `fluxerr` is used to derive a 5-sigma limiting magnitude when the photometry point is requested in magnitude space from the Photomety GET api.. [optional]  # noqa: E501
            group_ids (bool, date, datetime, dict, float, int, list, str, none_type): List of group IDs to which photometry points will be visible. If 'all', will be shared with site-wide public group (visible to all users who can view associated source).. [optional]  # noqa: E501
            dec (bool, date, datetime, dict, float, int, list, str, none_type): ICRS Declination of the centroid of the photometric aperture [deg]. Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values allowed.. [optional]  # noqa: E501
            ra_unc (bool, date, datetime, dict, float, int, list, str, none_type): Uncertainty on RA [arcsec]. Can be given as a scalar or a 1D list. If a scalar, will be broadcast to all values given as lists. Null values allowed.. [optional]  # noqa: E501
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
        self.fluxerr = fluxerr
        self.mjd = mjd
        self.zp = zp
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
