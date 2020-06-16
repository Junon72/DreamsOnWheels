from django.db import models

CONTACT_STATUS_CHOICES = [
    ('n', 'New'),
    ('r', 'Sales read'),
    ('f', 'Sales follow'),
    ('d', 'Sales done'),
    ('c', 'Contributor request'),
    ('e', 'Contributor in exchange'),
    ('a', 'Contributor done'),
    ('or', 'Other read'),
    ('of', 'Other follow'),
    ('od', 'Other done')
]


class Contact(models.Model):
    name = models.CharField(max_length=100, blank=False)
    from_email = models.CharField(max_length=100, blank=False)
    subject = models.CharField(max_length=100, blank=False)
    message = models.CharField(max_length=500, blank=False)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(
        max_length=2, choices=CONTACT_STATUS_CHOICES, default='n'
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.subject}-{self.date}"