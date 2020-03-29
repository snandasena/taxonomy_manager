from django.http import HttpResponse
from django.views.generic import View

from .models import Taxonomy


class TaxonomyDetailsView(View):
    @staticmethod
    def get(request, *args, **keywords):
        tx_id = keywords['id']
        data = Taxonomy.objects.get(id=tx_id)

        json_data = data.serialize()

        return HttpResponse(json_data, content_type="application/json")


class TaxonomyListView(View):
    @staticmethod
    def get(request, *args, **keywords):
        json_data = Taxonomy.objects.all().serialize()
        return HttpResponse(json_data, content_type="application/json")
