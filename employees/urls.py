from django.urls import path

from .views import CreateRetrieveUpdateDeleteEmployeeView, EmployeeListAPIView

urlpatterns = [
    path('api/v1/employees', CreateRetrieveUpdateDeleteEmployeeView.as_view()),
    path('api/v1/employees/list', EmployeeListAPIView.as_view()),
   # path('api/v1/employees/<int:pk>', CreateRetrieveUpdateDeleteEmployeeView.as_view())
    ]