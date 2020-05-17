from rest_framework.generics import ListAPIView

from .serializers import rpaServerserializer
from .models import rpaserverConfig


class rpaserverlist(ListAPIView):
    queryset = rpaserverConfig.objects.all()
    serializer_class = rpaServerserializer