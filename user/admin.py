from django.contrib import admin
from .models import Hobby, Profile, User
from django.contrib.auth.admin import UserAdmin as BaseUseradmin

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(BaseUseradmin):
    list_display = ('id', 'username', 'fullname', 'email')
    list_display_link = ('username',)
    list_filter = ('username',)
    search_fields = ('username', 'email',)
    readonly_fields = ('username', 'join_date',)
    
    fieldsets = (
        ("info", {'fields': ('username', 'password', 'email', 'fullname', 'join_date')}),
        ('permissions', {'fields': ('is_admin', 'is_active', )}),
    )
    filter_horizontal = []
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date',)
        else:
            return ('join_date', )       
    inlines = (
            ProfileInline,
        )
    # def has_add_permission(self, request, obj=None): # 추가 권한
    #     return False

    # def has_delete_permission(self, request, obj=None): # 삭제 권한
    #     return False

    # def has_change_permission(self, request, obj=None): # 수정 권한
    #     return False
    
    
# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.register(Hobby)



