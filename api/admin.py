from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Mumin

# Register your models here.


class MuminResource(resources.ModelResource):
    class Meta:
        model = Mumin
        import_id_fields = ('its_id',)
        exclude = ('created', 'updated', 'is_hof')
        skip_unchanged = True
        report_skipped = False


class MuminAdmin(ImportExportModelAdmin):
    list_display = ['__str__', 'jamaat_id',
                    'its_id', 'is_hof', 'email', 'cell_number']
    list_filter = ['is_hof', 'updated', 'created', 'jamaat_id', 'hof_its_id']
    search_fields = ['its_id', 'jamaat_id', 'first_name', 'last_name']
    resource_class = MuminResource


admin.site.register(Mumin, MuminAdmin)
