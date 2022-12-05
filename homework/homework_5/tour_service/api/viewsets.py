from rest_framework import viewsets
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status

from collections import OrderedDict

class LinksAwarePageNumberPagination(PageNumberPagination):
   def get_paginated_response(self, data, links=[]):
       return Response(OrderedDict([
          ('count', self.page.paginator.count),
          ('next', self.get_next_link()),
          ('previous', self.get_previous_link()),
          ('results', data),
          ('_links', links),
       ]))

class HateoasModelViewSet(viewsets.ModelViewSet):
    """
    This class should be inherited by viewsets that wants to provide hateoas links
    You should override following methodes:
      - get_list_links
      - get_retrieve_links
      - get_create_links
      - get_update_links
      - get_destroy_links
    """

    pagination_class = LinksAwarePageNumberPagination


    def get_list_links(self, request):
        return {}

    def get_retrieve_links(self, request, instance):
        return {}

    def get_create_links(self, request):
        return {}

    def get_update_links(self, request, instance):
        return {}

    def get_destroy_links(self, request, instance):
        return {}

    def get_paginated_response(self, data, links=None):
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data, links)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data, links=self.get_list_links())

        serializer = self.get_serializer(queryset, many=True)

        return Response(OrderedDict([
            ('results', serializer.data),
            ('_links', self.get_list_links(request))
        ]))

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        data = serializer.data
        data['_links'] = self.get_retrieve_links(request, instance)
        return Response(data)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = serializer.data
        data['_links'] = self.get_create_links(request)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        data = serializer.data
        data['_links'] = self.get_update_links(request, instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = {'_links': self.get_destroy_links(request, instance)}
        self.perform_destroy(instance)
        return Response(data, status=status.HTTP_204_NO_CONTENT)