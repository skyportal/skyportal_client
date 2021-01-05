
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
from skyportal-client.api.acls_api import AclsApi
from skyportal-client.api.allocations_api import AllocationsApi
from skyportal-client.api.annotations_api import AnnotationsApi
from skyportal-client.api.assignments_api import AssignmentsApi
from skyportal-client.api.candidates_api import CandidatesApi
from skyportal-client.api.classifications_api import ClassificationsApi
from skyportal-client.api.comments_api import CommentsApi
from skyportal-client.api.data_sharing_api import DataSharingApi
from skyportal-client.api.default_api import DefaultApi
from skyportal-client.api.facility_api import FacilityApi
from skyportal-client.api.filters_api import FiltersApi
from skyportal-client.api.followup_requests_api import FollowupRequestsApi
from skyportal-client.api.group_admission_requests_api import GroupAdmissionRequestsApi
from skyportal-client.api.groups_api import GroupsApi
from skyportal-client.api.instruments_api import InstrumentsApi
from skyportal-client.api.invitations_api import InvitationsApi
from skyportal-client.api.lab_api import LabApi
from skyportal-client.api.news_feed_api import NewsFeedApi
from skyportal-client.api.notifications_api import NotificationsApi
from skyportal-client.api.observing_runs_api import ObservingRunsApi
from skyportal-client.api.photometry_api import PhotometryApi
from skyportal-client.api.roles_api import RolesApi
from skyportal-client.api.sources_api import SourcesApi
from skyportal-client.api.spectra_api import SpectraApi
from skyportal-client.api.streams_api import StreamsApi
from skyportal-client.api.system_info_api import SystemInfoApi
from skyportal-client.api.taxonomies_api import TaxonomiesApi
from skyportal-client.api.telescopes_api import TelescopesApi
from skyportal-client.api.thumbnails_api import ThumbnailsApi
from skyportal-client.api.users_api import UsersApi
from skyportal-client.api.weather_api import WeatherApi
