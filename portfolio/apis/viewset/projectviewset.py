from rest_framework import viewsets
from ..serializers.Project import ProjectSerializer
from ..models.project import Project 



class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
