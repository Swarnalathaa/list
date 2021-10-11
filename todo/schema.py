import graphene
from graphene_django import DjangoObjectType
from .models import CustomUser, TodoList 
from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

class UserType(DjangoObjectType):
    class Meta: 
        model = CustomUser
        fields = ('id','name')

  
class TodoListType(DjangoObjectType):
    class Meta: 
        model = TodoList
        fields = (
            'id',
            'title',
            'content', 
            'user',
        )  


class Query(UserQuery, MeQuery,graphene.ObjectType):
    TodoLists = graphene.List(TodoListType)

    def resolve_TodoLists(root, info, **kwargs):
        # Querying a list
        return TodoList.objects.all()


class TodoInput(graphene.InputObjectType):
    title = graphene.String()
    content = graphene.String()
    user = graphene.String()

class CreateTodo(graphene.Mutation):
    class Arguments:
        input = TodoInput(required=True)
    todo = graphene.Field(TodoListType)
    @classmethod
    def mutate(cls, root, info, input):
        todo = TodoList()
        todo.title = input.title
        todo.user = input.user
        todo.content = input.content
        todo.save()
        return CreateTodo(todo=todo)

class AuthMutation(graphene.ObjectType):
   register = mutations.Register.Field()
   verify_account = mutations.VerifyAccount.Field()
   token_auth = mutations.ObtainJSONWebToken.Field()

class Mutation(AuthMutation ,graphene.ObjectType):
    create_todo = CreateTodo.Field()
    pass
schema = graphene.Schema(query=Query, mutation=Mutation)