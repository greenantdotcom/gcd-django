from django.conf.urls.defaults import *
from piston.resource import Resource
# from piston_demo.api.handlers import TaskHandler
from apps.api.handlers import *
from apps.api.emitters import ExtJSONEmitter

testtask_resource = Resource(TestTaskHandler)
publisher_resource = Resource(PublisherHandler)
publisher_series_resource = Resource(PublisherSeriesHandler)
publisher_brands_resource = Resource(PublisherBrandsHandler)
series_resource = Resource(SeriesHandler)
series_issues_resource = Resource(SeriesIssueHandler)

urlpatterns = patterns('',
   url(r'^testtasks/(?P<id>\d+)$', testtask_resource),
   url(r'^testtasks$', testtask_resource),
   
   # url(r'^publishers/(?P<id>\d+)$', publisher_resource,  {'emitter_format': 'ext-json'}),
   # url(r'^publishers$', publisher_resource,  {'emitter_format': 'ext-json'}),
   url(r'^publishers/(?P<id>\d+)/series$', publisher_series_resource),
   url(r'^publishers/(?P<id>\d+)/brands$', publisher_brands_resource),
   url(r'^publishers/(?P<id>\d+)$', publisher_resource),
   url(r'^publishers$', publisher_resource),
   
   url(r'^series/(?P<id>\d+)$', series_resource),
   url(r'^series/(?P<id>\d+)/issues$', series_issues_resource),
   url(r'^series$', series_resource),
)

# 
# 
# 
# from piston.resource import Resource
# from api.handlers import TestHandler
# 
# 
# # urlpatterns = patterns('',
# #    # url(r'^test(\.(?P<emitter_format>.+))$', ...),
# # )