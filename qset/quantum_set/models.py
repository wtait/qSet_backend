from django.db import models

class QuantumStateCard(models.Model):
    '''
        A quantum state card describes a point on the Bloch sphere,
        represented by the angles theta (from the z-axis) and phi (from the x-axis).
    '''
    card_id = models.AutoField(primary_key=True)
    theta = models.FloatField()  # Angle from z-axis
    phi = models.FloatField()    # Angle from x-axis

    def __str__(self):
        return f"QuantumStateCard {self.card_id}: Theta {self.theta}, Phi {self.phi}"

class QuantumOperationCard(models.Model):
    '''
        A quantum operation card represents a quantum operation like Pauli-X, Pauli-Y, etc.
    '''
    OPERATION_CHOICES = [
        ('X', 'Pauli-X'),
        ('Y', 'Pauli-Y'),
        ('Z', 'Pauli-Z'),
        ('H', 'Hadamard'),
        # Add more as needed
    ]
    card_id = models.AutoField(primary_key=True)
    operation = models.CharField(max_length=20, choices=OPERATION_CHOICES)

    def __str__(self):
        return f"QuantumOperationCard {self.card_id}: Operation {self.operation}"

class Deck(models.Model):
    '''
        A deck is a collection of state and operation cards, used for gameplay.
    '''
    name = models.CharField(max_length=100)
    state_cards = models.ManyToManyField(QuantumStateCard)
    operation_cards = models.ManyToManyField(QuantumOperationCard)

    def __str__(self):
        return self.name

class Game(models.Model):
    '''
        The game model holds the current state of the game, including the deck used and the score.
    '''
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    # Other fields can be added as needed, such as time_remaining, etc.

    def __str__(self):
        return f"Game using {self.deck.name} with score {self.score}"

