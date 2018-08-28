from django.urls import include, re_path,path
from . import views
  

urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/reply/$',views.reply_topic, name='reply_topic'),
    re_path(r'^boards/(?P<pk>\d+)/$',views.TopicListView.as_view(), name='board_topics'),
    re_path(r'^boards/(?P<pk>\d+)/new/$', views.new_topic, name='new_topic'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/$', views.PostListView.as_view(), name='topic_posts'),
    re_path(r'^boards/(?P<pk>\d+)/topics/(?P<topic_pk>\d+)/posts/(?P<post_pk>\d+)/edit/$',
            views.PostUpdateView.as_view(), name='edit_post'),
    
]