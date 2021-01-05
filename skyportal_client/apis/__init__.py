
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.acls_api import AclsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from skyportal_client.api.acls_api import AclsApi
from skyportal_client.api.allocations_api import AllocationsApi
from skyportal_client.api.annotations_api import AnnotationsApi
from skyportal_client.api.assignments_api import AssignmentsApi
from skyportal_client.api.candidates_api import CandidatesApi
from skyportal_client.api.classifications_api import ClassificationsApi
from skyportal_client.api.comments_api import CommentsApi
from skyportal_client.api.data_sharing_api import DataSharingApi
from skyportal_client.api.default_api import DefaultApi
from skyportal_client.api.facility_api import FacilityApi
from skyportal_client.api.filters_api import FiltersApi
from skyportal_client.api.followup_requests_api import FollowupRequestsApi
from skyportal_client.api.group_admission_requests_api import GroupAdmissionRequestsApi
from skyportal_client.api.groups_api import GroupsApi
from skyportal_client.api.instruments_api import InstrumentsApi
from skyportal_client.api.invitations_api import InvitationsApi
from skyportal_client.api.lab_api import LabApi
from skyportal_client.api.news_feed_api import NewsFeedApi
from skyportal_client.api.notifications_api import NotificationsApi
from skyportal_client.api.observing_runs_api import ObservingRunsApi
from skyportal_client.api.photometry_api import PhotometryApi
from skyportal_client.api.roles_api import RolesApi
from skyportal_client.api.sources_api import SourcesApi
from skyportal_client.api.spectra_api import SpectraApi
from skyportal_client.api.streams_api import StreamsApi
from skyportal_client.api.system_info_api import SystemInfoApi
from skyportal_client.api.taxonomies_api import TaxonomiesApi
from skyportal_client.api.telescopes_api import TelescopesApi
from skyportal_client.api.thumbnails_api import ThumbnailsApi
from skyportal_client.api.users_api import UsersApi
from skyportal_client.api.weather_api import WeatherApi
