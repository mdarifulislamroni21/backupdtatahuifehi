from django.contrib import admin
from Post.models import Categorys,Post,PostImage,Comment,NewsLetter,RepComment,visitors
# Register your models here.
admin.site.register(Categorys)
admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Comment)
admin.site.register(NewsLetter)
admin.site.register(RepComment)
admin.site.register(visitors)