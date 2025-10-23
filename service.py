from jnius import autoclass, cast

# Android classes
Context = autoclass('android.content.Context')
WindowManager = autoclass('android.view.WindowManager')
LayoutParams = autoclass('android.view.WindowManager$LayoutParams')
View = autoclass('android.view.View')
Button = autoclass('android.widget.Button')

class FloatingService:
    def create_floating_window(self):
        PythonService = autoclass('org.kivy.android.PythonService')
        service = PythonService.mService
        
        # Create layout params for floating window
        params = LayoutParams()
        params.type = LayoutParams.TYPE_APPLICATION_OVERLAY
        params.flags = (LayoutParams.FLAG_NOT_FOCUSABLE |
                       LayoutParams.FLAG_NOT_TOUCH_MODAL)
        params.width = 200
        params.height = 200
        params.x = 0
        params.y = 100
        
        # Create button
        button = Button(service)
        button.setText("Floating Ball")
        button.setBackgroundColor(0xFFFF0000)  # Red
        
        # Add to window manager
        wm = service.getSystemService(Context.WINDOW_SERVICE)
        wm.addView(button, params)