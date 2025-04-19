from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)
from drf_spectacular.utils import extend_schema, OpenApiResponse
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import ModelViewSet

from customers.forms import CustomerForm
from customers.models import Customer
from customers.serializers import CustomerSerializer


class CustomerViewSet(ModelViewSet):
    """API для управления контрактами."""

    queryset = Customer.objects.select_related("lead").select_related("contract").all()
    serializer_class = CustomerSerializer

    @extend_schema(
        summary="Получить список всех активных клиентов",
        responses=CustomerSerializer(many=True),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Получить одного активного клиента по ID",
        responses=CustomerSerializer,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Создать нового активного клиента",
        request=CustomerSerializer,
        responses={201: CustomerSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Полностью обновить активного клиента по ID",
        request=CustomerSerializer,
        responses=CustomerSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частично обновить активного клиента по ID",
        request=CustomerSerializer,
        responses=CustomerSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить активного клиента по ID",
        responses={
            HTTP_204_NO_CONTENT: OpenApiResponse(description="Активный клиент удален")
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class CustomersListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Представление для отображения списка всех активных клиентов.

    Доступно только для авторизованных пользователей.
    """

    permission_required = "customers.view_customer"
    template_name = "customers/customers-list.html"
    queryset = Customer.objects.select_related("lead").select_related("contract").all()
    context_object_name = "customers"


class CustomerDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации об активном клиенте.

    Доступно только для авторизованных пользователей.
    """

    permission_required = "customers.view_customer"
    template_name = "customers/customers-detail.html"
    model = Customer
    context_object_name = "object"


class CustomerCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Представление для создания нового активного клиента.

    Доступно только для авторизованных пользователей.
    После успешного создания перенаправляет на список всех активных клиентов.
    """

    permission_required = "customers.add_customer"
    template_name = "customers/customers-create.html"
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy("customers:customers_list")

    def form_valid(self, form):
        response = super().form_valid(form)

        lead = form.cleaned_data.get("lead")
        contract = form.cleaned_data.get("contract")

        if lead:
            lead.is_active = True
            lead.save()

        if contract:
            contract.is_signed = True
            contract.save()

        return response


class CustomerUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования существующего активного клиента.

    Доступно только для авторизованных пользователей.
    После успешного редактирования перенаправляет на страницу деталей.
    """

    permission_required = "customers.change_customer"
    template_name = "customers/customers-edit.html"
    model = Customer
    form_class = CustomerForm

    def get_success_url(self):
        return reverse("customers:customer_detail", kwargs={"pk": self.object.pk})

    def form_valid(self, form):
        response = super().form_valid(form)

        old_lead = self.get_object().lead
        old_contract = self.get_object().contract
        new_lead = form.cleaned_data.get("lead")
        new_contract = form.cleaned_data.get("contract")

        if old_lead != new_lead:
            if old_lead:
                old_lead.is_active = False
                old_lead.save()
            if new_lead:
                new_lead.is_active = True
                new_lead.save()

        if old_contract != new_contract:
            if old_contract:
                old_contract.is_signed = False
                old_contract.save()
            if new_contract:
                new_contract.is_signed = True
                new_contract.save()

        return response


class CustomerDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления активного клиента.

    Доступно только для авторизованных пользователей.
    После успешного удаления перенаправляет на список всех активных клиентов.
    """

    permission_required = "customers.delete_customer"
    template_name = "customers/customers-delete.html"
    model = Customer
    success_url = reverse_lazy("customers:customers_list")

    def form_valid(self, form):
        response = super().form_valid(form)

        lead = form.cleaned_data.get("lead")
        contract = form.cleaned_data.get("contract")

        if lead:
            lead.is_active = False
            lead.save()

        if contract:
            contract.is_signed = False
            contract.save()

        return response
