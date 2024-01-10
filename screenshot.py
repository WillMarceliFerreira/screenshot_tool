import PySimpleGUI as sg
import pyautogui
import time
import threading
import keyboard  # Importando a biblioteca keyboard

# Função modificada para captura de tela
def capture_screen(image_count):
    screenshot = pyautogui.screenshot()
    screenshot.save(f'screenshot_{image_count}.png')

# Função para monitorar as teclas do teclado
def keyboard_monitor(window, image_count, lock):
    while True:
        try:
            # Se Ctrl+H for pressionado, capture a tela
            if keyboard.is_pressed('f9'):
                with lock:
                    image_count[0] += 1
                    current_count = image_count[0]
                window.write_event_value('-CAPTURE-', current_count)
                time.sleep(0.5)  # Pequena pausa para evitar múltiplas capturas
        except:
            break  # Termina a thread se ocorrer algum erro

# Layout da interface gráfica
layout = [
    [sg.Text('Press F9 to capture the screen or use the button.')],
    [sg.Button("Capture Screen"), sg.Button("Exit")],
    [sg.Text("", key="-STATUS-")]
]

# Criar janela
sg.theme('Reddit')
window = sg.Window("Screen Capture", layout)

# Inicializar contador de imagens e lock
image_count = [0]
lock = threading.Lock()

# Inicializar e iniciar a thread de monitoramento do teclado
thread = threading.Thread(target=keyboard_monitor, args=(window, image_count, lock), daemon=True)
thread.start()

# Loop de eventos
while True:
    event, values = window.read()

    # Se o usuário fechar a janela ou clicar em "Sair"
    if event == sg.WIN_CLOSED or event == "Sair":
        break

    # Se o usuário clicar em "Capturar Tela" ou se a tecla Ctrl+H for pressionada
    if event == "Capturar Tela" or event == "-CAPTURE-":
        with lock:
            current_count = image_count[0]
        capture_screen(current_count)
        window["-STATUS-"].update(f"Screenshot {current_count} saved.")
        time.sleep(0.5)  # Pequena pausa para evitar múltiplas capturas

# Fechar janela e terminar a thread
keyboard.unhook_all()
window.close()