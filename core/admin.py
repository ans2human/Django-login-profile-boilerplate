from django.contrib import admin
# Register your models here.
from .models import Profile
from django.utils.html import format_html


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('ph_no', 'company', 'designation')
    def image_tag(self, profile):
        return format_html('<img src="{}" />'.format(profile.photo.url))

        image_tag.short_description = 'Image of the user'

