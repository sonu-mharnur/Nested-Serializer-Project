from django.urls import path
# from rest_framework.authtoken import views
from .views import InstructorListView,CourseListView,CourseDetailView,InstructorDetailView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('Instructor/', InstructorListView.as_view(), name='home'),
    path('courses/', CourseListView.as_view(), name='home'),
    path('courses/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('Instructor/<int:pk>', InstructorDetailView.as_view(), name='course-detail'),
    # path('api-token-auth/', views.obtain_auth_token),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
