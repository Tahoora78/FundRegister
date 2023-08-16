from django.urls import path
# from rest_framework_swagger import get_swagger_view


from . import views

# schema_view = get_swagger_view(title=)


urlpatterns = [
    path('', views.test, name='index'),
    path('save_data', views.save_fund_info, name='save_fund_info'),
    path('fund_by_regno/<reg_no>', views.show_fund_info_by_regno, name='get_fund_info'),
    path('fund_by_name/<name>', views.show_fund_info_by_name)
]