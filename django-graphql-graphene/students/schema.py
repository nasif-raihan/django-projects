import graphene
from graphene_django import DjangoObjectType
from .models import Student


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "name", "email", "category")


class Query(graphene.ObjectType):
    students = graphene.List(StudentType)

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()


schema = graphene.Schema(query=Query)
