from django.contrib import admin
from .models import story,chappter,comments
admin.site.register(story)
admin.site.register(chappter)
admin.site.site_header="story"
admin.site.register(comments)