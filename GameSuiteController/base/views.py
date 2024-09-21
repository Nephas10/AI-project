from django.shortcuts import render
from django.http import HttpResponse
import subprocess

# virutal environment

python_interpreter = r'..\env\Scripts\python.exe'

def dashboard(request):
    name = 'Game Suite'
    context = {
        'name': name
    }
    return render(request, 'base/dashboard.html', context)



def run_tic_tac_toe(request):
    # Path to your virtual environment's Python interpreter
    
    # Path to the game script
    script_path = r'..\Game Suite\TicTacToe-AI\main.py'

    try:
        subprocess.run([python_interpreter, script_path], check=True)  # Use 'python' on Windows
        return HttpResponse("Thank you for playing")
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Script failed with error: {str(e)}")
    
    
def run_sudoku(request):
    
    script_path = r'..\Game Suite\pygame-sudoku\sudoku.py'

    try:
        subprocess.run([python_interpreter, script_path], check=True)  # Use 'python' on Windows
        return HttpResponse("Thank you for playing")
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Script failed with error: {str(e)}")
    
    
def run_checkers(request):
    interpreter = r'..\env\Scripts\python.exe'
    script_path = r'..\Game Suite\python-checkers\checkers.py'
    argument = 'cpu'

    try:
        # Capture both stdout and stderr
        result = subprocess.run([interpreter, script_path, argument], 
                                capture_output=True, text=True, check=True)
        # Return stdout to see what happened
        return HttpResponse(f"Script Output: {result.stdout}")
    except subprocess.CalledProcessError as e:
        return HttpResponse(f"Script failed with error: {str(e)}")