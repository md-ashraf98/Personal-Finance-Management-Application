from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from .forms import SignUpForm, SignInForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .models import Transaction
from .forms import TransactionForm

# Cover Page View (Landing Page)
def cover_page(request):
    return render(request, 'finance_app/cover.html')

# Registration View (Handle both Sign-Up and Sign-In forms)
def registration(request):
    # Always initialize both forms
    sign_up_form = SignUpForm()
    sign_in_form = SignInForm()

    if request.method == 'POST':
        if 'sign_up' in request.POST:
            # Handle Sign-Up form submission
            sign_up_form = SignUpForm(request.POST)
            if sign_up_form.is_valid():
                user = sign_up_form.save(commit=False)
                user.set_password(sign_up_form.cleaned_data['password'])
                user.save()

                messages.success(request, "Registration successful! Please log in.")
                return redirect('sign_in')  # Redirect to sign-in page after successful registration

        elif 'sign_in' in request.POST:
            # Handle Sign-In form submission
            sign_in_form = SignInForm(request.POST)
            if sign_in_form.is_valid():
                username = sign_in_form.cleaned_data['username']
                password = sign_in_form.cleaned_data['password']
                user = authenticate(request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, "Login successful!")
                    return redirect('home')  # Redirect to home page after successful login
                else:
                    messages.error(request, "Invalid username or password.")

    return render(request, 'finance_app/registration.html', {
        'sign_up_form': sign_up_form,
        'sign_in_form': sign_in_form
    })

# Home page (after successful sign-up or sign-in)
def home(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.user = request.user  # Associate with the current user
            new_transaction.save()
            return redirect('home')  # After saving, reload the page to show the new transaction
    else:
        form = TransactionForm()

    # Get all transactions for the logged-in user
    transactions = Transaction.objects.filter(user=request.user)

    return render(request, 'finance_app/home.html', {'form': form, 'transactions': transactions})

# Add Transaction View
def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            new_transaction = form.save(commit=False)
            new_transaction.user = request.user  # Associate the transaction with the current logged-in user
            new_transaction.save()
            return redirect('home')  # Redirect to the home page after successfully adding the transaction
    else:
        form = TransactionForm()  # Initialize the empty form

    return render(request, 'finance_app/add_transaction.html', {'form': form})

# Edit Transaction
def edit_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)

    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to home page after editing the transaction
    else:
        form = TransactionForm(instance=transaction)

    return render(request, 'finance_app/edit_transaction.html', {'form': form})

# Delete Transaction
def delete_transaction(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    transaction.delete()
    return redirect('home')

# Sign-Up View (Direct redirection after submission)
def sign_up(request):
    if request.method == 'POST':
        # No validation, just redirect to home page
        return redirect('home')  # Redirect to home after sign-up form submission
    else:
        form = UserCreationForm()  # Empty sign-up form
    return render(request, 'finance_app/sign_up.html', {'form': form})

# Sign-In View (Direct redirection after submission)
def sign_in(request):
    if request.method == 'POST':
        # No authentication, just redirect to home page
        return redirect('home')  # Redirect to home after sign-in form submission
    else:
        form = AuthenticationForm()  # Empty sign-in form
    return render(request, 'finance_app/sign_in.html', {'form': form})

def transaction_history(request):
    transactions = Transaction.objects.filter(user=request.user).order_by('-date')
    return render(request, 'finance_app/transaction_history.html', {'transactions': transactions})
