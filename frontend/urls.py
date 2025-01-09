from . import views

urlpatterns = [
    path('home/', views.base, name='base'),
]