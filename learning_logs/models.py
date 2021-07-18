from django.db import models

class Topic(models.Model):
    """Topic that the user is studying."""
    text = models.CharField(max_length=200)
    date_added =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text
