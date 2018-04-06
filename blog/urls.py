from django.conf.urls import url
from . import views
from django.conf.urls.static import static


urlpatterns = (
    url(r'^$', views.users_list, name='users_list'),
    url(r'^author/(?P<username>[a-zA-Z0-9_]+)/$', views.list_of_posts, name='list_of_posts'),
    url(r'^posts/(?P<pk>[a-zA-Z0-9_]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^accounts/login/$', views.log_in, name='login'),
    url(r'^accounts/logout$', views.log_out, name='log_out'),
    url(r'^me$', views.who_is_it, name='who_is_it'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>[0-9]+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^post/(?P<pk>[0-9]+)/like/$', views.post_like, name='post_like'),
    url(r'^post/(?P<pk>[0-9]+)/like1/$', views.post_like2, name='post_like2'),
    url(r'^profile/edit/$', views.profile_edit, name='profile_edit'),
    url(r'^register/$', views.register, name='register'),
)
