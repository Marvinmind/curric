from django.contrib import admin
from plan.models import *
# Register your models here.

class SectionAdmin(admin.ModelAdmin):
    filter_horizontal = ('modules',)
    filter_horizontal = ('exclusive_subsections', 'mandatory_subsections')
admin.site.register(Studyplan)
admin.site.register(ModuleSelections)
admin.site.register(Section, SectionAdmin)
admin.site.register(Module)