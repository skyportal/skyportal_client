# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from skyportal_client.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from skyportal_client.model.acl import ACL
from skyportal_client.model.allocation import Allocation
from skyportal_client.model.allocation_no_id import AllocationNoID
from skyportal_client.model.annotation import Annotation
from skyportal_client.model.annotation_no_id import AnnotationNoID
from skyportal_client.model.api_comment_attachment import ApiCommentAttachment
from skyportal_client.model.array_of_acl_no_i_ds import ArrayOfACLNoIDs
from skyportal_client.model.array_of_ac_ls import ArrayOfACLs
from skyportal_client.model.array_of_allocation_no_i_ds import ArrayOfAllocationNoIDs
from skyportal_client.model.array_of_allocations import ArrayOfAllocations
from skyportal_client.model.array_of_annotation_no_i_ds import ArrayOfAnnotationNoIDs
from skyportal_client.model.array_of_annotations import ArrayOfAnnotations
from skyportal_client.model.array_of_assignment_schemas import ArrayOfAssignmentSchemas
from skyportal_client.model.array_of_association_no_i_ds import ArrayOfAssociationNoIDs
from skyportal_client.model.array_of_associations import ArrayOfAssociations
from skyportal_client.model.array_of_candidate_no_i_ds import ArrayOfCandidateNoIDs
from skyportal_client.model.array_of_candidates import ArrayOfCandidates
from skyportal_client.model.array_of_classical_assignment_no_i_ds import ArrayOfClassicalAssignmentNoIDs
from skyportal_client.model.array_of_classical_assignments import ArrayOfClassicalAssignments
from skyportal_client.model.array_of_classification_no_i_ds import ArrayOfClassificationNoIDs
from skyportal_client.model.array_of_classifications import ArrayOfClassifications
from skyportal_client.model.array_of_code_no_i_ds import ArrayOfCodeNoIDs
from skyportal_client.model.array_of_codes import ArrayOfCodes
from skyportal_client.model.array_of_comment_no_i_ds import ArrayOfCommentNoIDs
from skyportal_client.model.array_of_comments import ArrayOfComments
from skyportal_client.model.array_of_errors import ArrayOfErrors
from skyportal_client.model.array_of_facility_transaction_no_i_ds import ArrayOfFacilityTransactionNoIDs
from skyportal_client.model.array_of_facility_transactions import ArrayOfFacilityTransactions
from skyportal_client.model.array_of_filter_no_i_ds import ArrayOfFilterNoIDs
from skyportal_client.model.array_of_filters import ArrayOfFilters
from skyportal_client.model.array_of_followup_request_group_no_i_ds import ArrayOfFollowupRequestGroupNoIDs
from skyportal_client.model.array_of_followup_request_groups import ArrayOfFollowupRequestGroups
from skyportal_client.model.array_of_followup_request_no_i_ds import ArrayOfFollowupRequestNoIDs
from skyportal_client.model.array_of_followup_request_posts import ArrayOfFollowupRequestPosts
from skyportal_client.model.array_of_followup_requests import ArrayOfFollowupRequests
from skyportal_client.model.array_of_group_admission_request_no_i_ds import ArrayOfGroupAdmissionRequestNoIDs
from skyportal_client.model.array_of_group_admission_requests import ArrayOfGroupAdmissionRequests
from skyportal_client.model.array_of_group_annotation_no_i_ds import ArrayOfGroupAnnotationNoIDs
from skyportal_client.model.array_of_group_annotations import ArrayOfGroupAnnotations
from skyportal_client.model.array_of_group_classification_no_i_ds import ArrayOfGroupClassificationNoIDs
from skyportal_client.model.array_of_group_classifications import ArrayOfGroupClassifications
from skyportal_client.model.array_of_group_comment_no_i_ds import ArrayOfGroupCommentNoIDs
from skyportal_client.model.array_of_group_comments import ArrayOfGroupComments
from skyportal_client.model.array_of_group_id_lists import ArrayOfGroupIDLists
from skyportal_client.model.array_of_group_invitation_no_i_ds import ArrayOfGroupInvitationNoIDs
from skyportal_client.model.array_of_group_invitations import ArrayOfGroupInvitations
from skyportal_client.model.array_of_group_no_i_ds import ArrayOfGroupNoIDs
from skyportal_client.model.array_of_group_obj_no_i_ds import ArrayOfGroupObjNoIDs
from skyportal_client.model.array_of_group_objs import ArrayOfGroupObjs
from skyportal_client.model.array_of_group_photometry_no_i_ds import ArrayOfGroupPhotometryNoIDs
from skyportal_client.model.array_of_group_photometrys import ArrayOfGroupPhotometrys
from skyportal_client.model.array_of_group_source_notification_no_i_ds import ArrayOfGroupSourceNotificationNoIDs
from skyportal_client.model.array_of_group_source_notifications import ArrayOfGroupSourceNotifications
from skyportal_client.model.array_of_group_spectrum_no_i_ds import ArrayOfGroupSpectrumNoIDs
from skyportal_client.model.array_of_group_spectrums import ArrayOfGroupSpectrums
from skyportal_client.model.array_of_group_stream_no_i_ds import ArrayOfGroupStreamNoIDs
from skyportal_client.model.array_of_group_streams import ArrayOfGroupStreams
from skyportal_client.model.array_of_group_taxonomy_no_i_ds import ArrayOfGroupTaxonomyNoIDs
from skyportal_client.model.array_of_group_taxonomys import ArrayOfGroupTaxonomys
from skyportal_client.model.array_of_group_user_no_i_ds import ArrayOfGroupUserNoIDs
from skyportal_client.model.array_of_group_users import ArrayOfGroupUsers
from skyportal_client.model.array_of_groups import ArrayOfGroups
from skyportal_client.model.array_of_instrument_no_i_ds import ArrayOfInstrumentNoIDs
from skyportal_client.model.array_of_instruments import ArrayOfInstruments
from skyportal_client.model.array_of_invitation_no_i_ds import ArrayOfInvitationNoIDs
from skyportal_client.model.array_of_invitations import ArrayOfInvitations
from skyportal_client.model.array_of_nonce_no_i_ds import ArrayOfNonceNoIDs
from skyportal_client.model.array_of_nonces import ArrayOfNonces
from skyportal_client.model.array_of_obj_no_i_ds import ArrayOfObjNoIDs
from skyportal_client.model.array_of_objs import ArrayOfObjs
from skyportal_client.model.array_of_observing_run_get_with_assignmentss import ArrayOfObservingRunGetWithAssignmentss
from skyportal_client.model.array_of_observing_run_gets import ArrayOfObservingRunGets
from skyportal_client.model.array_of_observing_run_no_i_ds import ArrayOfObservingRunNoIDs
from skyportal_client.model.array_of_observing_run_posts import ArrayOfObservingRunPosts
from skyportal_client.model.array_of_observing_runs import ArrayOfObservingRuns
from skyportal_client.model.array_of_partial_no_i_ds import ArrayOfPartialNoIDs
from skyportal_client.model.array_of_partials import ArrayOfPartials
from skyportal_client.model.array_of_phot_flux_flexibles import ArrayOfPhotFluxFlexibles
from skyportal_client.model.array_of_phot_mag_flexibles import ArrayOfPhotMagFlexibles
from skyportal_client.model.array_of_photometry_fluxs import ArrayOfPhotometryFluxs
from skyportal_client.model.array_of_photometry_mags import ArrayOfPhotometryMags
from skyportal_client.model.array_of_photometry_no_i_ds import ArrayOfPhotometryNoIDs
from skyportal_client.model.array_of_photometry_range_querys import ArrayOfPhotometryRangeQuerys
from skyportal_client.model.array_of_photometrys import ArrayOfPhotometrys
from skyportal_client.model.array_of_responses import ArrayOfResponses
from skyportal_client.model.array_of_role_acl_no_i_ds import ArrayOfRoleACLNoIDs
from skyportal_client.model.array_of_role_ac_ls import ArrayOfRoleACLs
from skyportal_client.model.array_of_role_no_i_ds import ArrayOfRoleNoIDs
from skyportal_client.model.array_of_roles import ArrayOfRoles
from skyportal_client.model.array_of_source_notification_no_i_ds import ArrayOfSourceNotificationNoIDs
from skyportal_client.model.array_of_source_notifications import ArrayOfSourceNotifications
from skyportal_client.model.array_of_source_view_no_i_ds import ArrayOfSourceViewNoIDs
from skyportal_client.model.array_of_source_views import ArrayOfSourceViews
from skyportal_client.model.array_of_spectrum_ascii_file_parse_jso_ns import ArrayOfSpectrumAsciiFileParseJSONs
from skyportal_client.model.array_of_spectrum_ascii_file_post_jso_ns import ArrayOfSpectrumAsciiFilePostJSONs
from skyportal_client.model.array_of_spectrum_no_i_ds import ArrayOfSpectrumNoIDs
from skyportal_client.model.array_of_spectrum_posts import ArrayOfSpectrumPosts
from skyportal_client.model.array_of_spectrums import ArrayOfSpectrums
from skyportal_client.model.array_of_stream_invitation_no_i_ds import ArrayOfStreamInvitationNoIDs
from skyportal_client.model.array_of_stream_invitations import ArrayOfStreamInvitations
from skyportal_client.model.array_of_stream_no_i_ds import ArrayOfStreamNoIDs
from skyportal_client.model.array_of_stream_user_no_i_ds import ArrayOfStreamUserNoIDs
from skyportal_client.model.array_of_stream_users import ArrayOfStreamUsers
from skyportal_client.model.array_of_streams import ArrayOfStreams
from skyportal_client.model.array_of_taxonomy_no_i_ds import ArrayOfTaxonomyNoIDs
from skyportal_client.model.array_of_taxonomys import ArrayOfTaxonomys
from skyportal_client.model.array_of_telescope_no_i_ds import ArrayOfTelescopeNoIDs
from skyportal_client.model.array_of_telescopes import ArrayOfTelescopes
from skyportal_client.model.array_of_thumbnail_no_i_ds import ArrayOfThumbnailNoIDs
from skyportal_client.model.array_of_thumbnails import ArrayOfThumbnails
from skyportal_client.model.array_of_token_acl_no_i_ds import ArrayOfTokenACLNoIDs
from skyportal_client.model.array_of_token_ac_ls import ArrayOfTokenACLs
from skyportal_client.model.array_of_token_no_i_ds import ArrayOfTokenNoIDs
from skyportal_client.model.array_of_tokens import ArrayOfTokens
from skyportal_client.model.array_of_user_acl_no_i_ds import ArrayOfUserACLNoIDs
from skyportal_client.model.array_of_user_ac_ls import ArrayOfUserACLs
from skyportal_client.model.array_of_user_invitation_no_i_ds import ArrayOfUserInvitationNoIDs
from skyportal_client.model.array_of_user_invitations import ArrayOfUserInvitations
from skyportal_client.model.array_of_user_no_i_ds import ArrayOfUserNoIDs
from skyportal_client.model.array_of_user_role_no_i_ds import ArrayOfUserRoleNoIDs
from skyportal_client.model.array_of_user_roles import ArrayOfUserRoles
from skyportal_client.model.array_of_user_social_auth_no_i_ds import ArrayOfUserSocialAuthNoIDs
from skyportal_client.model.array_of_user_social_auths import ArrayOfUserSocialAuths
from skyportal_client.model.array_of_users import ArrayOfUsers
from skyportal_client.model.assignment_schema import AssignmentSchema
from skyportal_client.model.association import Association
from skyportal_client.model.association_no_id import AssociationNoID
from skyportal_client.model.candidate import Candidate
from skyportal_client.model.candidate_no_id import CandidateNoID
from skyportal_client.model.classical_assignment import ClassicalAssignment
from skyportal_client.model.classical_assignment_no_id import ClassicalAssignmentNoID
from skyportal_client.model.classification import Classification
from skyportal_client.model.classification_no_id import ClassificationNoID
from skyportal_client.model.code import Code
from skyportal_client.model.code_no_id import CodeNoID
from skyportal_client.model.comment import Comment
from skyportal_client.model.comment_no_id import CommentNoID
from skyportal_client.model.error import Error
from skyportal_client.model.facility_transaction import FacilityTransaction
from skyportal_client.model.facility_transaction_no_id import FacilityTransactionNoID
from skyportal_client.model.filter import Filter
from skyportal_client.model.filter_no_id import FilterNoID
from skyportal_client.model.followup_request import FollowupRequest
from skyportal_client.model.followup_request_group import FollowupRequestGroup
from skyportal_client.model.followup_request_group_no_id import FollowupRequestGroupNoID
from skyportal_client.model.followup_request_no_id import FollowupRequestNoID
from skyportal_client.model.followup_request_post import FollowupRequestPost
from skyportal_client.model.group import Group
from skyportal_client.model.group_admission_request import GroupAdmissionRequest
from skyportal_client.model.group_admission_request_no_id import GroupAdmissionRequestNoID
from skyportal_client.model.group_annotation import GroupAnnotation
from skyportal_client.model.group_annotation_no_id import GroupAnnotationNoID
from skyportal_client.model.group_classification import GroupClassification
from skyportal_client.model.group_classification_no_id import GroupClassificationNoID
from skyportal_client.model.group_comment import GroupComment
from skyportal_client.model.group_comment_no_id import GroupCommentNoID
from skyportal_client.model.group_id_list import GroupIDList
from skyportal_client.model.group_invitation import GroupInvitation
from skyportal_client.model.group_invitation_no_id import GroupInvitationNoID
from skyportal_client.model.group_no_id import GroupNoID
from skyportal_client.model.group_obj import GroupObj
from skyportal_client.model.group_obj_no_id import GroupObjNoID
from skyportal_client.model.group_photometry import GroupPhotometry
from skyportal_client.model.group_photometry_no_id import GroupPhotometryNoID
from skyportal_client.model.group_source_notification import GroupSourceNotification
from skyportal_client.model.group_source_notification_no_id import GroupSourceNotificationNoID
from skyportal_client.model.group_spectrum import GroupSpectrum
from skyportal_client.model.group_spectrum_no_id import GroupSpectrumNoID
from skyportal_client.model.group_stream import GroupStream
from skyportal_client.model.group_stream_no_id import GroupStreamNoID
from skyportal_client.model.group_taxonomy import GroupTaxonomy
from skyportal_client.model.group_taxonomy_no_id import GroupTaxonomyNoID
from skyportal_client.model.group_user import GroupUser
from skyportal_client.model.group_user_no_id import GroupUserNoID
from skyportal_client.model.inline_object import InlineObject
from skyportal_client.model.inline_object1 import InlineObject1
from skyportal_client.model.inline_object10 import InlineObject10
from skyportal_client.model.inline_object11 import InlineObject11
from skyportal_client.model.inline_object12 import InlineObject12
from skyportal_client.model.inline_object13 import InlineObject13
from skyportal_client.model.inline_object14 import InlineObject14
from skyportal_client.model.inline_object15 import InlineObject15
from skyportal_client.model.inline_object16 import InlineObject16
from skyportal_client.model.inline_object17 import InlineObject17
from skyportal_client.model.inline_object18 import InlineObject18
from skyportal_client.model.inline_object19 import InlineObject19
from skyportal_client.model.inline_object2 import InlineObject2
from skyportal_client.model.inline_object20 import InlineObject20
from skyportal_client.model.inline_object21 import InlineObject21
from skyportal_client.model.inline_object22 import InlineObject22
from skyportal_client.model.inline_object3 import InlineObject3
from skyportal_client.model.inline_object4 import InlineObject4
from skyportal_client.model.inline_object5 import InlineObject5
from skyportal_client.model.inline_object6 import InlineObject6
from skyportal_client.model.inline_object7 import InlineObject7
from skyportal_client.model.inline_object8 import InlineObject8
from skyportal_client.model.inline_object9 import InlineObject9
from skyportal_client.model.inline_response200 import InlineResponse200
from skyportal_client.model.instrument import Instrument
from skyportal_client.model.instrument_no_id import InstrumentNoID
from skyportal_client.model.invitation import Invitation
from skyportal_client.model.invitation_no_id import InvitationNoID
from skyportal_client.model.nonce import Nonce
from skyportal_client.model.nonce_no_id import NonceNoID
from skyportal_client.model.obj import Obj
from skyportal_client.model.obj_no_id import ObjNoID
from skyportal_client.model.observing_run import ObservingRun
from skyportal_client.model.observing_run_get import ObservingRunGet
from skyportal_client.model.observing_run_get_with_assignments import ObservingRunGetWithAssignments
from skyportal_client.model.observing_run_no_id import ObservingRunNoID
from skyportal_client.model.observing_run_post import ObservingRunPost
from skyportal_client.model.partial import Partial
from skyportal_client.model.partial_no_id import PartialNoID
from skyportal_client.model.phot_flux_flexible import PhotFluxFlexible
from skyportal_client.model.phot_mag_flexible import PhotMagFlexible
from skyportal_client.model.photometry import Photometry
from skyportal_client.model.photometry_flux import PhotometryFlux
from skyportal_client.model.photometry_mag import PhotometryMag
from skyportal_client.model.photometry_no_id import PhotometryNoID
from skyportal_client.model.photometry_range_query import PhotometryRangeQuery
from skyportal_client.model.response import Response
from skyportal_client.model.role import Role
from skyportal_client.model.role_acl import RoleACL
from skyportal_client.model.role_acl_no_id import RoleACLNoID
from skyportal_client.model.single_acl import SingleACL
from skyportal_client.model.single_acl_no_id import SingleACLNoID
from skyportal_client.model.single_allocation import SingleAllocation
from skyportal_client.model.single_allocation_no_id import SingleAllocationNoID
from skyportal_client.model.single_annotation import SingleAnnotation
from skyportal_client.model.single_annotation_no_id import SingleAnnotationNoID
from skyportal_client.model.single_assignment_schema import SingleAssignmentSchema
from skyportal_client.model.single_association import SingleAssociation
from skyportal_client.model.single_association_no_id import SingleAssociationNoID
from skyportal_client.model.single_candidate import SingleCandidate
from skyportal_client.model.single_candidate_no_id import SingleCandidateNoID
from skyportal_client.model.single_classical_assignment import SingleClassicalAssignment
from skyportal_client.model.single_classical_assignment_no_id import SingleClassicalAssignmentNoID
from skyportal_client.model.single_classification import SingleClassification
from skyportal_client.model.single_classification_no_id import SingleClassificationNoID
from skyportal_client.model.single_code import SingleCode
from skyportal_client.model.single_code_no_id import SingleCodeNoID
from skyportal_client.model.single_comment import SingleComment
from skyportal_client.model.single_comment_no_id import SingleCommentNoID
from skyportal_client.model.single_error import SingleError
from skyportal_client.model.single_facility_transaction import SingleFacilityTransaction
from skyportal_client.model.single_facility_transaction_no_id import SingleFacilityTransactionNoID
from skyportal_client.model.single_filter import SingleFilter
from skyportal_client.model.single_filter_no_id import SingleFilterNoID
from skyportal_client.model.single_followup_request import SingleFollowupRequest
from skyportal_client.model.single_followup_request_group import SingleFollowupRequestGroup
from skyportal_client.model.single_followup_request_group_no_id import SingleFollowupRequestGroupNoID
from skyportal_client.model.single_followup_request_no_id import SingleFollowupRequestNoID
from skyportal_client.model.single_followup_request_post import SingleFollowupRequestPost
from skyportal_client.model.single_group import SingleGroup
from skyportal_client.model.single_group_admission_request import SingleGroupAdmissionRequest
from skyportal_client.model.single_group_admission_request_no_id import SingleGroupAdmissionRequestNoID
from skyportal_client.model.single_group_annotation import SingleGroupAnnotation
from skyportal_client.model.single_group_annotation_no_id import SingleGroupAnnotationNoID
from skyportal_client.model.single_group_classification import SingleGroupClassification
from skyportal_client.model.single_group_classification_no_id import SingleGroupClassificationNoID
from skyportal_client.model.single_group_comment import SingleGroupComment
from skyportal_client.model.single_group_comment_no_id import SingleGroupCommentNoID
from skyportal_client.model.single_group_id_list import SingleGroupIDList
from skyportal_client.model.single_group_invitation import SingleGroupInvitation
from skyportal_client.model.single_group_invitation_no_id import SingleGroupInvitationNoID
from skyportal_client.model.single_group_no_id import SingleGroupNoID
from skyportal_client.model.single_group_obj import SingleGroupObj
from skyportal_client.model.single_group_obj_no_id import SingleGroupObjNoID
from skyportal_client.model.single_group_photometry import SingleGroupPhotometry
from skyportal_client.model.single_group_photometry_no_id import SingleGroupPhotometryNoID
from skyportal_client.model.single_group_source_notification import SingleGroupSourceNotification
from skyportal_client.model.single_group_source_notification_no_id import SingleGroupSourceNotificationNoID
from skyportal_client.model.single_group_spectrum import SingleGroupSpectrum
from skyportal_client.model.single_group_spectrum_no_id import SingleGroupSpectrumNoID
from skyportal_client.model.single_group_stream import SingleGroupStream
from skyportal_client.model.single_group_stream_no_id import SingleGroupStreamNoID
from skyportal_client.model.single_group_taxonomy import SingleGroupTaxonomy
from skyportal_client.model.single_group_taxonomy_no_id import SingleGroupTaxonomyNoID
from skyportal_client.model.single_group_user import SingleGroupUser
from skyportal_client.model.single_group_user_no_id import SingleGroupUserNoID
from skyportal_client.model.single_instrument import SingleInstrument
from skyportal_client.model.single_instrument_no_id import SingleInstrumentNoID
from skyportal_client.model.single_invitation import SingleInvitation
from skyportal_client.model.single_invitation_no_id import SingleInvitationNoID
from skyportal_client.model.single_nonce import SingleNonce
from skyportal_client.model.single_nonce_no_id import SingleNonceNoID
from skyportal_client.model.single_obj import SingleObj
from skyportal_client.model.single_obj_no_id import SingleObjNoID
from skyportal_client.model.single_observing_run import SingleObservingRun
from skyportal_client.model.single_observing_run_get import SingleObservingRunGet
from skyportal_client.model.single_observing_run_get_with_assignments import SingleObservingRunGetWithAssignments
from skyportal_client.model.single_observing_run_no_id import SingleObservingRunNoID
from skyportal_client.model.single_observing_run_post import SingleObservingRunPost
from skyportal_client.model.single_partial import SinglePartial
from skyportal_client.model.single_partial_no_id import SinglePartialNoID
from skyportal_client.model.single_phot_flux_flexible import SinglePhotFluxFlexible
from skyportal_client.model.single_phot_mag_flexible import SinglePhotMagFlexible
from skyportal_client.model.single_photometry import SinglePhotometry
from skyportal_client.model.single_photometry_flux import SinglePhotometryFlux
from skyportal_client.model.single_photometry_mag import SinglePhotometryMag
from skyportal_client.model.single_photometry_no_id import SinglePhotometryNoID
from skyportal_client.model.single_photometry_range_query import SinglePhotometryRangeQuery
from skyportal_client.model.single_response import SingleResponse
from skyportal_client.model.single_role import SingleRole
from skyportal_client.model.single_role_acl import SingleRoleACL
from skyportal_client.model.single_role_acl_no_id import SingleRoleACLNoID
from skyportal_client.model.single_role_no_id import SingleRoleNoID
from skyportal_client.model.single_source_notification import SingleSourceNotification
from skyportal_client.model.single_source_notification_no_id import SingleSourceNotificationNoID
from skyportal_client.model.single_source_view import SingleSourceView
from skyportal_client.model.single_source_view_no_id import SingleSourceViewNoID
from skyportal_client.model.single_spectrum import SingleSpectrum
from skyportal_client.model.single_spectrum_ascii_file_parse_json import SingleSpectrumAsciiFileParseJSON
from skyportal_client.model.single_spectrum_ascii_file_post_json import SingleSpectrumAsciiFilePostJSON
from skyportal_client.model.single_spectrum_no_id import SingleSpectrumNoID
from skyportal_client.model.single_spectrum_post import SingleSpectrumPost
from skyportal_client.model.single_stream import SingleStream
from skyportal_client.model.single_stream_invitation import SingleStreamInvitation
from skyportal_client.model.single_stream_invitation_no_id import SingleStreamInvitationNoID
from skyportal_client.model.single_stream_no_id import SingleStreamNoID
from skyportal_client.model.single_stream_user import SingleStreamUser
from skyportal_client.model.single_stream_user_no_id import SingleStreamUserNoID
from skyportal_client.model.single_taxonomy import SingleTaxonomy
from skyportal_client.model.single_taxonomy_no_id import SingleTaxonomyNoID
from skyportal_client.model.single_telescope import SingleTelescope
from skyportal_client.model.single_telescope_no_id import SingleTelescopeNoID
from skyportal_client.model.single_thumbnail import SingleThumbnail
from skyportal_client.model.single_thumbnail_no_id import SingleThumbnailNoID
from skyportal_client.model.single_token import SingleToken
from skyportal_client.model.single_token_acl import SingleTokenACL
from skyportal_client.model.single_token_acl_no_id import SingleTokenACLNoID
from skyportal_client.model.single_token_no_id import SingleTokenNoID
from skyportal_client.model.single_user import SingleUser
from skyportal_client.model.single_user_acl import SingleUserACL
from skyportal_client.model.single_user_acl_no_id import SingleUserACLNoID
from skyportal_client.model.single_user_invitation import SingleUserInvitation
from skyportal_client.model.single_user_invitation_no_id import SingleUserInvitationNoID
from skyportal_client.model.single_user_no_id import SingleUserNoID
from skyportal_client.model.single_user_role import SingleUserRole
from skyportal_client.model.single_user_role_no_id import SingleUserRoleNoID
from skyportal_client.model.single_user_social_auth import SingleUserSocialAuth
from skyportal_client.model.single_user_social_auth_no_id import SingleUserSocialAuthNoID
from skyportal_client.model.source_notification import SourceNotification
from skyportal_client.model.source_notification_no_id import SourceNotificationNoID
from skyportal_client.model.source_view import SourceView
from skyportal_client.model.source_view_no_id import SourceViewNoID
from skyportal_client.model.spectrum import Spectrum
from skyportal_client.model.spectrum_ascii_file_parse_json import SpectrumAsciiFileParseJSON
from skyportal_client.model.spectrum_ascii_file_post_json import SpectrumAsciiFilePostJSON
from skyportal_client.model.spectrum_no_id import SpectrumNoID
from skyportal_client.model.spectrum_post import SpectrumPost
from skyportal_client.model.stream import Stream
from skyportal_client.model.stream_invitation import StreamInvitation
from skyportal_client.model.stream_invitation_no_id import StreamInvitationNoID
from skyportal_client.model.stream_no_id import StreamNoID
from skyportal_client.model.stream_user import StreamUser
from skyportal_client.model.stream_user_no_id import StreamUserNoID
from skyportal_client.model.success import Success
from skyportal_client.model.taxonomy import Taxonomy
from skyportal_client.model.taxonomy_no_id import TaxonomyNoID
from skyportal_client.model.telescope import Telescope
from skyportal_client.model.telescope_no_id import TelescopeNoID
from skyportal_client.model.thumbnail import Thumbnail
from skyportal_client.model.thumbnail_no_id import ThumbnailNoID
from skyportal_client.model.token import Token
from skyportal_client.model.token_acl import TokenACL
from skyportal_client.model.token_acl_no_id import TokenACLNoID
from skyportal_client.model.token_no_id import TokenNoID
from skyportal_client.model.user import User
from skyportal_client.model.user_acl import UserACL
from skyportal_client.model.user_acl_no_id import UserACLNoID
from skyportal_client.model.user_invitation import UserInvitation
from skyportal_client.model.user_invitation_no_id import UserInvitationNoID
from skyportal_client.model.user_no_id import UserNoID
from skyportal_client.model.user_role import UserRole
from skyportal_client.model.user_role_no_id import UserRoleNoID
from skyportal_client.model.user_social_auth import UserSocialAuth
from skyportal_client.model.user_social_auth_no_id import UserSocialAuthNoID
