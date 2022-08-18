from .views import MadklubViewSet
# from django.urls import path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("madklub", MadklubViewSet)
urlpatterns = router.urls


# urlpatterns = [
#     path('', MadklubView.as_view(), name='madklubs')
# ]
