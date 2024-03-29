from django.contrib import admin

from .models import Comment, Review, Category, Genre, Title


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'author', 'title', 'pub_date')
    search_fields = ('text', 'score', 'pub_date')
    list_filter = ('title', 'pub_date')
    empty_value_display = '-пусто-'


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)

