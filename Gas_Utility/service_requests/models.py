from django.db import models

class ServiceRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    customer_name = models.CharField(max_length=100)
    email = models.EmailField()
    request_type = models.CharField(max_length=100)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True) 
    updated_at = models.DateTimeField(auto_now=True)      
    resolved_at = models.DateTimeField(blank=True, null=True)  

    def save(self, *args, **kwargs):
       
        if self.status == 'Resolved' and not self.resolved_at:
            self.resolved_at = models.DateTimeField.now()
        super(ServiceRequest, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.customer_name} - {self.request_type}'
