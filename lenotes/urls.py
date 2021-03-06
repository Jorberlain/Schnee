from django.urls import path
import django.views

from lenotes import views

app_name = 'lenotes'

urlpatterns = [
    path('index/', views.index, name = 'index'),

    path('home/', views.home, name = 'home'),

    path('group/<int:group_id>', views.group, name = 'group'),

    path('diary_month/<int:group_id>/<int:year>/<int:month>', views.diary_month, name = 'diary_month'),

    path('manage/<int:group_id>', views.manage, name = 'manage'),
    
    path('del_member/<int:group_id><int:info_id>', views.del_member, name = 'del_member'),

    path('send_invite/<int:group_id>', views.send_invite, name = 'send_invite'),

    path('new_group/', views.new_group, name = 'new_group'),

    path('del_group/<int:group_id>', views.del_group, name = 'del_group'),

    path('new_diary/<int:group_id>', views.new_diary, name = 'new_diary'),

    path('edit_diary_md/<int:diary_id>', views.edit_diary_md, name = 'edit_diary_md'),

    path('diary_log/<int:diary_id>', views.diary_log, name = 'diary_log'),

    path('lenotes_intro/', views.lenotes_intro, name = 'lenotes_intro'),
]
