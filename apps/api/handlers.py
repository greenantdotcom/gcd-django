from django.core.paginator import Paginator
from piston.handler import BaseHandler
from apps.api.models import TestTask
from apps.gcd.models import *
from piston.doc import generate_doc
from piston.resource import Resource

class CountryHandler(BaseHandler):
    """
    """
    exclude= ('id')
    model = Country

class PublisherHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
    exclude= ('deleted','reserved')
    model = Publisher

class SeriesHandler(BaseHandler):
    """
    """
    exclude= ('deleted')
    model = Series


class BrandHandler(BaseHandler):
    """
    """
    exclude= ('deleted')
    model = Brand

class IndiciaPublisherHandler(BaseHandler):
    """
    """
    model = IndiciaPublisher

class PublisherSeriesHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
    def read(self, request, id):
        return Series.objects.filter(publisher_id=id,publisher__deleted=0,deleted=0).order_by('sort_name')

class PublisherIndiciaHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
    # @staticmethod
    # def resource_uri():
    #     return ('api_blogpost_handler', ['id'])
    
    def read(self, request, id):
        return IndiciaPublisher.objects.filter(parent_id=int(id),parent__deleted=0,deleted=0).order_by('name')

class PublisherBrandHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
#    fields = ( 'id', 'name', )
    
    def read(self, request, id):
        return Brand.objects.filter(parent_id=int(id),deleted=0)


class CountryHandler(BaseHandler):
    """
    Handles returning countries in a consistent manner
    """
    fields = ( 'id', 'name', 'code', )
    model = Country
    ## TODO: Uppercase the country code?




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

class BrandHandler(BaseHandler):
    """
    """
    model = IndiciaPublisher

class IssueHandler(BaseHandler):
    """
    Defines how series are returned and fetched
    """
    fields = ( 'id', 'title', 'number', 'price', 'isbn', 'publication_date', 'page_count', 'short_name', 'full_name', 'language', 'volume_number', 'series_id', ( 'indicia_publisher', ( 'name' ) ) )
    model = Issue
    
    def read(self, request, id):
        item = Issue.objects.filter(id=int(id), deleted=0).get()
        
        data = {
                    'id': item.id,
                    'short_name': item.short_name(),
                    'series_id': item.series_id,
                    'brand': item.brand,
                    'number': item.number,
                    'indicia_brand': item.indicia_publisher,
                    'number': item.number,
                    # 'volume_number': item.volume_number,
                    'price': item.price,
                    'isbn': item.isbn,
                    'publication_date': item.publication_date,
                    'page_count': item.page_count,
                    'language': item.page_count,
                    
                }
        
        return data;

# class DocumentationHandler(BaseHandler):
#     def read(self, request):
#         doc = generate_doc(PublisherHandler);
#         
#         sig = ' (methods follow )'
#         
#         return doc.get_methods().__dict__()
#         
#         for method in doc.get_methods():
#            print method.name # -> 'read'
#            print method.signature # -> 'read(post_slug=<optional>)'
#            
#            for argn, argdef in method.iter_args():
#               sig += argn
#         
#               if argdef:
#                  sig += "=%s" % argdef
#         
#               sig += ', '
#         
#            sig = sig.rstrip(",")
#         
#         return sig

# doc = generate_doc(PublisherHandler)
# 
# print doc.name

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
