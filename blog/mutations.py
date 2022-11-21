import graphene
import graphql_jwt
from blog import models, types

class CreateUser(graphene.Mutation):
    user = graphene.Field(types.UserType)

    class Arguments:
        username = graphene.String(required=True)
        password = graphene.String(required=True)
        email = graphene.String(required=True)

    def mutate(self, info, username, password, email):
        user = models.User(
            username=username,
            email=email,
        )
        user.set_password(password)
        user.save()

        return CreateUser(user=user) 
    
class Mutation(graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
    
class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(types.UserType)
    
    @classmethod
    def resolve(cls, root, info, **kwarg):
        return cls(user=info.context.user)
    
class Mutation(graphene.ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    
