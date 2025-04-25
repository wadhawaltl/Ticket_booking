from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ShowListView, BookTicketView, BookingHistoryView, AdminShowListView, AdminShowCreateView, AdminShowUpdateView, AdminShowDeleteView, AdminBookingListView, AdminDashboardView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('shows/', ShowListView.as_view(), name='show_list'),
    path('book/<int:show_id>/', BookTicketView.as_view(), name='book_ticket'),
    path('history/', BookingHistoryView.as_view(), name='booking_history'),
    path('admin/shows/', AdminShowListView.as_view(), name='admin_show_list'),
    path('admin/shows/add/', AdminShowCreateView.as_view(), name='admin_show_add'),
    path('admin/shows/edit/<int:pk>/', AdminShowUpdateView.as_view(), name='admin_show_edit'),
    path('admin/shows/delete/<int:pk>/', AdminShowDeleteView.as_view(), name='admin_show_delete'),
    path('admin/bookings/', AdminBookingListView.as_view(), name='admin_booking_list'),
    path('admin/dashboard/', AdminDashboardView.as_view(), name='admin_dashboard'),
]