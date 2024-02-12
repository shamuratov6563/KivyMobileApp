from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import Screen
from kivymd.uix.button import MDRectangleFlatButton
from kivy.lang import Builder
from helpers import *


class MainApp(MDApp):
    screen = Screen()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.dialog = None
        self.header = None
        self.c1 = None
        self.c2 = None
        self.c3 = None
        self.c4 = None
        self.t1 = None
        self.t2 = None
        self.one_three = None
        self.one_four = None
        self.two_four = None
        self.m_yuk = None

    def build(self):
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.primary_hue = "A700"
        self.theme_cls.theme_style = "Light"
        # border black
        md_flat_button = MDRectangleFlatButton(text='Aniqlash',
                                               pos_hint={'center_x': 0.5, 'center_y': 0.1},
                                               on_release=self.find_most_convenient_way,
                                               _min_width=500)
        self.c1 = Builder.load_string(c1)
        self.c2 = Builder.load_string(c2)
        self.c3 = Builder.load_string(c3)
        self.c4 = Builder.load_string(c4)
        self.t1 = Builder.load_string(t1)
        self.t2 = Builder.load_string(t2)
        self.m_yuk = Builder.load_string(m_yuk)

        self.one_three = Builder.load_string(one_three)
        self.one_four = Builder.load_string(one_four)
        self.two_four = Builder.load_string(two_four)

        self.header = Builder.load_string(screen_helper)
        self.screen.add_widget(self.header)
        self.screen.add_widget(self.c1)
        self.screen.add_widget(self.c2)
        self.screen.add_widget(self.c3)
        self.screen.add_widget(self.c4)
        self.screen.add_widget(self.t1)
        self.screen.add_widget(self.t2)
        self.screen.add_widget(self.m_yuk)

        self.screen.add_widget(self.one_three)
        self.screen.add_widget(self.one_four)
        self.screen.add_widget(self.two_four)

        self.screen.add_widget(md_flat_button)

        return self.screen

    def find_most_convenient_way(self, obj):
        close_button = MDRectangleFlatButton(text="Yo'pish", on_release=self.close_dialog)

        # 1 - yechim
        results = {}
        most_convinients = []
        error = False
        try:
            ways_list = [
                [3, 2, 1, 0, "2,3,4 | 3,4"],
                [2, 2, 1, float(self.one_three.text) * float(self.t1.text), "2+3,4 | 3,4"],
                [2, 2, 1, float(self.one_four.text) * float(self.t2.text), '2,3+4 | 3,4'],
                [2, 2, 1, float(self.one_four.text) * float(self.t1.text), '2+4,3 | 3,4'],
                [1, 2, 1, (float(self.one_four.text) + float(self.one_three.text)) * float(self.t1.text), '2+3+4 | 3,4'],
                [3, 1, 1, float(self.two_four.text) * float(self.t2.text), '2,3,4 | 3+4'],
                [2, 1, 1, float(self.one_three.text) * float(self.t1.text) + float(self.two_four.text) * float(self.t2.text), '2+3,4 | 3+4'],
                [2, 1, 1, (float(self.one_four.text) + float(self.two_four.text)) * float(self.t2.text), '2,3+4 | 3+4'],
                [2, 1, 1, float(self.one_four.text) * float(self.t1.text) + (float(self.one_four.text) + float(self.two_four.text)) * float(self.t2.text), '2+4,3 | 3+4'],
                [1, 1, 1, (float(self.one_three.text) + float(self.one_four.text)) * float(self.t1.text) + (float(self.one_four.text) + float(self.two_four.text)) * float(self.t2.text), '2+3+4 | 3+4']
            ]
            for way in ways_list:
                result = 0
                for i in range(3):
                    c_i = float(getattr(self, f'c{i+1}').text)
                    result += c_i * float(self.m_yuk.text) * way[i] 
                result += way[3]

                if round(result, 2) in results:
                    results[round(result, 2)].append({
                        'way': len(results)+1,
                        'convenient_scheme': way[4],
                        'result': round(result, 2),
                    })
                else:
                    results[round(result, 2)] = [{
                        'way': len(results)+1,
                        'convenient_scheme': way[4],
                        'result': round(result, 2),
                    }]

            min_value = min(results.keys())
        except Exception as e:
            print(e)
            error = True


        print(most_convinients)
        print(results)



        
        if not error:

            text = ""
            for i in results[min_value]:
                text += f"""Eng qulay variant: {i['way']} \nEng qulay variant sxemasi: {i['convenient_scheme']} \nEng qulay variant vagon-soatlari: {i['result']} \n------------------------------------------------\n
                """

            

            self.dialog = MDDialog(title="Dastur Natijasi", 
                                   text=f"Eng qulay yo'l soni: {text}", 
                                   buttons=[close_button,]
            )
            self.dialog.open()
        else:
            self.dialog = MDDialog(title="Kiritilgan ma'lumotlardagi xatolik", 
                                   text=f"Kiritilgan ma'lumotlar faqat son va kasrli sonlar nuqtalar bilan ajratilganligiga e'tibor bering", 
                                   buttons=[close_button]
            )
            self.dialog.open()

    def close_dialog(self, obj):
        self.dialog.dismiss()


MainApp().run()
