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

from contracts.forms import ContractForm
from contracts.models import Contract
from contracts.serializers import ContractSerializer


class ContractViewSet(ModelViewSet):
    """API для управления контрактами."""

    queryset = Contract.objects.select_related("product").all()
    serializer_class = ContractSerializer

    @extend_schema(
        summary="Получить список всех контрактов",
        responses=ContractSerializer(many=True),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Получить один контракт по ID",
        responses=ContractSerializer,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Создать новый контракт",
        request=ContractSerializer,
        responses={201: ContractSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Полностью обновить контракт по ID",
        request=ContractSerializer,
        responses=ContractSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частично обновить контракт по ID",
        request=ContractSerializer,
        responses=ContractSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить контракт по ID",
        responses={HTTP_204_NO_CONTENT: OpenApiResponse(description="Контракт удален")},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class ContractsListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    """
    Представление для отображения списка всех контрактов.

    Доступно только для авторизованных пользователей.
    """

    permission_required = "contracts.view_contract"
    template_name = "contracts/contracts-list.html"
    queryset = Contract.objects.select_related("product").all()
    context_object_name = "contracts"


class ContractDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации о контракте.

    Доступно только для авторизованных пользователей.
    """

    permission_required = "contracts.view_contract"
    template_name = "contracts/contracts-detail.html"
    model = Contract
    context_object_name = "object"


class ContractCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    """
    Представление для создания нового контракта.

    Доступно только для авторизованных пользователей.
    После успешного создания перенаправляет на список всех контрактов.
    """

    permission_required = "contracts.add_contract"
    template_name = "contracts/contracts-create.html"
    model = Contract
    form_class = ContractForm
    success_url = reverse_lazy("contracts:contracts_list")


class ContractUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    """
    Представление для редактирования существующего контракта.

    Доступно только для авторизованных пользователей.
    После успешного редактирования перенаправляет на страницу деталей.
    """

    permission_required = "contracts.change_contract"
    template_name = "contracts/contracts-edit.html"
    model = Contract
    form_class = ContractForm

    def get_success_url(self):
        return reverse("contracts:contracts_detail", kwargs={"pk": self.object.pk})


class ContractDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    """
    Представление для удаления контракта.

    Доступно только для авторизованных пользователей.
    После успешного удаления перенаправляет на список всех контрактов.
    """

    permission_required = "contracts.delete_contract"
    template_name = "contracts/contracts-delete.html"
    model = Contract
    success_url = reverse_lazy("contracts:contracts_list")
