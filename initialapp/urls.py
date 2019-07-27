from djangosample.initialapp.views import *
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register(r'eproduct',ProductVset,basename='eproduct')
router.register(r'evendor',VendorVset,basename='evendor')

urlpatterns=router.urls