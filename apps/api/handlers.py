"""
Handlers for the webservices API
"""

from django.http import Http404
from django.shortcuts import get_object_or_404
# from piston.doc import generate_doc
#from piston.resource import Resource
from piston.handler import BaseHandler
from apps.gcd.models import Country, Publisher, Brand, Series, IndiciaPublisher, Issue

class AbstractHandler(BaseHandler):
    """
    Abstracts basic repeatable patterns for loading objects
    """
    def read(self, request, pk_id):
        """
        Handles an incoming request for a basic model
        """
        return rc.NOT_FOUND
        
        try:
            return self.load_object_for_handler(pk_id)
        except:
            pass
    
    def load_object_for_handler(self, pk_id):
        """
        For some reason, for some models, get_object_or_404 wasn't working when I was passing in
        self.model, self.model._meta.object_name, or anything else.
        """
        fetched_object = self.model.objects.get(pk=pk_id)
        
        if object:
            return fetched_object
        else:
            raise Http404('No %s matches the given query.' %
                self.model)

class CountryHandler(AbstractHandler):
    """
    Handler for countries
    """
    model = Country
    
class PublisherHandler(AbstractHandler):
    """
    Defines how publishers are returned and fetched
    """
    exclude = ('deleted', 'reserved')
    include = ('id')
    model = Publisher

class SeriesHandler(AbstractHandler):
    """
    Handler for series
    """
    
    include = ('id')
    exclude = ()
    model = Series

class BrandHandler(AbstractHandler):
    """
    Handler for brands
    """
    
    include = ('id')
    exclude = ()
    model = Brand

class IndiciaPublisherHandler(AbstractHandler):
    """
    Handler for indicia publishers
    """
    
    model = IndiciaPublisher
    exclude = ()

class PublisherSeriesHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
    def read(self, request, pk_id):
        """
        Finds those series which are related to the provided publisher
        """
        return Series.objects.filter(publisher_id=pk_id, publisher__deleted=0,
            deleted=0).order_by('sort_name')

class PublisherIssuesHandler(BaseHandler):
    """
    Returns a list of issues for a given publisher
    """
    def read(self, request, pk_id):
        """
        Finds those issues which are related to the provided publisher
        """
        return Issue.objects.filter(indicia_publisher__parent=pk_id, indicia_publisher__parent__deleted=0,
            deleted=0).order_by('sort_code')

class PublisherIndiciaHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
    
    def read(self, request, pk_id):
        """
        Finds those indicia publishers which are related to the provided publisher
        """
        return IndiciaPublisher.objects.filter(parent_id=int(pk_id),
            parent__deleted=0, deleted=0).order_by('name')

class PublisherBrandHandler(BaseHandler):
    """
    Defines how publishers are returned and fetched
    """
    def read(self, request, pk_id):
        """
        Finds those brands which are related to the provided publisher
        """
        return Brand.objects.filter(parent_id=int(pk_id), deleted=0)

class IndiciaPublisherSeriesHandler(BaseHandler):
    """
    TBD - How can I properly (if at all) query the issues attached to the ind_pub and then get the brands in that set. And if I do, what should that data actually look like?
    """
    
    def read(self, request, pk_id):
        """
        Finds those series which are related to the provided indicia publisher
        """
        issues = IndiciaPublisher.objects.get(pk=int(pk_id)).issue_set.order_by('sort_code').all()
        return set( item.series for item in issues )

class IndiciaPublisherIssuesHandler(BaseHandler):
    """
    Returns the list of issues for a given indicia publisher
    """
    
    def read(self, request, pk_id):
        """
        Finds those issues which are related to the provided indicia publisher
        """
        return IndiciaPublisher.objects.get(pk=int(pk_id)).issue_set.order_by('sort_code').all()

class SeriesIssueHandler(BaseHandler):
    """
    Returns the list of issues for a given series
    """
    
    def read(self, request, pk_id):
        """
        Finds those issues which are related to the provided series
        """
        return Series.objects.get(pk=int(pk_id)).issue_set.order_by('sort_code').all()

class BrandSeriesHandler(BaseHandler):
    """
    Returns the list of brands for a given series
    """
    
    def read(self, request, pk_id):
        """
        Finds those series which are related to the provided brand
        """
        issues = Brand.objects.get(pk=int(pk_id)).issue_set.order_by('sort_code').all()
        return set( item.series for item in issues )

class BrandIssueHandler(BaseHandler):
    """
    Returns the list of issues for a given brand
    """
    
    def read(self, request, pk_id):
        """
        Finds those issues which are related to the provided brand
        """
        return Brand.objects.get(pk=int(pk_id)).issue_set.order_by('sort_code').all()

class SeriesPublisherHandler(AbstractHandler):
    """
    Returns the list of publishers for a given series
    """
    
    def read(self, request, pk_id):
        """
        Finds those publishers which are related to the provided series
        """
        return "hi"

class SeriesIndiciaHandler(AbstractHandler):
    """
    Returns the list of indicia publishers for a given series
    """
    
    def read(self, request, pk_id):
        """
        Finds those indicia publishers which are related to the provided series
        """
        return "hi"

class IssueHandler(AbstractHandler):
    """
    Defines how series are returned and fetched
    """
    
    fields = ('id', 'title', 'number', 'price', 'isbn', 'publication_date',
        'page_count', 'short_name', 'full_name', 'language', 'volume_number',
        'series_id', ('indicia_publisher', 'name'))
    
    model = Issue