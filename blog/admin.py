from django.contrib import admin
from blog.models import Post, Category, Media


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'slug', 'created', 'modified', )
    list_filter = ('categories',)
    search_fields = ('title', 'markdown_content',)

    fieldsets = [
        ('Post', {
            'fields': ('title', 'header_image', )
        }),
        ('Markdown', {
            'fields': ('markdown_content',)
        }),
        ('Categories', {
            'fields': ('categories',)
        }),
        ('Author', {
            'fields': ('author', )
        }),
        ('History', {
            'fields': ('created', 'modified',)
        })
    ]
    readonly_fields = ('created', 'modified',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)

    fieldsets = [
        ('Categories', {
            'fields': ('name',)
        }),
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Media)
