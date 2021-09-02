from django.urls import path

from .views import LoginView, RegistrationView, LogoutView, ActivationView, ChangePasswordView, ForgotPasswordView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('activation/', ActivationView.as_view()),
    path('changepass/', ChangePasswordView.as_view()),
    path('forgotpass/', ForgotPasswordView.as_view()),
]