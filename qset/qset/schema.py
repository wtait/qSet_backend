import graphene
import quantum_set.schema

class Query(quantum_set.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)