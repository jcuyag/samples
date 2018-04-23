from django.contrib import admin
from app.models import Track, Speaker, Session
# Register your models here.


class SpeakerAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'bio']


class TrackAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']


class SessionAdmin(admin.ModelAdmin):
    list_display = ['title', 'description',
                    'track', 'speaker']


admin.site.register(Track, TrackAdmin)
admin.site.register(Speaker, SpeakerAdmin)
admin.site.register(Session, SessionAdmin)