from django.db import models

class Topic(models.Model):
    """Topic that the user is studying."""
    text = models.CharField(max_length=200)
    date_added =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returns a string representation of the model."""
        return self.text


class Entry(models.Model):
    """Information received by the user on the topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE,)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

        def __str__(self):
            """Returns the string view of the model."""
            return self.text[:50] + "..."
