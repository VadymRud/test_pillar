from django.contrib import admin
from .models import Chapter, News

class ChapterAdmin(admin.ModelAdmin):
    pass


admin.site.register(Chapter, ChapterAdmin)


class NewsAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)
