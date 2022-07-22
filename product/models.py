from django.db import models


class Category(models.Model):

    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        blank=True,
        null=True,
        related_name='child',
        on_delete=models.CASCADE
        )

    def __str__(self):
        parent_path = [self.name]
        parent_ = self.parent

        while parent_ is not None:
            parent_path.append(parent_.name)
            parent_ = parent_.parent

        return ' > '.join(parent_path[::-1])

class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.ManyToManyField(Category)

    def __str__(self):
        return '{} | Category {}'.format(self.name, self.category)