import graphene

from projects.models import Project, ToDo
from users_app.models import Users
from .types import UsersType, ProjectType, ToDoType
from .mutations import Mutations


class Query(graphene.ObjectType):
    users = graphene.List(UsersType)
    projects = graphene.List(ProjectType)
    to_do = graphene.List(ToDoType)
    users_id = graphene.List(UsersType)
    projects_id = graphene.Field(ProjectType, id=graphene.Int())
    to_do_id = graphene.Field(ToDoType, id=graphene.Int())


    def resolve_users(root, info):
        """ пример запроса для users:
        {users{
            username
            firstName
            lastName
            email
            }
        }"""
        return Users.objects.all()


    def resolve_projects(root, info):
        """пример запроса для project:
        {projects{
            project
            gitLink
            isActive
            users{
                username
                }
            }
        }"""
        return Project.objects.all()


    def resolve_to_do(root, info):
        """пример запроса для todo:
            {toDo
                {
                    id
                    project {
                            project
                            }
                    noteText
                    users {
                            username
                            }
                    createdAt
                    updatedAt
                    isActive
                }
            }"""
        return ToDo.objects.all()


    def resolve_users_id(root, info, id=None):
        try:
            return Users.objects.get(id=id)
        except Users.DoesNotExists:
            return None


    def resolve_projects_id(root, info, id=None):
        """пример запроса:{
            projectsId(id:1){
                id
                project
                gitLink
                isActive
                users{
                    username
                }
            }
        }"""
        try:
            return Project.objects.get(id=id)
        except Project.DoesNotExist:
            return None


    def resolve_to_do_id(root, info, id=None):
        """пример запроса: {
        toDoId(id:1){
            project{
                project
                }
            noteText
            users{
                username
                }
            createdAt
            updatedAt
            isActive
            }
        }"""
        try:
            return ToDo.objects.get(id=id)
        except ToDo.DoesNotExist:
            return None


schema = graphene.Schema(query=Query, mutation=Mutations)
