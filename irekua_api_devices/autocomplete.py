from dal import autocomplete

from irekua_devices.models import DeviceType
from irekua_devices.models import DeviceBrand
from irekua_devices.models import Device
from irekua_api_core.autocomplete import register_autocomplete


urlpatterns = []


@register_autocomplete(DeviceType, urlpatterns)
class DeviceTypesAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = DeviceType.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


@register_autocomplete(DeviceBrand, urlpatterns)
class DeviceBrandAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = DeviceBrand.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs


@register_autocomplete(Device, urlpatterns)
class DeviceAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Device.objects.all()

        if self.q:
            qs = qs.filter(model__istartswith=self.q)

        return qs
