from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from .models import Especialidade, Medico, Paciente, Consulta, Exame, Medicamento, Receita, ReceitaMedicamento
from .serializers import EspecialidadeSerializer, MedicoSerializer, PacienteSerializer, ConsultaSerializer, ExameSerializer, MedicamentoSerializer, ReceitaSerializer, ReceitaMedicamentoSerializer

class EspecialidadeViewSet(ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class MedicoViewSet(ModelViewSet):
    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer


class PacienteViewSet(ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer

class ConsultaViewSet(ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer

class ExameViewSet(ModelViewSet):
    queryset = Exame.objects.all()
    serializer_class = ExameSerializer

class MedicamentoViewSet(ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer

class ReceitaViewSet(ModelViewSet):
    queryset = Receita.objects.all()
    serializer_class = ReceitaSerializer

class ReceitaMedicamentoViewSet(ModelViewSet):
    queryset = ReceitaMedicamento.objects.all()
    serializer_class = ReceitaMedicamentoSerializer

