from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('index/', views.index,name='index'),
    path('about/',views.about,name='about'),
    path('contact/', views.contact,name='contact'),
    path('comments/',views.comments,name='comments'),
    path('comments/<int:pk>/',views.CommentsDetailView.as_view(),name='comments_detail'),
    path('comments/<int:pk>/update',views.CommentsUpdateView.as_view(),name='commencts_update'),
    path('comments/<int:pk>/delete',views.CommentsDeleteView.as_view(),name='commencts_delete')

]
