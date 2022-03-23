import graphene

from graphene_django import DjangoObjectType

from projects.models import Project, ToDo
from users_app.models import Users


class UsersType(DjangoObjectType):
    class Meta:
        model = Users
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class Query(graphene.ObjectType):
    users = graphene.List(UsersType)
    projects = graphene.List(ProjectType)
    to_do = graphene.List(ToDoType)
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



schema = graphene.Schema(query=Query)
