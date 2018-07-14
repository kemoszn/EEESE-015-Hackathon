from django.contrib import admin
from .models import Post, Comment


#class CommentAdmin(admin.ModelAdmin):
	#list_display = ('name',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('slug', 'author', 'publish','status')


admin.site.register(Post,PostAdmin)
admin.site.register(Comment)
