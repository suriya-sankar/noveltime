from django.contrib import admin
from .models import story,chappter
admin.site.register(story)
admin.site.register(chappter)
admin.site.site_header="story"