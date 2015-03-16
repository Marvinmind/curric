from django.conf.urls import patterns, include, url

urlpatterns = patterns('plan.views',
	url(r'^showplan/$','showplan'),
    url(r'editplan/$','editplan')
)