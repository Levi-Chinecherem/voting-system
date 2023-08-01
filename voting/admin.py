from django.contrib import admin
from django.utils.html import format_html
from .models import Candidate, Vote, VotingPosition

class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'details', 'image_thumbnail')
    search_fields = ('name', 'position__position')
    list_filter = ('position',)

    def image_thumbnail(self, obj):
        return format_html('<img src="{}" style="max-height: 50px; max-width: 50px;" alt="{}">', obj.image.url, obj.name)

    image_thumbnail.allow_tags = True

class VotingPositionAdmin(admin.ModelAdmin):
    list_display = ('position', 'start_date', 'end_date', 'is_active')
    list_filter = ('start_date', 'end_date')

    def is_active(self, obj):
        return obj.is_active()

    is_active.boolean = True

admin.site.register(Candidate, CandidateAdmin)
admin.site.register(Vote)
admin.site.register(VotingPosition, VotingPositionAdmin)
