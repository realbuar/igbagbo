from django.urls import path
from . import views

app_name = 'church'


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('ay', views.upload, name='upload' ),
    path('cells', views.wsf, name='wsf_list'),
    path('books', views.shop, name='book_list'),
    path('media', views.studio, name='nice'),
    path('halelluyah', views.tropics, name='wonder'),
    path('congrat', views.topics, name='topics'),
    path('mercy(?P<topic_id>\d+)$', views.topic, name='good'),
    path('miracles(?P<tropic_id>\d+)$', views.tropic, name='no'),
    path('yaf', views.Yaf, name='amen'),
    path('wow', views.contact, name='back'),
     path('woow', views.yafcontact, name='alayo'),
    path('new', views.tops, name='new'),
    path('(?P<top_id>\d+)$', views.top, name='news')
]
