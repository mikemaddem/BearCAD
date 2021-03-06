from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.conf import settings
from django.conf.urls.static import settings
from profiles import views as profile_views
from django.conf.urls.static import static
from pages import views as pages_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^register/', profile_views.CreateUserFormView.as_view(), name='register'),

    path('', pages_views.index, name='index'),
    path('about/', pages_views.about, name='about'),
    path('terms/', pages_views.terms, name='terms'),
    path('privacy/', pages_views.privacy, name='privacy'),
    path('404/', pages_views.notfound),

    url(r'^login/', profile_views.login, {'template_name': 'profiles/login_form.html'}, name='login'),
    #url(r'^logout/', logout, {'template_name': 'index.html', 'next_page': '/'}, name='logout'),
    #url(r'^reset-password/$', password_reset, {'template_name': 'profiles/reset_form.html', 'email_template_name': 'profiles/reset_email.html'}, name='reset_password'),
    ##url(r'^reset-password/done/$', password_reset_done, {'template_name': 'profiles/reset_done.html'}, name='password_reset_done'),
    #url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', password_reset_confirm, {'template_name': 'profiles/reset_confirm.html'}, name='password_reset_confirm'),
    #url(r'^reset-password/complete$', password_reset_complete, {'template_name': 'profiles/reset_complete.html'}, name='password_reset_complete'),
    url(r'^profile/', include('profiles.urls', namespace='profiles')),
    url(r"^activate/(?P<uidb64>[0-9A-Za-z_'\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$", profile_views.activate, name='activate'),


]
