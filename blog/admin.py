from django.contrib import admin
from .models import Post,BlogComment

# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'email', 'post', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')

admin.site.register(Post)
admin.site.register(BlogComment)
