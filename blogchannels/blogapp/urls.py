from django.conf.urls import url
from blogapp.views import base_view, post_detail


urlpatterns = [
    url(r'^$', base_view, name='base_view'),
    url(r'post/(?P<slug>[-\w]+)/$', post_detail, name='post_detail')
]
