from django.db import models

class QuantumStateCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    theta = models.FloatField()  # Angle from z-axis
    phi = models.FloatField()    # Angle from x-axis

    def __str__(self):
        return f"QuantumStateCard {self.card_id}: Theta {self.theta}, Phi {self.phi}"

class QuantumOperationCard(models.Model):
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
