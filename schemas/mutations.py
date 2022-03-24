import graphene

from projects.models import Project, ToDo
from users_app.models import Users
from .types import ProjectType, ToDoType, UsersType


class ProjectUpdateMutation(graphene.Mutation):
    class Arguments:
        git_link = graphene.String(required=True)
        is_active = graphene.Boolean()
        id = graphene.ID()

    projects = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, git_link, is_active, id):
        """пример запроса:
            mutation updateProject{
                updateProject(id:20, gitLink:"www.TEST!.com", isActive:false){
                    projects{
                        project
                        id
                        gitLink
                        isActive
                    }
                }
            }"""
        projects = Project.objects.get(id=id)
        projects.git_link = git_link
        projects.is_active = is_active
        projects.save()
        return ProjectUpdateMutation(projects=projects)


class ProjectCreateMutation(graphene.Mutation):
    class Arguments:
        project = graphene.String(required=True)
        git_link = graphene.String()


    projects = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, project, git_link):
        """пример запроса:
        mutation createProject{
            createProject(project:"test", gitLink:"www.test.ru"){
                projects{
                    id
                    project
                    gitLink
                    isActive
                    users{
                      username
                    }
                }
            }
        }"""
        projects = Project(project=project, git_link=git_link)
        projects.save()
        return ProjectUpdateMutation(projects=projects)


class ProjectDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    projects = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, id):
        """пример запроса: mutation deleteProject{
                deleteProject(id:39){
                    projects{
                        project
                    }
                }
            }"""
        Project.objects.get(id=id).delete()
        return ProjectDeleteMutation(projects=None)


class ToDoUpdateMutation(graphene.Mutation):
    class Arguments:
        note_text = graphene.String()
        is_active = graphene.Boolean()
        id = graphene.ID()

    to_do = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, note_text, id, is_active):
        """пример запроса:mutation updateToDo{
                updateToDo(id:11, noteText:"changed!", isActive:false){
                    toDo{
                        project{
                        project
                        }
                    noteText
                    isActive
                    createdAt
                    updatedAt
                        users{
                        username
                        }
                    }
                }
            }

        """
        to_do = ToDo.objects.get(id=id)
        to_do.note_text = note_text
        to_do.is_active = is_active
        to_do.save()
        return ToDoUpdateMutation(to_do=to_do)


class ToDoCreateMutation(graphene.Mutation):
    class Arguments:
        note_text = graphene.String(required=True)
        project_id = graphene.ID(required=True)
        users_id = graphene.ID(required=True)

    to_do = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, note_text, project_id, users_id):
        """пример запроса: mutation createToDo{
                createToDo(noteText:"here new note!", projectId:1, usersId:12){
                    toDo{
                    id
                    project{
                        project
                        }
                    noteText
                    isActive
                    createdAt
                    updatedAt
                    users {
                        id
                        }
                    }
                }
            }"""
        project = Project.objects.get(id=project_id)
        users = Users.objects.get(id=users_id)
        to_do = ToDo(note_text=note_text, project=project, users=users)
        to_do.save()
        return ToDoCreateMutation(to_do=to_do)


class ToDoDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID()

    to_do = graphene.Field(ToDoType)

    @classmethod
    def mutate(cls, root, info, id):
        """пример запроса: mutation deleteToDo{
                deleteToDo(id:11){
                    toDo{
                    n   oteText
                    }
                }
            }"""
        ToDo.objects.get(id=id).delete()
        return ToDoDeleteMutation(to_do=None)


class Mutations(graphene.ObjectType):
    update_project = ProjectUpdateMutation.Field()
    create_project = ProjectCreateMutation.Field()
    delete_project = ProjectDeleteMutation.Field()
    update_to_do = ToDoUpdateMutation.Field()
    create_to_do = ToDoCreateMutation.Field()
    delete_to_do = ToDoDeleteMutation.Field()
