from django.urls import path
from . import views

urlpatterns= [
    path('',views.home,name='home'),
    # path('detail/',views.detail,name='detail'),
    path('delete/<int:task_id>/',views.delete,name="delete"),
    path('update/<int:id>/', views.update, name="update"),
    path('cbv_home',views.Task_list_view.as_view(),name='cbv_home'),
    path('cbv_detail/<int:pk>/',views.Task_detail_view.as_view(),name='cbv_detail'),
    path('cbv_update/<int:pk>/',views.Task_update_view.as_view(),name='cbv_update'),
    path('cbv_delete/<int:pk>/',views.Task_delete_view.as_view(),name='cbv_delete'),
]