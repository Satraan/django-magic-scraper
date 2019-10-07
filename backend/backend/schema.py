from graphene_django import DjangoObjectType
from magicscraper.models import Merchant
import graphene


# Create a GraphQL type for the actor model


class MerchantType(DjangoObjectType):
    class Meta:
        model = Merchant


class Query(graphene.ObjectType):
    merchants = graphene.List(MerchantType)

    def resolve_merchants(self, info):
        return Merchant.objects.all()


schema = graphene.Schema(query=Query)
