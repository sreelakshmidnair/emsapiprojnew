from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views


router = DefaultRouter()

router.register(r'departments',views.DepartmentViewSet)
router.register(r'employees',views.EmployeeViewSet)
router.register(r'users',views.UserViewSet)
  


urlpatterns =[
    path("signup/",views.SignupAPIView.as_view() , name="user.signup"),
    path("login/",views.LoginAPIView.as_view() , name="user.login"),

  ]
#url patterns

urlpatterns = urlpatterns + router.urls