from django.conf.urls.defaults import *
from piston.resource import Resource
# from piston_demo.api.handlers import TaskHandler
from apps.api.handlers import *
from apps.api.emitters import ExtJSONEmitter

publisher_resource = Resource(PublisherHandler)
publisher_series_resource = Resource(PublisherSeriesHandler)
publisher_brand_resource = Resource(PublisherBrandHandler)
publisher_indicia_resource = Resource(PublisherIndiciaHandler)
publisher_issues_resource = Resource(PublisherIssuesHandler)

brand_resource = Resource(BrandHandler)
brand_issue_resource = Resource(BrandIssueHandler)
brand_series_resource = Resource(BrandSeriesHandler)

indicia_resource = Resource(IndiciaPublisherHandler)
indicia_publisher_issues_resource = Resource(IndiciaPublisherIssuesHandler)
indicia_publisher_series_resource = Resource(IndiciaPublisherSeriesHandler)

series_resource = Resource(SeriesHandler)
series_issues_resource = Resource(SeriesIssueHandler)
series_publishers_resource = Resource(SeriesPublisherHandler)
series_indicia_publishers_resource = Resource(SeriesIndiciaHandler)

issue_resource = Resource(IssueHandler)

urlpatterns = patterns('',
    url(r'^publisher/(?P<pk_id>\d+)$', publisher_resource),
    url(r'^publisher/(?P<pk_id>\d+)/series$', publisher_series_resource),
    url(r'^publisher/(?P<pk_id>\d+)/brands$', publisher_brand_resource),
    url(r'^publisher/(?P<pk_id>\d+)/indicia_publishers$', publisher_indicia_resource),
    url(r'^publisher/(?P<pk_id>\d+)/issues$', publisher_issues_resource),
    
    url(r'^brand/(?P<pk_id>\d+)$', brand_resource),
    url(r'^brand/(?P<pk_id>\d+)/issues$', brand_issue_resource),
    url(r'^brand/(?P<pk_id>\d+)/series$', brand_series_resource),
    
    url(r'^indicia_publisher/(?P<pk_id>\d+)$', indicia_resource),
    url(r'^indicia_publisher/(?P<pk_id>\d+)/issues$', indicia_publisher_issues_resource),
    url(r'^indicia_publisher/(?P<pk_id>\d+)/series$', indicia_publisher_series_resource),
    
    url(r'^issue/(?P<pk_id>\d+)$', issue_resource),
    
    url(r'^series/(?P<pk_id>\d+)$', series_resource),
    url(r'^series/(?P<pk_id>\d+)/issues$', series_issues_resource),
    url(r'^series/(?P<pk_id>\d+)/publishers$', series_publishers_resource),
    url(r'^series/(?P<pk_id>\d+)/indicia_publishers$', series_indicia_publishers_resource),
)