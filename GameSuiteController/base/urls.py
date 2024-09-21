from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path("", views.dashboard , name='dashboard'),
    path("/tic_tac_toe", views.run_tic_tac_toe , name='tic_tac_toe'),
    path("/sudoku", views.run_sudoku , name='sudoku'),
    path("/checkers", views.run_checkers , name='checkers'),
]

