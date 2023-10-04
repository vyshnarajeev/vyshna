from django .urls import path
from .import views
app_name='ecoapp'
urlpatterns=[
    path('',views.allProCat,name="allProCat"),
    path('<slug:c_slug>/',views.allProCat,name="products_by_category"),
    path('<slug:c_slug>/<slug:product_slug>/',views.proDetail,name="ProdutCategoryDetail"),
]
