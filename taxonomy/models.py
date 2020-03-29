import json
from django.db import models

from django.core.serializers import serialize


# Create your models here.

class TaxonomyQuerySet(models.QuerySet):
    def serialize(self):
        qs = self
        data = list(map(lambda obj: json.loads(obj.serialize()), qs))
        return json.dumps(data)


class TaxonomyManager(models.Manager):
    def get_queryset(self):
        return TaxonomyQuerySet(self.model, using=self._db)


class TaxonomyType(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=100, null=False, unique=True)


class Taxonomy(models.Model):
    id = models.CharField(primary_key=True, null=False, max_length=10)
    name = models.CharField(null=False, unique=True, max_length=100)
    is_enabled = models.BooleanField(null=False)
    iab_code = models.CharField(null=True, max_length=10)
    type = models.ForeignKey(TaxonomyType, on_delete=models.CASCADE)

    objects = TaxonomyManager()

    def serialize(self):
        json_data = serialize("json", [self], fields=('name', 'is_enabled', 'iab_code', 'type'))
        stuct = json.loads(json_data)
        data = json.dumps(stuct[0]['fields'])
        return data
