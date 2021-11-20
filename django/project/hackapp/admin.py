from django.contrib import admin
from hackapp.models import User, Follow, Challenge, Challenge_User, Challenge_Check

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('user_id', 'user_pw', 'name',)

class FollowAdmin(admin.ModelAdmin):
    list_display=('num', 'user_id', 'target_id',)

class ChallengeAdmin(admin.ModelAdmin):
    list_display=('challenge_id', 'name', 'start_date', 'end_date', 'image', 'contents', 'creator_id',)

class Challenge_UserAdmin(admin.ModelAdmin):
    list_display=('challenge_id', 'user_id', 'start_date', 'num',)

class Challenge_CheckAdmin(admin.ModelAdmin):
    list_display=('num', 'challenge_id', 'user_id', 'check_date',)

admin.site.register(User, UserAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Challenge, ChallengeAdmin)
admin.site.register(Challenge_User, Challenge_UserAdmin)
admin.site.register(Challenge_Check, Challenge_CheckAdmin)