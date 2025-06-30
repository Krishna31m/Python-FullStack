from django.db import models
from django.core.exceptions import ValidationError
from datetime import timedelta, date
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, unique=True, blank=True, null=True)
    category = models.CharField(max_length=100, blank=True, null=True)
    publication_year = models.PositiveIntegerField(blank=True, null=True)
    copies_total = models.IntegerField(default=1)
    copies_available = models.IntegerField(default=1)

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Loan(models.Model):
    STATUS_CHOICES = [
        ('borrowed', 'Borrowed'),
        ('returned', 'Returned'),
    ]
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(blank=True)
    return_date = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowed')

    def clean(self):
        if self.return_date and self.return_date < self.loan_date:
            raise ValidationError("Return date cannot be before loan date.")

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = self.loan_date + timedelta(days=7)
        
        super().save(*args, **kwargs)

        # Handle fine logic
        if self.status == 'borrowed':
            # Not returned yet, check if overdue
            today = date.today()
            if today > self.due_date:
                days_late = (today - self.due_date).days
                amount = days_late * 10

                fine, created = Fine.objects.get_or_create(loan=self)
                fine.amount = amount
                fine.save()

        elif self.status == 'returned' and self.return_date and self.return_date > self.due_date:
            days_late = (self.return_date - self.due_date).days
            amount = days_late * 10
            fine, created = Fine.objects.get_or_create(loan=self)
            fine.amount = amount
            fine.save()


class Fine(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return f"₹{self.amount} Fine for Loan #{self.loan.id} - {'Paid' if self.paid else 'Unpaid'}"
