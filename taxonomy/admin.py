from django.contrib import admin
from .models import (Taxonomy,
                     TaxonomyType)

# Register your models here.

admin.site.register(Taxonomy)
admin.site.register(TaxonomyType)
