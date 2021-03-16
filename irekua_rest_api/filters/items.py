import django_filters

from irekua_database.models import Item
from .utils import BaseFilter


search_fields = ("item_type__name",)


class Filter(BaseFilter):
    is_uploaded = django_filters.BooleanFilter(
        field_name="item_file", method="is_uploaded_filter", label="is uploaded"
    )

    def is_uploaded_filter(self, queryset, name, value):
        return queryset.filter(item_file__isnull=value)

    class Meta:
        model = Item
        fields = {
            #  Item filters
            "item_type": ["exact"],
            "item_type__name": ["exact", "icontains"],
            # Deployment filters
            "sampling_event_device": ["exact"],
            "sampling_event_device__latitude": ["exact", "lt", "lte", "gt", "gte"],
            "sampling_event_device__altitude": ["exact", "lt", "lte", "gt", "gte"],
            "sampling_event_device__longitude": ["exact", "lt", "lte", "gt", "gte"],
            "sampling_event_device__deployed_on": ["exact", "lt", "lte", "gt", "gte"],
            "sampling_event_device__recovered_on": ["exact", "lt", "lte", "gt", "gte"],
            # Sampling Event filters
            "sampling_event_device__sampling_event": ["exact"],
            "sampling_event_device__sampling_event__sampling_event_type": ["exact"],
            "sampling_event_device__sampling_event__sampling_event_type__name": [
                "exact",
                "icontains",
            ],
            "sampling_event_device__sampling_event__started_on": [
                "exact",
                "lt",
                "lte",
                "gt",
                "gte",
            ],
            "sampling_event_device__sampling_event__ended_on": [
                "exact",
                "lt",
                "lte",
                "gt",
                "gte",
            ],
            #  Collection Site filters
            "sampling_event_device__sampling_event__collection_site": ["exact"],
            "sampling_event_device__sampling_event__collection_site__internal_id": [
                "exact",
                "icontains",
            ],
            "sampling_event_device__sampling_event__collection_site__site_type": [
                "exact"
            ],
            "sampling_event_device__sampling_event__collection_site__site_type__name": [
                "exact",
                "icontains",
            ],
            #  Site Descriptors filters
            "sampling_event_device__sampling_event__collection_site__site_descriptors": [
                "exact"
            ],
            "sampling_event_device__sampling_event__collection_site__site_descriptors__descriptor_type": [
                "exact"
            ],
            "sampling_event_device__sampling_event__collection_site__site_descriptors__descriptor_type__name": [
                "exact",
                "icontains",
            ],
            "sampling_event_device__sampling_event__collection_site__site_descriptors__value": [
                "exact",
                "icontains",
            ],
            #  Site filters
            "sampling_event_device__sampling_event__collection_site__site": ["exact"],
            "sampling_event_device__sampling_event__collection_site__site__latitude": [
                "exact",
                "lt",
                "gt",
                "lte",
                "gte",
            ],
            "sampling_event_device__sampling_event__collection_site__site__longitude": [
                "exact",
                "lt",
                "gt",
                "lte",
                "gte",
            ],
            "sampling_event_device__sampling_event__collection_site__site__altitude": [
                "exact",
                "lt",
                "gt",
                "lte",
                "gte",
            ],
            # Collection filters
            "sampling_event_device__sampling_event__collection": ["exact"],
            "sampling_event_device__sampling_event__collection__name": [
                "exact",
                "icontains",
            ],
            "sampling_event_device__sampling_event__collection__collection_type": [
                "exact"
            ],
            "sampling_event_device__sampling_event__collection__collection_type__name": [
                "exact",
                "icontains",
            ],
            "sampling_event_device__sampling_event__collection__institution": ["exact"],
            "sampling_event_device__sampling_event__collection__institution__institution_name": [
                "exact",
                "icontains",
            ],
            "sampling_event_device__sampling_event__collection__institution__institution_code": [
                "exact",
                "icontains",
            ],
            # Collection Device filters
            "sampling_event_device__collection_device": ["exact"],
            "sampling_event_device__collection_device__internal_id": [
                "exact",
                "icontains",
            ],
            #  Physical Device filters
            "sampling_event_device__collection_device__physical_device": ["exact"],
            "sampling_event_device__collection_device__physical_device__serial_number": [
                "exact",
                "icontains",
            ],
            "sampling_event_device__collection_device__physical_device__device__brand": [
                "exact"
            ],
            "sampling_event_device__collection_device__physical_device__device__brand__name": [
                "exact",
                "icontains",
            ],
            "sampling_event_device__collection_device__physical_device__device__model": [
                "exact",
                "icontains",
            ],
            "sampling_event_device__collection_device__physical_device__device__device_type": [
                "exact"
            ],
            "sampling_event_device__collection_device__physical_device__device__device_type__name": [
                "exact",
                "icontains",
            ],
            #  Annotation filters
            "annotation__labels": ["exact"],
            "annotation__labels__value": ["exact", "icontains"],
            "annotation__labels__term_type": ["exact"],
            "annotation__labels__term_type__name": ["exact", "icontains"],
            "annotation__annotation_type": ["exact"],
            "annotation__annotation_type__name": ["exact", "icontains"],
            #  User filters
            "created_by": ["exact"],
            "created_by__username": ["exact", "icontains"],
            "created_by__first_name": ["exact", "icontains"],
            "created_by__last_name": ["exact", "icontains"],
            "created_by__institution": ["exact"],
            "created_by__institution__institution_code": ["exact", "icontains"],
            "created_by__institution__institution_name": ["exact", "icontains"],
            # Date filters
            "created_on": ["exact", "lt", "lte", "gt", "gte"],
        }
