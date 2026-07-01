from django.contrib import admin

from ..models import AttributeValue

class AttributeValueInline(admin.TabularInline):
    model = AttributeValue
    extra = 1