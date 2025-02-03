import os
import socket
import subprocess
from time import sleep
from colorama import Fore, Style, init


init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_ip():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "No disponible"

def print_ascii_art():
    print(Fore.CYAN + """ 

 ░▒▓██████▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░    ░▒▓██▓▒░  
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░  ░▒▓██▓▒░    
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓██▓▒░      
░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░        
 ░▒▓██████▓▒░ ░▒▓██████▓▒░░▒▓█▓▒░▒▓████████▓▒░ 
   ░▒▓█▓▒░                                     
    ░▒▓██▓▒░                                   

    """ + Style.RESET_ALL)

def show_menu():
    clear_screen()
    print_ascii_art()
    print(Fore.YELLOW + "=== MENÚ PRINCIPAL ===" + Style.RESET_ALL)
    print(Fore.GREEN + "[1] Ejecutar Servidor Flask")
    print(Fore.RED + "[2] Salir")
    return input(Fore.BLUE + "Selecciona una opción: " + Style.RESET_ALL)

def run_app():
    clear_screen()
    print_ascii_art()
    print(Fore.YELLOW + "=== EJECUTANDO SERVIDOR ===" + Style.RESET_ALL)
    print(Fore.GREEN + f"IP del servidor: {get_ip()}")
    print(Fore.GREEN + "Puerto: 5000")
    print(Fore.GREEN + "Accede en: http://127.0.0.1:5000/")
    print(Fore.YELLOW + "Presiona CTRL+C para detener el servidor")
    sleep(2)
    
    try:
        process = subprocess.Popen(["python", "app.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        process.wait()
    except KeyboardInterrupt:
        print(Fore.RED + "\nServidor detenido manualmente." + Style.RESET_ALL)
        process.terminate()
        process.wait()


if __name__ == "__main__":
    while True:
        choice = show_menu()
        if choice == "1":
            run_app()
        elif choice == "2":
            print(Fore.RED + "Saliendo...")
            break
        else:
            print(Fore.RED + "Opción no válida, intenta de nuevo.")
            sleep(2)
