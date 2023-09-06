import graphene
from graphene_django import DjangoObjectType
from .models import Deck, Game, QuantumStateCard, QuantumOperationCard

class QuantumStateCardType(DjangoObjectType):
    class Meta:
        model = QuantumStateCard
        fields = ("card_id", "theta", "phi")

class QuantumOperationCardType(DjangoObjectType):
    class Meta:
        model = QuantumOperationCard
        fields = ("card_id", "operation")

class DeckType(DjangoObjectType):
    class Meta:
        model = Deck
        fields = ("name", "state_cards", "operation_cards")

class GameType(DjangoObjectType):
    class Meta:
        model = Game
        fields = ("deck", "score")


class Query(graphene.ObjectType):
    state_cards = graphene.List(QuantumStateCardType)
    operation_cards = graphene.List(QuantumOperationCardType)
    deck = graphene.Field(DeckType)
    game = graphene.Field(GameType)

    def resolve_state_cards(self, info):
        return QuantumStateCard.objects.all()

    def resolve_operation_cards(self, info):
        return QuantumOperationCard.objects.all()

    def resolve_deck(self, info):
        return Deck.objects.first()

    def resolve_game(self, info):
        return Game.objects.first()