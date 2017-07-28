from django.conf.urls import url

from . import views
app_name = 'polls'
urlpatterns = [
               # url(r'^f(?P<value>\d+)', views.first, name='first'),
               # url(r'^s', views.second, name='second'),
               # url(r'^$', views.base, name='base'),

               url(r'^$', views.index, name='index'),
               # ex: /polls/5/
               # url(r'^(?P<question_id+)$', views.details, name='details'),
               url(r'^(?P<question_id>[0-9]+)/$', views.details, name='details'),
               # ex: /polls/5/results/
               url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
               # ex: /polls/5/vote/
               url(r'^(?P<question_id>[0-9]+)/votes/$', views.vote, name='vote'),
               ]
