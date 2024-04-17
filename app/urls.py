from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as as_view
from .forms import LoginForm,MyPasswordChangeForm,MyPasswordResetForm,MySetPasswordForm
urlpatterns = [
    path('',views.ProductView.as_view(),name='home'),
    path('product-detail/<int:pk>/', views.ProductDetailsView.as_view(), name='product-detail'),
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),


    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('mobile/', views.mobile, name='mobile'),
    path('accounts/login/',as_view.LoginView.as_view(template_name = 'app/login.html',authentication_form=LoginForm), name='login'),
    path('logout/',as_view.LogoutView.as_view(next_page = 'login'), name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('pluscart/', views.plus_cart, name='pluscart'),
    path('minuscart/', views.minus_cart, name='minuscart'),
    path('removecart/', views.remove_cart, name='removecart'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),


    path('passwordchange/',as_view.PasswordChangeView.as_view(template_name = 'app/passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone/'), name='passwordchange'),
    
    path("passwordchangedone/", as_view.PasswordChangeDoneView.as_view(template_name = 'app/passwordchangedone.html'), name="passwordchangedone"),
    
    path("password-reset/", as_view.PasswordResetView.as_view(template_name = 'app/password_reset.html',form_class=MyPasswordResetForm), name="password_reset"),
    
    path("password-reset/done/", as_view.PasswordResetDoneView.as_view(template_name = 'app/password_reset_done.html'), name="password_reset_done"),
    
    path("password-reset-confirm/<uidb64>/<token>/", as_view.PasswordResetConfirmView.as_view(template_name = 'app/password_reset_confirm.html',form_class=MySetPasswordForm), name="password_reset_confirm"),
    
    path("password-reset-complete/", as_view.PasswordResetCompleteView.as_view(template_name = 'app/password_reset_complete.html'), name="password_reset_complete"),
    
    path('buy/', views.buy_now, name='buy-now'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
]+static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
