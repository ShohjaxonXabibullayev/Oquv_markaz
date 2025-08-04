from django.urls import path
from .views import *

#APIView uchun
# urlpatterns = [
#     path('', OquvmarkazAPIView.as_view(), name='ListCreate'),
#     # path('detail/<int:pk>/', DetailUpdateDlete.as_view(), name='detail')
# ]

#GenericAPIView (mixinsiz) uchun
# urlpatterns = [
#     path('', Oquv_markazAPIView.as_view(), name='ListAPI')
# ]

#GenericAPIView (mixins bilan)
urlpatterns = [
    path('', Oquv_markaz_mixins.as_view(), name='mixins')
]