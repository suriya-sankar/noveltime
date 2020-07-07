from django.contrib import admin
from .models import story,chappter,comments,audio_story,audio_chappter,audio_comments
admin.site.register(story)
admin.site.register(chappter)
admin.site.site_header="story"
admin.site.register(comments)
admin.site.register(audio_chappter)
admin.site.register(audio_story)
admin.site.register(audio_comments)