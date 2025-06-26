from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import (
    EspecialidadeViewSet,
    MedicoViewSet,
    PacienteViewSet,
    ConsultaViewSet,
    ExameViewSet,
    MedicamentoViewSet,
    ReceitaViewSet,
    ReceitaMedicamentoViewSet
)

router = DefaultRouter()
router.register(r'especialidades', EspecialidadeViewSet)
router.register(r'medicos', MedicoViewSet)
router.register(r'pacientes', PacienteViewSet)
router.register(r'consultas', ConsultaViewSet)
router.register(r'exames', ExameViewSet)
router.register(r'medicamentos', MedicamentoViewSet)
router.register(r'receitas', ReceitaViewSet)
router.register(r'receita-medicamentos', ReceitaMedicamentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
