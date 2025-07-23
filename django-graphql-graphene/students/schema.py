import graphene
from graphene_django import DjangoObjectType
from .models import Student


class StudentType(DjangoObjectType):
    class Meta:
        model = Student
        fields = ("id", "name", "email", "category")


class Query(graphene.ObjectType):
    students = graphene.List(StudentType)
    student = graphene.Field(StudentType, id=graphene.Int(required=True))

    def resolve_students(self, info, **kwargs):
        return Student.objects.all()

    def resolve_student(self, info, id):
        try:
            return Student.objects.get(pk=id)
        except Student.DoesNotExist:
            return None


class CreateStudent(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        email = graphene.String(required=True)
        category = graphene.String(required=True)

    student = graphene.Field(StudentType)

    def mutate(self, info, name, email, category):
        student = Student(name=name, email=email, category=category)
        student.save()

        # noinspection PyArgumentList
        return CreateStudent(student=student)


class UpdateStudent(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)
        name = graphene.String()
        email = graphene.String()
        category = graphene.String()

    student = graphene.Field(StudentType)

    def mutate(self, info, id, name=None, email=None, category=None):
        try:
            student = Student.objects.get(pk=id)
        except Student.DoesNotExist:
            return None

        if name is not None:
            student.name = name
        if email is not None:
            student.email = email
        if category is not None:
            student.category = category

        student.save()

        return UpdateStudent(student=student)  # type: ignore


class DeleteStudent(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, id):
        try:
            student = Student.objects.get(pk=id)
            student.delete()
            return DeleteStudent(ok=True)  # type: ignore
        except Student.DoesNotExist:
            return DeleteStudent(ok=False)  # type: ignore


class Mutation(graphene.ObjectType):
    create_student = CreateStudent.Field()
    update_student = UpdateStudent.Field()
    delete_student = DeleteStudent.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
