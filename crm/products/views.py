from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet

from products.forms import ProductForm
from products.models import Product
from products.serializers import ProductSerializer


class ProductViewSet(ModelViewSet):
    """API для управления услугами (услуги = продукты в системе)."""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @extend_schema(
        summary="Получить список всех услуг",
        responses=ProductSerializer(many=True),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Получить одну услугу по ID",
        responses=ProductSerializer,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Создать новую услугу",
        request=ProductSerializer,
        responses={201: ProductSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Полностью обновить услугу по ID",
        request=ProductSerializer,
        responses=ProductSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частично обновить услугу по ID",
        request=ProductSerializer,
        responses=ProductSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить услугу по ID",
        responses={HTTP_204_NO_CONTENT: OpenApiResponse(description="Услуга удалена")},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ProductCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания новой услуги.

    Доступно только для авторизованных пользователей.
    После успешного создания перенаправляет на список услуг.
    """

    template_name = "products/products-create.html"
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("products:products_list")


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """
    Представление для редактирования существующей услуги.

    Доступно только для авторизованных пользователей.
    После успешного редактирования перенаправляет на страницу деталей услуги.
    """

    template_name = "products/products-edit.html"
    model = Product
    form_class = ProductForm

    def get_success_url(self):
        return reverse(
            "products:product_detail",
            kwargs={"pk": self.object.pk},
        )


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление для удаления услуги.

    Доступно только для авторизованных пользователей.
    После успешного удаления перенаправляет на список услуг.
    """

    template_name = "products/products-delete.html"
    model = Product
    success_url = reverse_lazy("products:products_list")


class ProductsListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения списка всех услуг.

    Доступно только для авторизованных пользователей.
    """

    template_name = "products/products-list.html"
    model = Product
    context_object_name = "products"


class ProductDetailView(LoginRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации об услуге.

    Доступно только для авторизованных пользователей.
    """

    template_name = "products/products-detail.html"
    model = Product
    context_object_name = "object"
