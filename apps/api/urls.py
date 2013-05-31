from django.conf.urls.defaults import *
from piston.resource import Resource
# from piston_demo.api.handlers import TaskHandler
from apps.api.handlers import *
from apps.api.emitters import ExtJSONEmitter

publisher_resource = Resource(PublisherHandler)
publisher_series_resource = Resource(PublisherSeriesHandler)
publisher_brand_resource = Resource(PublisherBrandHandler)
publisher_indicia_resource = Resource(PublisherIndiciaHandler)

# series_resource = Resource(SeriesHandler)
# series_issues_resource = Resource(SeriesIssueHandler)
# # documentation_resource = Resource(DocumentationHandler)
# issue_resource = Resource(IssueHandler)
# brand_resource = Resource(BrandHandler)

urlpatterns = patterns('',
    url(r'^publishers/(?P<id>\d+)$', publisher_resource),
    url(r'^publishers/(?P<id>\d+)/series$', publisher_series_resource),
    url(r'^publishers/(?P<id>\d+)/brands$', publisher_brand_resource),
    url(r'^publishers/(?P<id>\d+)/indicia_publishers$', publisher_indicia_resource),
    
    # url(r'^indicia_publishers/(?P<id>\d+)$', indicia_resource),
    # url(r'^indicia_publishers/(?P<id>\d+)/series$', indicia_series_resource),
    # 
    # url(r'^brands/(?P<id>\d+)$', brand_resource),
    # url(r'^brands/(?P<id>\d+)/issues$', brand_issue_resource),
    # url(r'^brands/(?P<id>\d+)/series$', brand_series_resource),
    # 
    # url(r'^series/(?P<id>\d+)$', series_resource),
    # 
    # url(r'^issue/(?P<id>\d+)$', issue_resource),
    # 
    # url(r'^publishers$', publisher_resource),
    # 
    # url(r'^series/(?P<id>\d+)/issues$', series_issues_resource),
    # url(r'^series$', series_resource),
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