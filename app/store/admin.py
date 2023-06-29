from django.contrib import admin
from store.models import *


def get_model_fields(model, type_exclusion=['JSONField', 'TextField'], field_exclusion=[]):
    return [f.name for f in model._meta.fields if not (f.name in field_exclusion or f.get_internal_type() in type_exclusion)]


@admin.register(Application)
class UserAdmin(admin.ModelAdmin):
    list_display = get_model_fields(
        Application, type_exclusion=[], field_exclusion=[])
    search_fields = ('name', 'developer__phone')
