from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('trips/', views.trips_index, name='index'),
  path('trips/<int:trip_id>/', views.trips_detail, name='detail'),
  path('trips/create/', views.TripCreate.as_view(), name='trips_create'),
  path('trips/<int:pk>/update/', views.TripUpdate.as_view(), name='trips_update'),
  path('trips/<int:pk>/delete/', views.TripDelete.as_view(), name='trips_delete'),
  path('tasks/', views.tasks_index, name='taskpage'),
  path('trips/<int:trip_id>/add_tasks/', views.add_tasks, name='add_tasks'),
  path('trips/<int:trip_id>/add_savings/', views.add_savings, name='add_savings'),
  path('trips/<int:trip_id>/add_photo/', views.add_photo, name='add_photo'),
  # path('admin/', admin.site.urls),
  # path('', include('main_app.urls')),
  path('accounts/', include('django.contrib.auth.urls')),
  path('accounts/signup', views.signup, name='signup'),
]
