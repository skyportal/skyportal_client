
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
from skyportal-client.acls_api import AclsApi
from skyportal-client.allocations_api import AllocationsApi
from skyportal-client.annotations_api import AnnotationsApi
from skyportal-client.assignments_api import AssignmentsApi
from skyportal-client.candidates_api import CandidatesApi
from skyportal-client.classifications_api import ClassificationsApi
from skyportal-client.comments_api import CommentsApi
from skyportal-client.data_sharing_api import DataSharingApi
from skyportal-client.default_api import DefaultApi
from skyportal-client.facility_api import FacilityApi
from skyportal-client.filters_api import FiltersApi
from skyportal-client.followup_requests_api import FollowupRequestsApi
from skyportal-client.group_admission_requests_api import GroupAdmissionRequestsApi
from skyportal-client.groups_api import GroupsApi
from skyportal-client.instruments_api import InstrumentsApi
from skyportal-client.invitations_api import InvitationsApi
from skyportal-client.lab_api import LabApi
from skyportal-client.news_feed_api import NewsFeedApi
from skyportal-client.notifications_api import NotificationsApi
from skyportal-client.observing_runs_api import ObservingRunsApi
from skyportal-client.photometry_api import PhotometryApi
from skyportal-client.roles_api import RolesApi
from skyportal-client.sources_api import SourcesApi
from skyportal-client.spectra_api import SpectraApi
from skyportal-client.streams_api import StreamsApi
from skyportal-client.system_info_api import SystemInfoApi
from skyportal-client.taxonomies_api import TaxonomiesApi
from skyportal-client.telescopes_api import TelescopesApi
from skyportal-client.thumbnails_api import ThumbnailsApi
from skyportal-client.users_api import UsersApi
from skyportal-client.weather_api import WeatherApi
