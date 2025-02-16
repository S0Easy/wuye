from django.contrib import admin
from .models import BSIC_INFO

from django.urls import path
# Register your models here.


@admin.register(BSIC_INFO)
class BSIC_INFOAdmin(admin.ModelAdmin):
    #fields = ('ip', 'hostname')
    list_display = ('ip', 'hostname', 'assset_desc', 'os_type')
    # list_display_links = ('ip', 'hostname')
    list_filter = ('ip', 'hostname', 'assset_desc', 'os_type')
    search_fields = ('ip', 'hostname', 'assset_desc', 'os_type')



    actions = ['make_copy', 'custom_button']

    def custom_button(self, request, queryset):
        pass

    # 显示的文本，与django admin一致
    custom_button.short_description = '测试按钮'
    # icon，参考element-ui icon与https://fontawesome.com
    custom_button.icon = 'fas fa-audio-description'

    # 指定element-ui的按钮类型，参考https://element.eleme.cn/#/zh-CN/component/button
    custom_button.type = 'danger'

    # 给按钮追加自定义的颜色
    custom_button.style = 'color:black;'

    def make_copy(self, request, queryset):
        pass
    make_copy.short_description = '复制员工'


    fieldsets = [
        ('主机信息', {
            'fields': ['ip', 'hostname']
        }),
        ('资产描述', {
            'fields': ['assset_desc']
        }),
        ('操作系统', {
            'fields': ['os_type']
        }),
    ]


admin.site.index_title = "欢迎使用cmdb管理系统"
admin.site.site_header = "cmdb管理系统"


