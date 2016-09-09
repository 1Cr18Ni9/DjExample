from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.core.urlresolvers import reverse_lazy

app_name = 'account'

urlpatterns = [
    # url(r'^login/$', views.user_login, name='login'),

    # /account/
    url(r'^$', views.dashboard, name='dashboard'),

    # /account/login/
    url(r'^login/$', auth_views.login, name='login'),

    # /account/logout/
    url(r'^logout/$',
        auth_views.logout, name='logout'),

    # /account/logout-then-login/
    url(r'^logout-then-login/$',
        auth_views.logout_then_login, name='logout_then_login'),

    # /account/password-change/
    url(r'^password-change/$', auth_views.password_change,
        {'post_change_redirect': reverse_lazy('account:password_change_done'), }, name='password_change'),

    # /account/password-change/done/
    url(r'^password-change/done/$',
        auth_views.password_change_done, name='password_change_done'),

    # /account/password-reset/
    url(r'^password-reset/$', auth_views.password_reset,
        {'post_reset_redirect': reverse_lazy('account:password_reset_done')}, name='password_reset'),

    # /account/password-reset/done/
    url(r'^password-reset/done/$', auth_views.password_reset_done,
        name='password_reset_done'),

    # /account/password-reset/confirm/xx/xxxxxxxxxxxxxx/
    url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',
        auth_views.password_reset_confirm,
        {'post_reset_redirect': reverse_lazy(
            'account:password_reset_complete')},
        name='password_reset_confirm'),

    # /account/password-reset/complete/
    url(r'^password-reset/complete/$', auth_views.password_reset_complete,
        name='password_reset_complete'),

    # /account/register/  Creating an account
    url(r'^register/$', views.register, name='register'),

    # /account/edit/
    url(r'^edit/$', views.edit, name='edit'),
]
