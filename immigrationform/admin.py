from django.contrib import admin

from .models import Question, FreeResponse, FreeResponseQuestion, MultiChoiceResponse, MultiChoiceQuestion, Answer, PolarQuestion, DocumentAttribute, DocumentAttrValue

# Register your models here.


class MultiChoiceInLine(admin.StackedInline):
    model = MultiChoiceResponse
    extra = 3


class MultiChoiceAdmin(admin.ModelAdmin):
    inlines = [MultiChoiceInLine]


class AttrInline(admin.StackedInline):
    model = DocumentAttrValue
    extra = 3


class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttrInline]


admin.site.register(MultiChoiceQuestion, MultiChoiceAdmin)
admin.site.register(DocumentAttribute, AttributeAdmin)
admin.site.register([DocumentAttrValue, Question, FreeResponseQuestion, PolarQuestion, Answer, FreeResponse, MultiChoiceResponse])