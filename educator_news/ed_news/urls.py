from django.conf.urls import patterns, url

from ed_news import views

urlpatterns = patterns('',
    # My urls

    # --- Educator News home page ---
    url(r'^$', views.index, name='index'),

    url(r'^new/', views.new, name='new'),
    url(r'^submit/', views.submit, name='submit'),
    url(r'^upvote_article/(?P<article_id>\d+)/$', views.upvote_article, name='upvote_article'),
)
