from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import Show, Booking
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            return render(request, 'register.html', {'error': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})

        User.objects.create_user(username=username, password=password)
        return redirect('login')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('show_list')  # Redirect to the booking page after login
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('login')

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

class ShowListView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'show_list.html', {'shows': shows})

@method_decorator(login_required, name='dispatch')
class BookTicketView(View):
    def get(self, request, show_id):
        show = Show.objects.get(id=show_id)
        return render(request, 'book_ticket.html', {'show': show})

    def post(self, request, show_id):
        show = Show.objects.get(id=show_id)
        seats = int(request.POST.get('seats'))

        if seats > show.available_seats:
            return render(request, 'book_ticket.html', {'show': show, 'error': 'Not enough seats available'})

        show.available_seats -= seats
        show.save()

        Booking.objects.create(user=request.user, show=show, seats=seats)
        return redirect('booking_history')

@method_decorator(login_required, name='dispatch')
class BookingHistoryView(View):
    def get(self, request):
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'booking_history.html', {'bookings': bookings})

@method_decorator(login_required, name='dispatch')
class AdminShowListView(View):
    def get(self, request):
        shows = Show.objects.all()
        return render(request, 'admin_show_list.html', {'shows': shows})

@method_decorator(login_required, name='dispatch')
class AdminShowCreateView(CreateView):
    model = Show
    fields = ['title', 'description', 'date', 'time', 'total_seats', 'available_seats']
    template_name = 'admin_show_form.html'
    success_url = reverse_lazy('admin_show_list')

@method_decorator(login_required, name='dispatch')
class AdminShowUpdateView(UpdateView):
    model = Show
    fields = ['title', 'description', 'date', 'time', 'total_seats', 'available_seats']
    template_name = 'admin_show_form.html'
    success_url = reverse_lazy('admin_show_list')

@method_decorator(login_required, name='dispatch')
class AdminShowDeleteView(DeleteView):
    model = Show
    template_name = 'admin_show_confirm_delete.html'
    success_url = reverse_lazy('admin_show_list')

@method_decorator(login_required, name='dispatch')
class AdminBookingListView(View):
    def get(self, request):
        bookings = Booking.objects.all()
        return render(request, 'admin_booking_list.html', {'bookings': bookings})

@method_decorator(login_required, name='dispatch')
class AdminDashboardView(View):
    def get(self, request):
        return render(request, 'admin_dashboard.html')
