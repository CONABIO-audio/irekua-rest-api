from rest_framework import routers
from irekua_rest_api import views


main_router = routers.DefaultRouter()
main_router.register(r"annotations", views.AnnotationViewSet)
main_router.register(r"collections", views.CollectionViewSet)
main_router.register(r"devices", views.DeviceViewSet)
main_router.register(r"items", views.ItemViewSet)
main_router.register(r"sampling_events", views.SamplingEventViewSet)
main_router.register(r"sites", views.SiteViewSet)
main_router.register(r"terms", views.TermTypeViewSet)
main_router.register(r"users", views.UserViewSet)

main_router.register(r"types/mime_types", views.MimeTypeViewSet)
main_router.register(r"types/annotation_types", views.AnnotationTypeViewSet)
main_router.register(r"types/collection_types", views.CollectionTypeViewSet)
main_router.register(r"types/device_types", views.DeviceTypeViewSet)
main_router.register(r"types/entailment_types", views.EntailmentTypeViewSet)
main_router.register(r"types/event_types", views.EventTypeViewSet)
main_router.register(r"types/item_types", views.ItemTypeViewSet)
main_router.register(r"types/licence_types", views.LicenceTypeViewSet)
main_router.register(
    r"types/sampling_event_type_device_types", views.SamplingEventTypeDeviceTypeViewSet
)
main_router.register(
    r"types/sampling_event_type_site_types", views.SamplingEventTypeSiteTypeViewSet
)
main_router.register(r"types/sampling_event_types", views.SamplingEventTypeViewSet)
main_router.register(r"types/site_types", views.SiteTypeViewSet)
main_router.register(
    r"types/collection_type_site_types", views.CollectionTypeSiteTypeViewSet
)
main_router.register(
    r"types/collection_type_administrators", views.CollectionTypeAdministratorViewSet
)
main_router.register(
    r"types/collection_type_annotation_types", views.CollectionTypeAnnotationTypeViewSet
)
main_router.register(
    r"types/collection_type_licence_types", views.CollectionTypeLicenceTypeViewSet
)
main_router.register(
    r"types/collection_type_sampling_event_types",
    views.CollectionTypeSamplingEventTypeViewSet,
)
main_router.register(
    r"types/collection_type_item_types", views.CollectionTypeItemTypeViewSet
)
main_router.register(
    r"types/collection_type_event_types", views.CollectionTypeEventTypeViewSet
)
main_router.register(
    r"types/collection_type_device_types", views.CollectionTypeDeviceTypeViewSet
)
main_router.register(r"types/collection_type_roles", views.CollectionTypeRoleViewSet)

main_router.register(r"additional/annotation_votes", views.AnnotationVoteViewSet)
main_router.register(r"additional/secondary_items", views.SecondaryItemViewSet)
# TODO: Remove when AnnotationTool migration from irekua-database to
# selia-annotator is complete.
# main_router.register(
#     r'additional/annotation_tools',
#     views.AnnotationToolViewSet)
main_router.register(r"additional/collection_devices", views.CollectionDeviceViewSet)
main_router.register(r"additional/collection_sites", views.CollectionSiteViewSet)
main_router.register(r"additional/collection_users", views.CollectionUserViewSet)
main_router.register(
    r"additional/collection_administrators", views.CollectionAdministratorViewSet
)
main_router.register(r"additional/device_brands", views.DeviceBrandViewSet)
main_router.register(r"additional/entailments", views.EntailmentViewSet)
main_router.register(r"additional/institutions", views.InstitutionViewSet)
main_router.register(r"additional/licences", views.LicenceViewSet)
main_router.register(r"additional/metacollections", views.MetaCollectionViewSet)
main_router.register(r"additional/physical_devices", views.PhysicalDeviceViewSet)
main_router.register(r"additional/roles", views.RoleViewSet)
main_router.register(r"additional/synonym_suggestions", views.SynonymSuggestionViewSet)
main_router.register(r"additional/synonyms", views.SynonymViewSet)
main_router.register(r"additional/tags", views.TagViewSet)
main_router.register(r"additional/term_suggestions", views.TermSuggestionViewSet)
main_router.register(r"additional/term_instances", views.TermViewSet)
main_router.register(
    r"additional/sampling_event_devices", views.SamplingEventDeviceViewSet
)

main_router.register(r"models/models", views.ModelViewSet)
main_router.register(r"models/model_versions", views.ModelVersionViewSet)
main_router.register(r"models/model_predictions", views.ModelPredictionViewSet)
