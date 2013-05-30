from django.core.paginator import Paginator
from piston.handler import BaseHandler
from apps.api.models import TestTask
from apps.gcd.models import *
from piston.doc import generate_doc

class TestTaskHandler(BaseHandler):
    model = TestTask

class CountryHandler(BaseHandler):
    """
    Handles returning countries in a consistent manner
    """
    fields = ( 'id', 'name', 'code', )
    model = Country
    ## TODO: Uppercase the country code?

class PublisherHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
    fields = ( 'id', 'name', 'created', 'updated', 'url', 'year_began', 'country', 'indicia_set' )
    model = Publisher

# class PublisherSeriesHandler(BaseHandler):
#     """
#     Defines how publishers are returned and fetched
#     """
#     fields = ( 'id', 'name', 'issue_count', )
#     model = Series
# 
#     # @staticmethod
#     # def resource_uri():
#     #     return ('api_blogpost_handler', ['id'])
#     
#     def read(self, request, id):
#         
#         p = Publisher.objects.get(id=int(id))
#         # except:
#             # return rc.NOT_FOUND;
#         
#         return p.series_set;

class PublisherBrandsHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
    fields = ( 'id', 'name', )
    model = IndiciaPublisher

    # @staticmethod
    # def resource_uri():
    #     return ('api_blogpost_handler', ['id'])
    
    def read(self, request, id):
        p = Publisher.objects.get(id=int(id))
        return p.indiciapublisher_set;

class PublisherSeriesHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
    fields = ( 'id', 'name', 'issue_count', )
    model = Series

    # @staticmethod
    # def resource_uri():
    #     return ('api_blogpost_handler', ['id'])
    
    def read(self, request, id):
        return Series.objects.filter(publisher_id=id,deleted=0).sort_by('')
        p = Publisher.objects.get(id=int(id))
        return p.series_set;

class SeriesHandler(BaseHandler):
    """
    Defines how series are returned and fetched
    """
    fields = ( 'id', 'name' )
    model = Series
    
    # def read(self, request, pk=None):
    #     if pk is not None:
    #         return Publisher.objects.get(pk=int(pk))
    #     paginator = Paginator(Publisher.objects.all(), 200)
    #     return paginator.page(int(request.GET.get('page', 1))).object_list

class SeriesIssueHandler(BaseHandler):
    """
    Defines how series are returned and fetched
    """
    fields = ( 'id', 'title', 'number', 'price', 'isbn', 'publication_date', 'page_count', 'short_name', 'full_name' )
    model = Issue
    
    def read(self, request, id):
        p = Series.objects.get(id=int(id))
        ## Return them in publication sort order
        return Issue.objects.filter(series_id=id, deleted=0).order_by( 'key_date', 'volume', 'number');

doc = generate_doc(PublisherHandler)

print doc.name

# return;

# print doc.name # -> 'BlogpostHandler'
# print doc.model # -> <class 'Blogpost'>
# print doc.resource_uri_template # -> '/api/post/{id}'
# 
# methods = doc.get_methods()
# 
# for method in methods:
#    print method.name # -> 'read'
#    print method.signature # -> 'read(post_slug=<optional>)'
# 
#    sig = ''
# 
#    for argn, argdef in method.iter_args():
#       sig += argn
# 
#       if argdef:
#          sig += "=%s" % argdef
# 
#       sig += ', '
# 
#    sig = sig.rstrip(",")
# 
#    print sig # -> 'read(repo_slug=None)'
# 
