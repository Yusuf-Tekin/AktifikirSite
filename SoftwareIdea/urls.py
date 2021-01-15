
from django.contrib import admin
from django.urls import path,include
from App import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Login),
    path('login/',views.Login,name = "Login"),
    path('newaccount/',views.NewAccount,name = "NewAccount"),
    path('home/',views.home,name = "Home"),
    path('logout/',views.Logout,name = "Logout"),
    path('apps/',views.Apps,name = "Apps"),
    path('ideas/',views.Ideas,name = "Ideas"),
    path('account/',views.Account,name = "Account"),
    path('newapp/',views.NewApp,name = "NewApp"),
    path('newidea/',views.NewIdea,name = "NewIdea"),
    path('apps/detail/<id>/',views.AppDetail,name = "AppDetail"),
    path('idea/detail/<id>/',views.IdeaDetail,name = "IdeaDetail"),
    path('ChangePassword/',views.ChangePassword,name = "ChangePassword"),
    path('deleteidea/<id>/',views.deleteidea,name = "deleteidea"),
    path('deleteapps/<id>/',views.deleteapps,name = "deleteapps"),
      # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
     name='password_reset_complete'),




]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
