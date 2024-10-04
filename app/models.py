from django.db import models
from django.contrib.auth.models import User
from  django.contrib.auth.models import AbstractUser
from django.utils import timezone

class customuser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_admin = models.BooleanField(default=False)
    is_user = models.BooleanField(default=False)
    branch = models.CharField(max_length=100, blank=True)  # Make sure this field exists
    enrollment = models.CharField(max_length=15, blank=True, null=True)
    def has_admin_permission(self):
        return self.is_admin


class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('history', 'History'),
        ('novel', 'Novel'),
        ('fantasy', 'Fantasy'),
        ('thriller', 'Thriller'),
        ('romance', 'Romance'),
        ('scifi','Sci-Fi')
        ]
    name=models.CharField(max_length=30)
    isbn=models.PositiveIntegerField()
    author=models.CharField(max_length=40)
    price = models.DecimalField(max_digits=10, decimal_places=2)  
    category=models.CharField(max_length=30,choices=catchoice,default='education')
    cover = models.ImageField(upload_to='app/cover', null=True, blank=True)
    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_sold = models.BooleanField(default=False)  # Add this field
    sold_to = models.ForeignKey(customuser, on_delete=models.SET_NULL, null=True, blank=True, related_name='purchased_books')
    is_issued= models.BooleanField(default=False)  # Add this field
    def delete(self, *args, **kwargs):
        # Handle the deletion of related BookIssue records
        # For example, set the book field to null in BookIssue
        BookIssue.objects.filter(book=self).update(book=None)
        super().delete(*args, **kwargs)

    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


class Order(models.Model):
    user = models.ForeignKey(customuser, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=255)
    address = models.TextField()
    cvv = models.CharField(max_length=4)  # Adjust length as needed
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    is_sold = models.BooleanField(default=False)
 
    def __str__(self):
        return f"Order {self.id} by {self.user.username}"



class BookIssue(models.Model):
    student = models.ForeignKey(customuser, on_delete=models.CASCADE, limit_choices_to={'is_user': True})
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)  #
    is_active = models.BooleanField(default=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)  # Add this line
    fine = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)  # Add this field
    is_sold = models.BooleanField(default=False)
    fine_paid = models.BooleanField(default=False)  # Add this field
    def __str__(self):
        return f'{self.book.name} issued to {self.student.username} on {self.issue_date}'
    
    def is_overdue(self):
        if self.return_date is None and self.due_date is not None:
            return timezone.now().date() > self.due_date
        return False
    
    def calculate_fine(self):
        if not self.is_returned:
            today = timezone.now().date()
            if today > self.due_date:
                overdue_days = (today - self.due_date).days
                # Define your fine calculation logic
                fine_amount = overdue_days * 10  # Example: 10 units of currency per overdue day
                return fine_amount
        return 0
 
class BookRequest(models.Model):
    student = models.ForeignKey(customuser, on_delete=models.CASCADE, limit_choices_to={'is_user': True})
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    request_date = models.DateField(default=timezone.now)
    is_approved = models.BooleanField(default=False)
    is_issued = models.BooleanField(default=False)
    
    issued_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'Request by {self.student.username} for {self.book.name} on {self.request_date}'

class BookIssueRequest(models.Model):
    student = models.ForeignKey(customuser, on_delete=models.CASCADE, limit_choices_to={'is_user': True})
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField(null=True, blank=True)
    return_date = models.DateField(null=True, blank=True)
    is_returned = models.BooleanField(default=False)  #
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.book.name} issued to {self.student.username} on {self.issue_date}'
    
    def is_overdue(self):
        if self.return_date is None and self.due_date is not None:
            return timezone.now().date() > self.due_date
        

class Cart(models.Model):
    user = models.ForeignKey(customuser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cart for {self.user.username} created on {self.created_at}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.book.name} in cart"

