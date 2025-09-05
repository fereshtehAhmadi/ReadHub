from rest_framework.routers import DefaultRouter

from src.apps.user.v1.presentation.admin.setting.library_employee import EmployeeViewSet

router = DefaultRouter()
router.register(r"settings/library-employee", EmployeeViewSet, basename="employee")
urlpatterns = router.urls
