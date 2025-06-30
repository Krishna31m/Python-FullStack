from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, TemplateView
)
from django.urls import reverse_lazy
from django.utils import timezone
from .models import Book, Member, Loan, Fine
from django.core.exceptions import ValidationError


# -------------------- HOME --------------------
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_count'] = Book.objects.count()
        context['member_count'] = Member.objects.count()
        context['loan_count'] = Loan.objects.count()
        context['fine_count'] = Fine.objects.count()
        return context


# -------------------- BOOK --------------------
class BookListView(ListView):
    model = Book
    template_name = 'books/list.html'
    context_object_name = 'books'
    paginate_by = 10

class BookCreateView(CreateView):
    model = Book
    template_name = 'books/create.html'
    fields = '__all__'
    success_url = reverse_lazy('book_list')

class BookUpdateView(UpdateView):
    model = Book
    template_name = 'books/update.html'
    fields = '__all__'
    success_url = reverse_lazy('book_list')

class BookDeleteView(DeleteView):
    model = Book
    template_name = 'books/delete.html'
    success_url = reverse_lazy('book_list')


# -------------------- MEMBER --------------------
class MemberListView(ListView):
    model = Member
    template_name = 'members/list.html'
    context_object_name = 'members'

class MemberCreateView(CreateView):
    model = Member
    template_name = 'members/create.html'
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('member_list')

class MemberUpdateView(UpdateView):
    model = Member
    template_name = 'members/update.html'
    fields = ['name', 'email', 'phone', 'address']
    success_url = reverse_lazy('member_list')

class MemberDeleteView(DeleteView):
    model = Member
    template_name = 'members/delete.html'
    success_url = reverse_lazy('member_list')



# -------------------- LOAN --------------------
class LoanListView(ListView):
    model = Loan
    template_name = 'loans/list.html'
    context_object_name = 'loans'

class LoanCreateView(CreateView):
    model = Loan
    template_name = 'loans/create.html'
    fields = ['book', 'member', 'due_date']  # Exclude loan_date

    success_url = reverse_lazy("loan_list")

    def get_initial(self):
        initial = super().get_initial()
        book_id = self.request.GET.get('book_id')
        if book_id:
            initial['book'] = book_id
        return initial

    def form_valid(self, form):
        book = form.cleaned_data['book']
        if book.copies_available > 0:
            book.copies_available -= 1
            book.save()
            return super().form_valid(form)
        else:
            form.add_error('book', 'No copies available')
            return self.form_invalid(form)

class LoanReturnView(UpdateView):
    model = Loan
    fields = []
    template_name = 'loans/return.html'
    success_url = reverse_lazy("loan_list")

    def form_valid(self, form):
        loan = form.save(commit=False)

        # Automatically set today's return date and update status
        today = timezone.now().date()
        loan.return_date = today
        loan.status = 'returned'

        # Increase available book copies
        loan.book.copies_available += 1
        loan.book.save()

        # Compare both dates properly
        if loan.return_date > loan.due_date:
            days_late = (loan.return_date - loan.due_date).days
            fine_amount = days_late * 10

            # Avoid duplicate fines for same loan
            if not Fine.objects.filter(loan=loan).exists():
                Fine.objects.create(loan=loan, amount=fine_amount)

        loan.save()
        return super().form_valid(form)


class LoanUpdateView(UpdateView):
    model = Loan
    template_name = 'loans/update.html'
    fields = ['loan_date', 'due_date', 'return_date', 'status']
    success_url = reverse_lazy("loan_list")

class LoanDeleteView(DeleteView):
    model = Loan
    template_name = 'loans/delete.html'
    success_url = reverse_lazy("loan_list")



# -------------------- FINE --------------------
class FineListView(ListView):
    model = Fine
    template_name = 'fines/list.html'
    context_object_name = 'fines'

    def get_queryset(self):
        queryset = Fine.objects.select_related('loan__book', 'loan__member')
        status = self.request.GET.get('status')
        if status == 'unpaid':
            return queryset.filter(paid=False)
        elif status == 'paid':
            return queryset.filter(paid=True)
        return queryset

class FineDeleteView(DeleteView):
    model = Fine
    template_name = 'fines/delete.html'
    success_url = reverse_lazy('fine_list')
