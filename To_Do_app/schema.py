import graphene

from graphene_django import DjangoObjectType

from projects.models import Project, ToDo
from users_app.models import Users


class Query(graphene.ObjectType):
    hello = graphene.String(default_value='Hi!')


schema = graphene.Schema(query=Query)