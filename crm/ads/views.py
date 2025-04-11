from django.contrib.auth.mixins import LoginRequiredMixin
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

from ads.forms import AdsForm
from ads.models import Ads
from ads.serializers import AdsSerializer


class AdsViewSet(ModelViewSet):
    """API для управления рекламными кампаниями."""

    queryset = Ads.objects.all()
    serializer_class = AdsSerializer

    @extend_schema(
        summary="Получить список всех рекламных кампаний",
        responses=AdsSerializer(many=True),
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @extend_schema(
        summary="Получить одну рекламную кампанию по ID",
        responses=AdsSerializer,
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @extend_schema(
        summary="Создать новую рекламную кампанию",
        request=AdsSerializer,
        responses={201: AdsSerializer},
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @extend_schema(
        summary="Полностью обновить рекламную кампанию по ID",
        request=AdsSerializer,
        responses=AdsSerializer,
    )
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @extend_schema(
        summary="Частично обновить рекламную кампанию по ID",
        request=AdsSerializer,
        responses=AdsSerializer,
    )
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @extend_schema(
        summary="Удалить рекламную кампанию по ID",
        responses={
            HTTP_204_NO_CONTENT: OpenApiResponse(
                description="Рекламная кампания удалена"
            )
        },
    )
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class AdsListView(LoginRequiredMixin, ListView):
    """
    Представление для отображения списка всех рекламных кампаний.

    Доступно только для авторизованных пользователей.
    """

    template_name = "ads/ads-list.html"
    queryset = Ads.objects.select_related("product")
    context_object_name = "ads"


class AdsDetailView(LoginRequiredMixin, DetailView):
    """
    Представление для отображения детальной информации о рекламной кампании.

    Доступно только для авторизованных пользователей.
    """

    template_name = "ads/ads-detail.html"
    model = Ads
    context_object_name = "object"


class AdsCreateView(LoginRequiredMixin, CreateView):
    """
    Представление для создания новой рекламной кампании.

    Доступно только для авторизованных пользователей.
    После успешного создания перенаправляет на список всех рекламных кампаний.
    """

    template_name = "ads/ads-create.html"
    model = Ads
    form_class = AdsForm
    success_url = reverse_lazy("ads:ads_list")


class AdsUpdateView(LoginRequiredMixin, UpdateView):
    """
    Представление для редактирования существующей рекламной кампании.

    Доступно только для авторизованных пользователей.
    После успешного редактирования перенаправляет на страницу деталей.
    """

    template_name = "ads/ads-edit.html"
    model = Ads
    form_class = AdsForm

    def get_success_url(self):
        return reverse("ads:ads_details", kwargs={"pk": self.object.pk})


class AdsDeleteView(LoginRequiredMixin, DeleteView):
    """
    Представление для удаления рекламной кампании.

    Доступно только для авторизованных пользователей.
    После успешного удаления перенаправляет на список всех рекламных кампаний.
    """

    template_name = "ads/ads-delete.html"
    model = Ads
    success_url = reverse_lazy("ads:ads_list")
