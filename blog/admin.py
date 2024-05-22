from django.contrib import admin

from blog.models import Tag, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  prepopulated_fields = {"slug": ("title",)}
  list_display = ('slug', 'published_at',)

admin.site.register(Tag)

