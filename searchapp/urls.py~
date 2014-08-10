from django.conf.urls import patterns,url
from django.conf import settings
from searchapp import views

urlpatterns=patterns('',
	url(r'^$',views.index,name='index'),
	url(r'result/',views.result,name='result'),
	url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)

