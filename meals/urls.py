from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
urlpatterns = router.urls

urlpatterns += [
    path('product/', views.product_list, name='product_list'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/delete/', views.delete_product, name='delete_product'),
    path('product/update/', views.update_product, name='update_product'),
    path('product/get/', views.get_product, name='get_product'),

    path('meal/', views.meal_list, name='meal_list'),
    path('meal/create/', views.create_meal, name='create_meal'),
    path('meal/delete/', views.delete_meal, name='delete_meal'),
    path('meal/update/', views.update_meal, name='update_meal'),
    path('meal/get/', views.get_meal, name='get_meal'),

    path('<str:name>/category-list/', views.category_list, name='category_list'),
    path('<str:name>/create-category/', views.create_category, name='create_category'),
    path('<str:name>/delete-category/', views.delete_category, name='delete_category'),
    path('<str:name>/get-category/', views.get_category, name='get_category'),

    path('generate-pdf/', views.generate_pdf, name='generate_pdf'),

]
