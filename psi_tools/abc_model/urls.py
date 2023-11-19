from django.urls import path

# import .views as views
# from .views import *
from abc_model import views
from abc_model import views_crud

urlpatterns = [
    # path("", views.abc_test, name="abc_test"),
    # path("", views.abc, name="abc_list"),

#     list
#     path("", views.abc_list, name="abc_list"),
#     item
#     path("<int:id_model>/", views.abc_item, name="abc_item"),

#     C
#     path('create/', views.abc_create, name="abc_create"),
#     path('create/', views.ABCCreate.as_view(), name="abc_create"),
    # path('list/', views.ABCList.as_view(), name="abc_list"),
    path('list/', views_crud.ABCList.as_view(), name="abc_list"),
    path('<int:pk>/', views_crud.ABCDetail.as_view(), name="abc_item"),
#     CRUDE
#     path("add/", views_crud.AddABC.as_view(), name="abc_add"),
    path("create/", views_crud.CreateABC.as_view(), name="create_abc"),
    path("update/<int:pk>/", views_crud.UpdateABC.as_view(), name="update_abc"),
    path("delete/<int:pk>/", views_crud.DeleteABC.as_view(), name="delete_abc"),


]


