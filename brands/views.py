from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework import generics
from . import models, forms, serializers


class BrandsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10
    permission_required = 'brands.view_brand'

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class BrandsCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Brand
    template_name = 'brand_create.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brands_list')
    permission_required = 'brands.add_brand'


class BrandsDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Brand
    template_name = 'brand_detail.html'
    permission_required = 'brands.view_brand'


class BrandsUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Brand
    template_name = 'brand_update.html'
    form_class = forms.BrandForm
    success_url = reverse_lazy('brands_list')
    permission_required = 'brands.change_brand'


class BrandsDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Brand
    template_name = 'brand_delete.html'
    success_url = reverse_lazy('brands_list')
    permission_required = 'brands.delete_brand'


class BrandCreateListAPIView(generics.ListCreateAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer


class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandSerializer
