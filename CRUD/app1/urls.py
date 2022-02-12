from django.urls import path
from .views import courseView,studentView,studentdataView,editView,removeView


urlpatterns = [

    path('student/', studentView, name='studentview'),
    path('course/', courseView, name='courseview'),
    path('studentdata/', studentdataView, name='studentdata'),
    path('edit/<int:id>/', editView, name='edit'),
    path('remove/<int:id>/', removeView, name='remove')

]