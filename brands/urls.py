from django.urls import path
from . import views
urlpatterns = [
    path('brands/list/', views.BrandsListView.as_view(), name='brands_list'),
    path('brands/create/', views.BrandsCreateView.as_view(), name='brand_create'),
    path('brands/<int:pk>/detail/',
         views.BrandsDetailView.as_view(), name='brand_detail'),
    path('brands/<int:pk>/update/',
         views.BrandsUpdateView.as_view(), name='brand_update'),
    path('brands/<int:pk>/delete/',
         views.BrandsDeleteView.as_view(), name='brand_delete'),

    path('api/v1/brands/', views.BrandCreateListAPIView.as_view(),
         name='brands-create-list-api-view'),
    path('api/v1/brands/<int:pk>/', views.BrandRetrieveUpdateDestroyAPIView.as_view(),
         name='brands-detail-api-view'),
]
