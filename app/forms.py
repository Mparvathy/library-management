from django import forms
from .models import Book,customuser,BookIssue,BookRequest,BookIssueRequest
import datetime
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'isbn', 'author', 'category','cover','price','is_active']
        widgets = {
            'category': forms.Select(choices=Book.catchoice),
        }


class DiectBookIssueForm(forms.ModelForm):
    class Meta:
        model = BookIssue
        fields = ['student', 'book', 'due_date',]
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['student'].queryset = customuser.objects.filter(is_user=True)
        self.fields['book'].queryset = Book.objects.filter(is_active=True)
        self.fields['due_date'].input_formats = ['%d-%m-%Y']  
     



class DueDateForm(forms.Form):
    due_date = forms.DateField(widget=forms.SelectDateWidget())
class StudentSignupForm(forms.ModelForm):
    class Meta:
        model = customuser
        fields = ['username', 'first_name', 'email', 'password', 'phone', 'branch', 'enrollment']
        widgets = {
            'password': forms.PasswordInput(),
        }
    def save(self, commit=True):
        user = super(StudentSignupForm, self).save(commit=False)
        if commit:
            user.set_password(user.password)  # Ensure password is hashed
            user.is_user = True  # Set the user type as student
            user.save()
        return user

class BookRequestForm(forms.ModelForm):
    class Meta:
        model = BookRequest
        fields = ['book']

# forms.py

from django import forms
from .models import CartItem

class CartItemForm(forms.ModelForm):
    class Meta:
        model = CartItem
        fields = ['quantity']


class FinePaymentForm(forms.Form):
    fine_amount = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.TextInput(attrs={'readonly': 'readonly'}))
    payment_method = forms.ChoiceField(choices=[('credit_card', 'Credit Card'), ('paypal', 'PayPal')], required=True)
    account_number = forms.CharField(required=False)
    cvv = forms.CharField(required=False)
    # Add any other fields you need for the payment

    def __init__(self, *args, **kwargs):
        fine_amount = kwargs.pop('fine_amount', None)
        super(FinePaymentForm, self).__init__(*args, **kwargs)
        if fine_amount:
            self.fields['fine_amount'].initial = fine_amount

