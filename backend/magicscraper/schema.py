import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from magicscraper.models import Merchant

# Create a GraphQL type for the actor model


class MerchantType(DjangoObjectType):
    class Meta:
        model = Merchant

# Create a Query type


class Query(ObjectType):
    actor = graphene.Field(ActorType, id=graphene.Int())
    movie = graphene.Field(MovieType, id=graphene.Int())
    actors = graphene.List(ActorType)
    movies = graphene.List(MovieType)

    def resolve_merchant(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Merchant.objects.get(pk=id)

        return None

	def resolve_merchants(self, info, **kwargs):
     return Merchant.objects.all()
