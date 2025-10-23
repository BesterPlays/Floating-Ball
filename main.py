from kivy.app import App
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random

class FloatingBallApp(App):
    def build(self):
        # Make window transparent and floating
        Window.clearcolor = (0, 0, 0, 0)
        Window.borderless = True
        Window.always_on_top = True
        
        # Create the floating ball
        self.ball = Button(
            size_hint=(None, None),
            size=(80, 80),
            background_color=(1, 0, 0, 0.8),
            background_normal='',
            pos=(300, 600)
        )
        self.ball.border = [0, 0, 0, 0]
        
        # Make it draggable
        self.ball.bind(on_touch_move=self.drag_ball)
        self.ball.bind(on_press=self.ball_clicked)
        
        return self.ball
    
    def drag_ball(self, instance, touch):
        if instance.collide_point(touch.x, touch.y):
            instance.center = (touch.x, touch.y)
            return True
    
    def ball_clicked(self, instance):
        # Change color on click
        colors = [
            (1, 0, 0, 0.8),    # Red
            (0, 1, 0, 0.8),    # Green
            (0, 0, 1, 0.8),    # Blue
            (1, 1, 0, 0.8),    # Yellow
            (1, 0, 1, 0.8)     # Purple
        ]
        instance.background_color = random.choice(colors)
        
        # Show permission reminder
        self.show_permission_popup()
    
    def show_permission_popup(self):
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(
            text='For floating over apps:\nGo to Settings → Accessibility\nand enable this app!',
            text_size=(300, None)
        ))
        
        popup = Popup(
            title='Accessibility Permission Needed',
            content=content,
            size_hint=(0.8, 0.4)
        )
        
        close_btn = Button(text='OK', size_hint_y=0.3)
        close_btn.bind(on_press=popup.dismiss)
        content.add_widget(close_btn)
        
        popup.open()

if __name__ == '__main__':
    FloatingBallApp().run()