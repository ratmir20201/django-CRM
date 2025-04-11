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

from leads.forms import LeadForm
from leads.models import Lead
from leads.serializers import LeadSerializer


class LeadViewSet(ModelViewSet):
    """API для управления потенциальными клиентами (lead)."""

    queryset = Lead.objects.select_related("ad").all()
    serializer_class = LeadSerializer

    @extend_schema(
        summary="Получить список всех потенциальных клиентов",
        responses=LeadSerializer(many=True),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Получить одного потенциального клиента по ID",
        responses=LeadSerializer,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Создать нового потенциального клиента",
        request=LeadSerializer,
        responses={201: LeadSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Полностью обновить потенциального клиента по ID",
        request=LeadSerializer,
        responses=LeadSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частично обновить потенциального клиента по ID",
        request=LeadSerializer,
        responses=LeadSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить потенциального клиента по ID",
        responses={HTTP_204_NO_CONTENT: OpenApiResponse(description="Услуга удалена")},
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class LeadCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания нового потенциального клиента.

    Доступно только для авторизованных пользователей.
    После успешного создания перенаправляет на список потенциальных клиентов.
    """

    template_name = "leads/leads-create.html"
    model = Lead
    form_class = LeadForm
    success_url = reverse_lazy("leads:leads_list")


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    """
    Представление для редактирования существующего потенциального клиента.

    Доступно только для авторизованных пользователей.
    После успешного редактирования перенаправляет на страницу деталей
    потенциального клиента.
    """

    template_name = "leads/leads-edit.html"
    model = Lead
    form_class = LeadForm

    def get_success_url(self):
        return reverse(
            "leads:lead_detail",
            kwargs={"pk": self.object.pk},
        )


class LeadDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление для удаления потенциального клиента.

    Доступно только для авторизованных пользователей.
    После успешного удаления перенаправляет на список потенциальных клиентов.
    """

    template_name = "leads/leads-delete.html"
    model = Lead
    success_url = reverse_lazy("leads:leads_list")


class LeadsListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения списка всех потенциальных клиентов.

    Доступно только для авторизованных пользователей.
    """

    template_name = "leads/leads-list.html"
    model = Lead
    context_object_name = "leads"


class LeadDetailView(LoginRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации об потенциальном клиенте.

    Доступно только для авторизованных пользователей.
    """

    template_name = "leads/leads-detail.html"
    model = Lead
    context_object_name = "object"
