from django.contrib import admin
from .models import Post, Category, Tag


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    # 配置 Post 在 admin 后台的一些展现形式。list_display 属性控制 Post 列表页展示的字段
    list_display = ['title', 'created_time', 'modified_time', 'category', 'author']
    # fields 属性，则用来控制表单展现的字段
    fields = ['title', 'body', 'excerpt', 'category', 'tags']


    def save_model(self, request, obj, form, change):
        """
        Postadmin 继承自 ModelAdmin，它有一个 save_model 方法，这个方法只有一行代码：obj.save()。
        它的作用就是将此 Modeladmin 关联注册的 model 实例（这里 Modeladmin 关联注册的是 Post）保存到数据库。
        这个方法接收四个参数，其中前两个，一个是 request，即此次的 HTTP 请求对象，第二个是 obj，即此次创建的关联对象的实例，
        于是通过复写此方法，就可以将 request.user 关联到创建的 Post 实例上，然后将 Post 数据再保存到数据库
        """
        obj.author = request.user
        super().save_model(request, obj, form, change)


# 把新增的 Postadmin 也注册进来
admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Tag)
