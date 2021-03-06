from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home),
    path('',views.intro),
    path('about/', views.about),
    path('contact/',views.contact),
    path('video/',views.video),
    path('second/',views.second),
    path('even/',views.output1),
    path('fourth/',views.fourth),
    path('p2/',views.two),
    path('p2out/',views.output2),
    path('p3/',views.third),
    path('p3out/',views.output3),
    path('fourth/',views.fourth),
    path('p4out/',views.output1),
    path('p5/',views.fifth),
    path('p5out/',views.fifth),
    path('p6/',views.sixth),
    path('p7/',views.seventh),
    path('p8/',views.eighth),
    path('p9/',views.ninth),
    path('p10/',views.tenth),
    path('quiz/',views.quiz),
    path('grade/',views.grade),
]