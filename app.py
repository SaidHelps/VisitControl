from datetime import date
from kivy.uix.checkbox import CheckBox
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.textinput import TextInput
import configparser
from kivy.core.window import Window
from kivy.lang.builder import Builder



class app(App):
    def __init__(self, **kwargs):
        self.vareble = None
        super().__init__(**kwargs)
        self.cof = configparser.ConfigParser()
        self.t2 = 't22-1b.ini'
        self.cof.read(self.t2)


        self.sm = ScreenManager()
        self.sc1 = Screen(name="main")
        self.sc2 = Screen(name="options")
        self.sc2_1 = Screen(name="options/add")
        self.sc2_2 = Screen(name="options/set")
        self.sc2_2_1 = Screen(name="options/set/user")
        self.sc2_3_1 = Screen(name="options/self")
        self.sc2_3_2 = Screen(name="options/self/remove")
        self.sc2_3_3 = Screen(name="options/self/create")
        self.sc2_3_4 = Screen(name="options/self/create/date")
        self.sc3 = Screen(name="status")
        self.sc3_1 = Screen(name="status/options")
        self.sm.add_widget(self.sc1)
        self.sm.add_widget(self.sc2)
        self.sm.add_widget(self.sc3)
        self.sm.add_widget(self.sc2_1)
        self.sm.add_widget(self.sc2_2)
        self.sm.add_widget(self.sc2_2_1)
        self.sm.add_widget(self.sc2_3_1)
        self.sm.add_widget(self.sc2_3_2)
        self.sm.add_widget(self.sc2_3_3)
        self.sm.add_widget(self.sc2_3_4)
        self.sm.add_widget(self.sc3_1)


    def build(self):
        #first window
        self.fl = FloatLayout()
        self.bl = BoxLayout()
        self.fl.add_widget(Image(color="white", size_hint=(1, 1)))
        self.bl.add_widget(Button(text="Опции", font_size=Window.size[0]/11,on_release=lambda x:self.changeWin('options')))
        self.bl.add_widget(Button(text="Список", font_size=Window.size[0]/11, on_release=lambda x:self.changeWin('status')))

        self.fl.add_widget(self.bl)

        self.sc1.add_widget(self.fl)
        #end first window

        #second window
        self.fl2 = FloatLayout()
        self.fl2.add_widget(Image(color="white", size_hint=(1, 1)))
        self.bl2 = BoxLayout(orientation="vertical")
        self.fl2.add_widget(self.bl2)
        self.bl2.add_widget(Button(text="Вернуться в главное меню --->",  font_size=Window.size[0]/15 ,on_release=lambda x: self.changeWin('main'), size_hint=(1, .3)))
        self.bl2.add_widget(Button(text="Добавить учеников", font_size=Window.size[0]/13, on_release=lambda x:self.changeWin('options/add')))
        self.bl2.add_widget(Button(text="Отметить Посещяемость", font_size=Window.size[0]/13,  on_release=lambda x:self.changeWin('options/set')))
        self.bl2.add_widget(Button(text="Ручное изменение", font_size=Window.size[0]/13,  on_release=lambda x:self.changeWin('options/self')))

        self.sc2.add_widget(self.fl2)
        #end second window

        #second window add
        self.fl2_1 = FloatLayout()
        self.fl2_1.add_widget(Image(color="white", size_hint=(1, 1)))
        self.input2_1 = TextInput(size_hint=(.7, .2), multiline=False, font_size=(Window.size[0]/10))
        self.fl2_1.add_widget(self.input2_1)
        self.errorlabel2_1 = Label(text="", pos_hint={'center_x':.5,'center_y':.5}, color="red", font_size=Window.size[0]/8, text_size=(Window.size[0]/1.2,Window.size[0]/2.5))
        self.fl2_1.add_widget(self.errorlabel2_1)
        self.fl2_1.add_widget(Button(text="Добавить в базу", text_size=(Window.size[0]/3.4,Window.size[0]/5),size_hint=(.3,.2), pos_hint={'x':.7,'y':0}, on_release=self.addToIni, color="violet",  font_size=Window.size[0]/16, bold=True))
        self.fl2_1.add_widget(Button(text="Вернуться в options --->", pos_hint={'x':0,'y':.9}, font_size=Window.size[0]/15, size_hint=(1, .1), on_release=lambda x: self.changeWin('options')))

        self.sc2_1.add_widget(self.fl2_1)
        #end of second window add

        #second window list
        self.fl2_2 = FloatLayout()
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter('height'))
        root = ScrollView(size=(Window.width, Window.height), size_hint=(1, .6))
        root.add_widget(self.layout)
        self.fl2_2.add_widget(Image(color="white", size_hint=(1, 1)))
        self.fl2_2.add_widget(Button(text="Вернуться в options --->", pos_hint={'x':0,'y':.9}, size_hint=(1, .1), font_size=Window.size[0]/15,on_release=lambda x: self.changeWin('options')))
        self.fl2_2.add_widget(root)

        self.sc2_2.add_widget(self.fl2_2)
        #end of second window list

        # 2 3 1
        self.fl2_3 = FloatLayout()
        self.fl2_3.add_widget(Image(color="white", size_hint=(1, 1)))
        self.bl2_3 = BoxLayout(orientation="vertical", size_hint=(1, .9), pos_hint={'x':0,'y':0})
        self.fl2_3.add_widget(Button(text="Вернуться в главное меню --->", pos_hint={'x':0,'y':.9}, size_hint=(1, .1), font_size=Window.size[0]/15,on_release=lambda x: self.changeWin('options')))
        self.bl2_3.add_widget(Button(text="Удалить ученика", font_size=Window.size[0]/13, on_release=lambda x: self.changeWin('options/self/remove')))
        self.bl2_3.add_widget(Button(text="Выставить дату в ручную", font_size=Window.size[0]/13, on_release=lambda x: self.changeWin('options/self/create')))

        self.fl2_3.add_widget(self.bl2_3)

        self.sc2_3_1.add_widget(self.fl2_3)
        # 2 3 1

        # 2 3 2
        self.fl2_3_2 = FloatLayout()
        self.fl2_3_2.add_widget(Image(color="white", size_hint=(1, 1)))
        self.layout2_3_2 = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout2_3_2.bind(minimum_height=self.layout2_3_2.setter('height'))
        root = ScrollView(size=(Window.width, Window.height), size_hint=(1, .8))
        root.add_widget(self.layout2_3_2)
        self.fl2_3_2.add_widget(Button(text="Вернуться в главное меню --->", font_size=Window.size[0]/15,pos_hint={'x':0,'y':.9}, size_hint=(1, .1), on_release=lambda x: self.changeWin('options/self')))
        self.sc2_3_2.add_widget(self.fl2_3_2)
        self.sc2_3_2.add_widget(root)
        # 2 3 2 close

        # 2 3 3
        self.fl2_3_3 = FloatLayout()

        self.fl2_3_3.add_widget(Image(color="white", size_hint=(1, 1)))
        self.fl2_3_3.add_widget(Button(text="Вернуться в меню ручной настройки --->", font_size=Window.size[0]/20,pos_hint={'x':0,'y':.9}, size_hint=(1, .1), on_release=lambda x: self.changeWin('options/self')))

        self.layout2_3_3 = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout2_3_3.bind(minimum_height=self.layout2_3_3.setter('height'))
        root = ScrollView(size_hint=(1, .7), size=(Window.width, Window.height))
        root.add_widget(self.layout2_3_3)

        self.fl2_3_3.add_widget(root)

        self.sc2_3_3.add_widget(self.fl2_3_3)
        # 2 3 3 close

        # 2 3 4
        self.fl2_3_4 = FloatLayout()
        self.fl2_3_4.add_widget(Image(color="white", size_hint=(1, 1)))
        self.fl2_3_4.add_widget(Button(text="Вернуться в меню ручной настройки --->", font_size=Window.size[0]/20,pos_hint={'x':0,'y':.9}, size_hint=(1, .1), on_release=lambda x: self.changeWin('options/self')))
        
        self.input2_3_4_year = TextInput(pos_hint={'x':0, 'center_y':.65}, size_hint=(.2, .07), font_size=Window.size[0]/15, multiline=False)
        self.input2_3_4_month = TextInput(pos_hint={'x':.4, 'center_y':.65}, size_hint=(.2, .07), font_size=Window.size[0]/15, multiline=False)
        self.input2_3_4_day = TextInput(pos_hint={'x':.8, 'center_y':.65}, size_hint=(.2, .07), font_size=Window.size[0]/15, multiline=False)

        self.checkBox2_2_3_2 = CheckBox(pos_hint={'center_x':.1,'center_y':.5}, color="black", size_hint=(.05, .05), on_release=self.checkBoxLogic11)
        self.checkBox2_2_3_3 = CheckBox(pos_hint={'center_x':.5,'center_y':.5}, color="black", size_hint=(.05, .05), on_release=self.checkBoxLogic21)
        self.checkBox2_2_3_4 = CheckBox(pos_hint={'center_x':.9,'center_y':.5}, color="black", size_hint=(.05, .05), on_release=self.checkBoxLogic31)
        
        self.fl2_3_4.add_widget(Label(text="Не было(-а) без причины",pos_hint={'center_x':.13,'center_y':.4}, color="black", font_size=Window.size[0]/25, text_size=(Window.size[0]/4, Window.size[1]/15)))
        self.fl2_3_4.add_widget(Label(text="Год",pos_hint={'center_x':.10,'center_y':.71}, color="black", font_size=Window.size[0]/21,))
        self.fl2_3_4.add_widget(Label(text="Месяц",pos_hint={'center_x':.5,'center_y':.71}, color="black", font_size=Window.size[0]/21,))
        self.fl2_3_4.add_widget(Label(text="День",pos_hint={'center_x':.9,'center_y':.71}, color="black", font_size=Window.size[0]/21,))
        self.fl2_3_4.add_widget(Label(text="Не было(-а) по уважительной", pos_hint={'center_x':.5,'center_y':.4}, color="black", font_size=Window.size[0]/25,  text_size=(Window.size[0]/3, Window.size[1]/15)))
        self.fl2_3_4.add_widget(Label(text="Был(-а)", pos_hint={'center_x':.93,'center_y':.43}, color="black", font_size=Window.size[0]/25, text_size=(Window.size[0]/4, Window.size[1]/15)))

        self.fl2_3_4.add_widget(self.checkBox2_2_3_2)
        self.fl2_3_4.add_widget(self.checkBox2_2_3_3)
        self.fl2_3_4.add_widget(self.checkBox2_2_3_4)
        self.errorlabel2_3_4 = Label(text="", pos_hint={"center_x":.5, "y":-.2}, font_size=Window.size[0]/20, text_size=(Window.size[0]/1.5, Window.size[1]/10))
        self.fl2_3_4.add_widget(self.errorlabel2_3_4)
        self.fl2_3_4.add_widget(Button(text="Добавить дату", font_size=Window.size[0]/22, size_hint=(.23, .1), pos_hint={'x':.4, 'y':.1}, text_size=(Window.size[0]/4.7,Window.size[1]/12), on_release=self.createDate))
        self.fl2_3_4.add_widget(self.input2_3_4_year)
        self.fl2_3_4.add_widget(self.input2_3_4_month)
        self.fl2_3_4.add_widget(self.input2_3_4_day)

        self.sc2_3_4.add_widget(self.fl2_3_4)
        # 2 3 4 close

        #third window
        self.fl3 = FloatLayout()
        self.fl3.add_widget(Image(color="white", size_hint=(1, 1)))

        self.layout3 = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout3.bind(minimum_height=self.layout3.setter('height'))
        root = ScrollView(size_hint=(1, .7), size=(Window.width, Window.height))
        root.add_widget(self.layout3)
        self.fl3.add_widget(Button(text="Вернуться в главное меню --->", pos_hint={'x':0,'y':.9}, size_hint=(1, .1), on_release=lambda x: self.changeWin('main'), font_size=Window.size[0]/15))
        self.fl3.add_widget(root)

        self.sc3.add_widget(self.fl3)
        #end of third window
        
        #3 1 window
        self.fl3_1 = FloatLayout()
        self.fl3_1.add_widget(Image(color="white", size_hint=(1, 1)))
        self.fl3_1.add_widget(Button(text="Вернуться в главное меню --->", pos_hint={'x':0,'y':.9}, size_hint=(1, .1), on_release=lambda x: self.changeWin('status'), font_size=Window.size[0]/15))

        self.layout3_1 = GridLayout(cols=1, spacing=10, size_hint_y=None)
        self.layout3_1.bind(minimum_height=self.layout3_1.setter('height'))
        root = ScrollView(size_hint=(1, .7), size=(Window.width, Window.height))
        root.add_widget(self.layout3_1)
        self.fl3_1.add_widget(root)

        self.sc3_1.add_widget(self.fl3_1)
        #end of 3 1 window

        return self.sm
    

    def createDate(self, q):
        if self.checkBox2_2_3_2.state == "normal" and self.checkBox2_2_3_3.state == "normal" and self.checkBox2_2_3_4.state == "normal":
            return 0
        else:
            try:
                qw = int(self.input2_3_4_day.text)
                qw += 1
                qw = int(self.input2_3_4_month.text)
                qw += 1
                qw = int(self.input2_3_4_year.text)
                qw += 1
            except:
                self.errorlabel2_3_4.color = "red"
                self.errorlabel2_3_4.text = "Дата, Месяц, Год принимают только целые числа"
                return 0
            # ???

    
    def optionAdd(self, q):
        self.sc2_2_1.clear_widgets()
        self.fl2_2_1 = FloatLayout()
        self.fl2_2_1.add_widget(Image(color="white", size_hint=(1, 1)))
        self.fl2_2_1.add_widget(Label(pos_hint={'center_x':.5,'center_y':.9}, text_size=(Window.size[0], Window.size[1]/4.6),text=f"Отметка посещяемости у [color=008000]{q.text}[/color] за [color=7a0031]{date.today()}[/color]", color="black", font_size=Window.size[0]/15, markup=True))
        self.checkBox2_2_1_2 = CheckBox(pos_hint={'center_x':.65,'center_y':.6}, color="black", size_hint=(.05, .05), on_release=self.checkBoxLogic1)
        self.checkBox2_2_1_3 = CheckBox(pos_hint={'center_x':.65,'center_y':.5}, color="black", size_hint=(.05, .05), on_release=self.checkBoxLogic2)
        self.checkBox2_2_1_4 = CheckBox(pos_hint={'center_x':.65,'center_y':.4}, color="black", size_hint=(.05, .05), on_release=self.checkBoxLogic3)
        
        self.fl2_2_1.add_widget(Label(text="Не было(-а) без причины",pos_hint={'center_x':.80,'center_y':.65}, color="black", font_size=Window.size[0]/22.5, text_size=(Window.size[0]/3, Window.size[1]/14)))
        self.fl2_2_1.add_widget(Label(text="Не было(-а) по уважительной", pos_hint={'center_x':.80,'center_y':.55}, color="black", font_size=Window.size[0]/22.5,  text_size=(Window.size[0]/3, Window.size[1]/14)))
        self.fl2_2_1.add_widget(Label(text="Был(-а)", pos_hint={'center_x':.80,'center_y':.45}, color="black", font_size=Window.size[0]/22.5, text_size=(Window.size[0]/3, Window.size[1]/14)))
        self.fl2_2_1.add_widget(Button(text="Вернуться к списку учеников --->", font_size=Window.size[0]/18,pos_hint={'x':0,'y':.9}, size_hint=(1, .1), on_release=lambda x: self.changeWin('options/set')))

        self.fl2_2_1.add_widget(Button(text="Выставить", font_size=Window.size[0]/15, size_hint=(.4, .2), pos_hint={'center_x':.2,'center_y':.5}, on_release=lambda x:self.addOption(section=q.text)))
        self.fl2_2_1.add_widget(self.checkBox2_2_1_2)
        self.fl2_2_1.add_widget(self.checkBox2_2_1_3)
        self.fl2_2_1.add_widget(self.checkBox2_2_1_4)

        self.sc2_2_1.add_widget(self.fl2_2_1)

        self.sm.current="options/set/user"


    def checkBoxLogic1(self, q):
        self.checkBox2_2_1_3.state = "normal"
        self.checkBox2_2_1_4.state = "normal"


    def checkBoxLogic2(self, q):
        self.checkBox2_2_1_2.state = "normal"
        self.checkBox2_2_1_4.state = "normal"


    def checkBoxLogic3(self, q):
        self.checkBox2_2_1_2.state = "normal"
        self.checkBox2_2_1_3.state = "normal"

    
    def checkBoxLogic11(self, q):
        self.checkBox2_2_3_3.state = "normal"
        self.checkBox2_2_3_4.state = "normal"


    def checkBoxLogic21(self, q):
        self.checkBox2_2_3_2.state = "normal"
        self.checkBox2_2_3_4.state = "normal"


    def checkBoxLogic31(self, q):
        self.checkBox2_2_3_2.state = "normal"
        self.checkBox2_2_3_3.state = "normal"


    def addOption(self, section):
        if self.checkBox2_2_1_2.state == "normal" and self.checkBox2_2_1_3.state == "normal" and self.checkBox2_2_1_4.state == "normal":
            return 0
        else:
            a = None
            if self.checkBox2_2_1_2.state == "down":
                a = "1"
            elif self.checkBox2_2_1_3.state == "down":
                a = "2"
            elif self.checkBox2_2_1_4.state == "down":
                a = "3"
            self.cof.read(self.t2)
            self.cof.set(str(section), str(date.today()), str(a))
            with open(self.t2, 'w') as configfile:
                self.cof.write(configfile)
            self.changeWin(win="options/set")


    def optionGet(self, q):
        self.layout3_1.clear_widgets()
        self.cof.read(self.t2)
        qa = self.cof[q.text]
        for i in qa:
            if self.cof[q.text][i] == "1":
                w = Button(text=str(i),size_hint_y=None, height=40, background_color="red")
                self.layout3_1.add_widget(w)
            elif self.cof[q.text][i] == "2":
                w = Button(text=str(i),size_hint_y=None, height=40, background_color="yellow")
                self.layout3_1.add_widget(w)
            elif self.cof[q.text][i] == "3":
                w = Button(text=str(i),size_hint_y=None, height=40, background_color="green")
                self.layout3_1.add_widget(w)
        self.changeWin("status/options")


    def changeWin(self, win):
        if win == "options/set":
            self.layout.clear_widgets()
            self.cof.read(self.t2)
            qw = self.cof.sections()
            for i in qw:
                btn = Button(text=str(i), size_hint_y=None, height=Window.size[1]/17, on_release=self.optionAdd)
                self.layout.add_widget(btn)
        elif win == "status":
            self.layout3.clear_widgets()
            self.cof.read(self.t2)
            q = self.cof.sections()
            for i in q:
                w = Button(text=str(i),size_hint_y=None, height=40, on_release=self.optionGet)
                self.layout3.add_widget(w)
        elif win == "options/self/remove":
            self.layout2_3_2.clear_widgets()
            self.cof.read(self.t2)
            q = self.cof.sections()
            for i in q:
                btn = Button(text=str(i), size_hint_y=None, height=Window.size[1]/17, on_release=self.callPopup232)
                self.layout2_3_2.add_widget(btn)
        elif win == "options/self/create":
            self.layout2_3_2.clear_widgets()
            self.cof.read(self.t2)
            q = self.cof.sections()
            for i in q:
                btn = Button(text=str(i), size_hint_y=None, height=Window.size[1]/17, on_release=self.buffer)
                self.layout2_3_3.add_widget(btn)
        self.sm.current = win
    
    
    def buffer(self, q):
        self.vareble = q.text
        self.changeWin("options/self/create/date")
    


    def callPopup232(self, q):
        self.popup2_3_2 = Popup(title=f'Удалить ученика {q.text} из базы?',
    size_hint=(.85, .6))
        flw = FloatLayout()
        flw.add_widget(Button(text="Да", pos_hint={'center_x':.3,'center_y':.5}, size_hint=(.3, .3), font_size=Window.size[0]/15, on_release=lambda x:self.removePreson(person=q.text, yn=True)))
        flw.add_widget(Button(text="Нет", pos_hint={'center_x':.7,'center_y':.5}, size_hint=(.3, .3), font_size=Window.size[0]/15, on_release=lambda x:self.removePreson(person=q.text, yn=False)))
        self.popup2_3_2.add_widget(flw)
        self.popup2_3_2.open()


    def removePreson(self, yn, person):
        if yn:
            self.popup2_3_2.dismiss()
            self.cof.read(self.t2)
            self.cof.remove_section(person)
            with open(self.t2, 'w') as configfile:
                self.cof.write(configfile)
            self.changeWin("options/self/remove")
        else:
            self.popup2_3_2.dismiss()


    def addToIni(self, q):
        try:
            if len(self.input2_1.text) >= 4:
                self.cof.read(self.t2)
                self.cof.add_section(self.input2_1.text)
                with open(self.t2, 'w') as configfile:
                    self.cof.write(configfile)
                self.errorlabel2_1.text = "Успешно добавленно!"
                self.errorlabel2_1.color="green"
                self.input2_1.text = ""
            else:
                self.errorlabel2_1.text="Минимальная длина 4 символа!"
                self.errorlabel2_1.color="red"
        except:
            self.errorlabel2_1.text = "Не удалось доабвить в базу!"
            self.errorlabel2_1.color="red"
app().run()