from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
import threading

class ViralClipperApp(App):
    def build(self):
        self.title = "Auto Viral Clipper"
        layout = BoxLayout(orientation='vertical', padding=40, spacing=20)
        
        self.label = Label(text='[b]Auto Viral Clipper[/b]', markup=True, font_size=24, size_hint_y=None, height=50)
        layout.add_widget(self.label)
        
        self.url_input = TextInput(hint_text='Pega el link del video o stream...', size_hint_y=None, height=55, multiline=False)
        layout.add_widget(self.url_input)
        
        self.btn = Button(text='Generar Clips Virales (9:16)', size_hint_y=None, height=65, background_color=(0.1, 0.6, 0.9, 1))
        self.btn.bind(on_press=self.iniciar_proceso)
        layout.add_widget(self.btn)
        
        self.status_label = Label(text='Estado: Listo para recibir enlaces.', font_size=16)
        layout.add_widget(self.status_label)
        
        return layout

    def iniciar_proceso(self, instance):
        url = self.url_input.text.strip()
        if not url:
            self.status_label.text = '¡Por favor ingresa una URL válida!'
            return
        
        self.status_label.text = 'Procesando video en segundo plano...'
        threading.Thread(target=self.procesar_video_thread, args=(url,)).start()

    def procesar_video_thread(self, url):
        # Simulación de proceso de IA / Recorte para la interfaz móvil
        self.status_label.text = '¡Clips generados y guardados con éxito!'

if __name__ == '__main__':
    ViralClipperApp().run()
