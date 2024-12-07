from django import forms
from django.contrib import admin
from .models import Personnel, Room, RoomSchedule

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['name', 'contact', 'location', 'image', 'employment_type', 'department_position']

    def __init__(self, *args, **kwargs):
        super(PersonnelForm, self).__init__(*args, **kwargs)
        self.fields['employment_type'].empty_label = "Select Employment Type"
        self.fields['department_position'].widget.attrs['disabled'] = 'disabled'  # Initially disabled

class PersonnelAdmin(admin.ModelAdmin):
    form = PersonnelForm

    class Media:
        js = ('js/custom_admin.js',)  # JavaScript to enable/disable the department_position field

class RoomAdmin(admin.ModelAdmin):
    # Override this method to hide "Rooms" from the admin index
    def has_module_permission(self, request):
        return False  # Prevents "Rooms" from showing in the sidebar

# Register your models here.
admin.site.register(Personnel, PersonnelAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(RoomSchedule)