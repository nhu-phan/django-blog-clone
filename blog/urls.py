from django.urls import re_path
from blog import views

urlpatterns = [
    re_path(r'^$', views.PostListView.as_view(), name='post_list'),
    re_path(r'^post/(?P<pk>\d+)/$', views.PostDetailView.as_view(), name='post_detail'),
    re_path(r'^about/$', views.AboutView.as_view(), name='about'),
    re_path(r'^post/new/$', views.create_post, name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$', views.PostUpdateView.as_view(), name='post_update'),
    re_path(r'^post/(?P<pk>\d+)/remove/$', views.PostDeleteView.as_view(), name='post_delete'),
    re_path(r'^drafts/$', views.DraftListView.as_view(), name='post_draft_list'),
    re_path(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$', views.approving_comment, name='approving_comment'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$', views.removing_comment, name='removing_comment'),
    re_path(r'^post/(?P<pk>\d+)/publish/$', views.publishing_post, name='publishing_post'),
    re_path(r'^base/', views.view_base, name='view_base'),
    re_path(r'^bye/$', views.see_you_again, name="seeyou"),
    re_path(r'^register/$', views.register_request, name="register"),
]

