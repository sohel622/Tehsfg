from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = False
        self.last_button = None

        # প্রধান লেআউট (ভার্টিকাল)
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=10)

        # রেজাল্ট ডিসপ্লে স্ক্রিন
        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=50,
            background_color=(0.15, 0.15, 0.15, 1),
            foreground_color=(1, 1, 1, 1),
            size_hint=(1, 0.25)
        )
        main_layout.add_widget(self.solution)

        # বোতামের গ্রিড (৪টি কলাম)
        buttons = [
            ["C", "(", ")", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "DEL", "="]
        ]

        grid = GridLayout(cols=4, spacing=8, size_hint=(1, 0.75))

        for row in buttons:
            for label in row:
                btn = Button(
                    text=label,
                    font_size=28,
                    background_normal="",
                    background_color=self.get_btn_color(label)
                )
                btn.bind(on_press=self.on_button_press)
                grid.add_widget(btn)

        main_layout.add_widget(grid)
        return main_layout

    def get_btn_color(self, label):
        # বোতামের সুন্দর থিম কালার
        if label in ["/", "*", "-", "+", "="]:
            return (0.98, 0.55, 0.0, 1)  # কমলা রঙ
        elif label in ["C", "DEL", "(", ")"]:
            return (0.35, 0.35, 0.35, 1)  # ছাই রঙ
        else:
            return (0.2, 0.2, 0.2, 1)      # গাঢ় ছাই রঙ

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        elif button_text == "DEL":
            self.solution.text = current[:-1]
        elif button_text == "=":
            if current:
                try:
                    # হিসাব সম্পন্ন করা
                    self.solution.text = str(eval(current))
                except Exception:
                    self.solution.text = "Error"
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                self.solution.text += button_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

if __name__ == "__main__":
    CalculatorApp().run()
      
