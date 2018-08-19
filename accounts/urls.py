from django.conf.urls import url
from django.contrib.auth import views as auth_views

#django introduced log in and logout views so we dont need to take care of it
#we import as auth_views so that it doesent get confused with views on line 6
from . import views
from django.urls import include, re_path

app_name = 'accounts'

urlpatterns = [
        re_path(r'login/$',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
        # we pass in the name of the template we want to connect it to
        re_path(r"logout/$", auth_views.LogoutView.as_view(),name="logout"),
        re_path(r'signup/$',views.SignUp.as_view(),name='signup'),
]
