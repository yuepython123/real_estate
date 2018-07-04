from django.conf.urls import url
import views
urlpatterns=[
    url(r'^$',views.customer_condition),
    url(r'^left.html$', views.left_view),
    url(r'^top.html$', views.top_view),
    url(r'^customer_state_list.html/(\d*)$',views.condition_all_view),
    url(r'^customer_state_add.html$',views.condition_add_view),
    url(r'^customer_type_list.html/(\d*)$',views.type_all_view),
    url(r'^customer_type_add.html$',views.type_add_view),
    url(r'^customer_source_list.html/(\d*)$',views.source_list_view),
    url(r'^customer_source_add.html$',views.source_add_view),
]