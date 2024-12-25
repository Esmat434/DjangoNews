from django.contrib import admin
from .models import Category,Tag,Artical,SaveArtical,Images,Comment,AnswerComment,Subscriber,Like,PageView
# Register your models here.

@admin.register(Category)
class CategoryAdmmin(admin.ModelAdmin):
    list_display = ['id','name','slug','is_enable','created_time']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id','category','name','slug']

@admin.register(Artical)
class ArticalAdmin(admin.ModelAdmin):
    list_display = ['id','category','title','slug','author','status']

@admin.register(SaveArtical)
class SaveArticalAdmin(admin.ModelAdmin):
    list_display = ['id','username','artical',"saved",'created_time']

@admin.register(Images)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id','artical','created_time']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','username','artical','created_time']

@admin.register(AnswerComment)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ['id','comment','content','created_time']
    
@admin.register(Subscriber)
class SubscripAdmin(admin.ModelAdmin):
    list_display = ['id','email','subscribed_date']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ['id','username','page_name','created_time']

@admin.register(PageView)
class PageViewAdmin(admin.ModelAdmin):
    list_display = ['id','ip','page_name','view_count']