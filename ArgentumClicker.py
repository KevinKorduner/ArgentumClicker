import ctypes
import sys
import keyboard
import pyautogui
import time
import subprocess

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def perform_double_clicks():
    try:
        for i in range(2):
            pyautogui.doubleClick()
            print(f"Doble clic {i+1} realizado.")
            time.sleep(0.01)  # Pausa mínima entre los doble clics
    except Exception as e:
        print(f"Error al realizar doble clics: {e}")

def on_key_event(e):
    if e.name == 'u':
        print("Tecla 'U' presionada, realizando doble clics...")
        perform_double_clicks()

def main():
    try:
        keyboard.on_press(on_key_event)
        print("Script en ejecución. Presiona 'esc' para salir.")
        keyboard.wait('esc')
    except KeyboardInterrupt:
        print("Script terminado manualmente.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    if is_admin():
        main()
    else:
        # Reintenta ejecutar el script como administrador
        print("Solicitando privilegios de administrador...")
        ctypes.windll.shell32.ShellExecuteW(
            None, "runas", sys.executable, __file__, None, 1
        )
        sys.exit()
