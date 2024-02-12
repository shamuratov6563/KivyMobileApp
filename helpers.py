c1 = """
MDTextField:
    hint_text: "c1"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.3, 'center_y': 0.8}
    size_hint_x: None
    width: 200
"""

c2 = """
MDTextField:
    hint_text: "c2"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.7, 'center_y': 0.8}
    size_hint_x: None
    width: 200
"""

c3 = """
MDTextField:
    hint_text: "c3"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.3, 'center_y': 0.65}
    size_hint_x: None
    width: 200
"""

c4 = """
MDTextField:
    hint_text: "c4"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.7, 'center_y': 0.65}
    size_hint_x: None
    width: 200
"""



t1 = """
MDTextField:
    hint_text: "tej 2 yo'l"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.3, 'center_y': 0.5}
    size_hint_x: None
    width: 200
"""

t2 = """
MDTextField:
    hint_text: "tej 3 yo'l"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.7, 'center_y': 0.5}
    size_hint_x: None
    width: 200
"""


one_three = """
MDTextField:
    hint_text: "1 ---> 3"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.3, 'center_y': 0.35}
    size_hint_x: None
    width: 200
"""


one_four = """
MDTextField:
    hint_text: "1 ---> 4"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.7, 'center_y': 0.35}
    size_hint_x: None
    width: 200
"""

two_four = """
MDTextField:
    hint_text: "2 ---> 4"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.3, 'center_y': 0.2}
    size_hint_x: None
    width: 200
"""

m_yuk = """
MDTextField:
    hint_text: "m yuk"
    helper_text: "kiritish majburiy"
    helper_text_mode: "on_focus"
    icon_right_color: app.theme_cls.primary_color
    pos_hint: {'center_x': 0.7, 'center_y': 0.2}
    size_hint_x: None
    width: 200
"""




screen_helper = """
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDTopAppBar: 
            title: 'Eng qulay sxema'
            # IMAGE IN THE LEFT SIDE
            left_action_items: [["train", lambda x: app.navigation_draw()]]
        MDLabel:
            text: '' 
            halign: 'center'
"""
