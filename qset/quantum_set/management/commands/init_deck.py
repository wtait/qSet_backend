from django.core.management.base import BaseCommand
from quantum_set.models import QuantumStateCard, QuantumOperationCard, Deck

class Command(BaseCommand):
    help = 'Initializes the deck with the cards'

    # Clear existing deck if any
    def handle(self, *args, **kwargs):
        QuantumStateCard.objects.all().delete()
        QuantumOperationCard.objects.all().delete()
        Deck.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared deck'))

        # Create the state cards
        for theta in range(0, 360, 90):
            for phi in range(0, 360, 90):
                QuantumStateCard.objects.create(theta=theta, phi=phi)

        # Create the operation cards
        for operation in ['X', 'Y', 'Z', 'H']:
            QuantumOperationCard.objects.create(operation=operation)

        # Create the deck
        deck = Deck.objects.create(name='Default Deck')
        deck.state_cards.set(QuantumStateCard.objects.all())
        deck.operation_cards.set(QuantumOperationCard.objects.all())

        self.stdout.write(self.style.SUCCESS('Successfully initialized deck'))

