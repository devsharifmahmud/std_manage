from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('home/', home),
]