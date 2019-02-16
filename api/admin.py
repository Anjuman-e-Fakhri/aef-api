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
    list_display = ['__str__', 'is_hof', 'jamaat_id', 'title', 'first_name', 'last_name',
                    'its_id', 'cell_number', 'email', 'address', 'city']
    list_filter = ['is_hof', 'title', 'updated', 'created']
    search_fields = ['its_id', 'jamaat_id', 'title', 'first_name', 'last_name',
                    'cell_number', 'email', 'address', 'city']
    readonly_fields = ('created', 'updated')
    resource_class = MuminResource
    fieldsets = (
        ('IDs', {
            'fields': (
                'its_id',
                'jamaat_id',
                'hof_its_id',
                'relationship_to_hof',
                )
        }),
        ('Details', {
            'fields': (
                'title',
                'first_name',
                'last_name',
                'gender',)
        }),
        ('Contact', {
            'fields': (
                'cell_number',
                'res_number',
                'other_number',
                'email',
                'email_2',
                'address',
                'city',
                'province',
                'postal_code',
                'country',)
        }),
        ('Other', {
            'classes': ('collapse',),
            'fields': ('is_hof', 'zone', 'birthday', 'created', 'updated', 'active'),
        }),
    )


admin.site.register(Mumin, MuminAdmin)
