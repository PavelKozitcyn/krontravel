from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['title']}
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.site_header = "Кронтревел"

admin.site.site_title = "Админ панель Кронтревел"
admin.site.index_title = "Управление Кронтревел"