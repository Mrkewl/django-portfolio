from rest_framework import routers

from .viewset.designviewset import DesignViewSet
from .viewset.userviewset import UserViewSet
from .viewset.projectviewset import ProjectViewSet

# from apis import views
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'designs', DesignViewSet)


# router.register(r'posts', PostViewSet)
# router.register(r'post', views.post_collection)


