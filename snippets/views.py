from django.contrib.auth.models import User
from snippets.models import Snippet
from snippets.serializers import SnippetSerializer, UserSerializer, SearchSerializer
from snippets.permissions import IsOwnerOrReadOnly
from rest_framework import renderers
from rest_framework import permissions
from django.shortcuts import redirect
from rest_framework.response import Response
from rest_framework.decorators import detail_route
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,)

    # We want to be explicit with 'get' method here, but it's the default anyways
    @detail_route(methods=['get'], renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SearchView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'search.html'

    def get(self, request):
        serializer = SearchSerializer()
        return Response({'serializer': serializer})

    def post(self, request):
        data = request.data
        serializer = SearchSerializer(data=data)
        if not serializer.is_valid():
            return Response({'serializer': serializer})
        return redirect('snippet-list')
