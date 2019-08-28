from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated

from suvorov_park.common.models import News
from .serializers import NewsSerializer


class NewsListAPIView(ListAPIView):
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    permission_classes = (IsAuthenticated,)
