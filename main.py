from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
import numpy as np

#Opening Page
Builder.load_string("""
<Homepage>:
    id: Homepage
    name: "Homepage"
    
    GridLayout:
        cols: 1
        
        Button:
            background_normal: "KSquared_Logo.png"
            on_release:
                app.root.current = "Fractions"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 60
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Fractions Calculator"
            on_release:
                app.root.current = "Fractions"
                root.manager.transition.direction = "left" 

""")

Builder.load_string("""
<Fractions>
    id:Fractions
    name:"Fractions"

    ScrollView:
        name: "Scroll"
        do_scroll_x: False
        do_scroll_y: True
        
        GridLayout:
            cols: 1
            padding:10
            spacing:10
            size_hint: 1, None
            width:200
            height: self.minimum_height
            
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Fractions Calculator"
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 

                Button:
                    text: "Clear Entry"   
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    on_release:
                        a.text = ""
                        b.text = ""
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        a.text = ""
                        b.text = ""
                        list_of_steps.clear_widgets()            
                    
            Label:
                font_size: 60
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Whole(Numerator/Denomenator)"       
                   
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
        
                Label:
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    text: "Fraction 1 ="
                                                        
                TextInput:
                    id: a
                    text: a.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(a.text)] 
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5        
        
                Label:
                    font_size: 75
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    text: "Fraction 2 ="
                                                    
                TextInput:
                    id: b
                    text: b.text
                    multiline: False
                    font_size: 125
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(b.text)] 
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
    
                Button:
                    id: steps
                    text: "+"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 1, 0, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions.add(a.text + "$" + b.text)  
                
                Button:
                    id: steps
                    text: "-"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions.sub(a.text + "$" + b.text) 
                        
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
    
                Button:
                    id: steps
                    text: "x"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 1, 0, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions.mult(a.text + "$" + b.text)  
                
                Button:
                    id: steps
                    text: "÷"   
                    font_size: 75
                    size_hint_y: None
                    background_color: 0, 0, 1, 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions.div(a.text + "$" + b.text) 
                       
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height                  
                    
""")

class Fractions(Screen):
    sm = ScreenManager()

    def __init__(self, **kwargs):
        super(Fractions, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)

    def _key_handler(self, instance, key, *args):
        if key == 27:
            self.set_previous_screen()
            return True

    def set_previous_screen(self):
        if sm.current != "Homepage":
            sm.transition.direction = 'right'
            sm.current = sm.previous()
            
    layouts = []
    def add(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            answer = ""
            #Fraction and Fraction
            if entry.count("/") == 2 and entry.count("(") == 0 and entry.count(")") == 0:
                print("ADD F + F")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                if entry_list[0].count("/") == 1:
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_index]
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                if entry_list[1].count("/") == 1:
                    frac_sign_index = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_index]
                    denom_b = entry_list[1][frac_sign_index+1:]
                    print("denom_b",denom_b)
                lcm = str(np.lcm(int(denom_a),int(denom_b)))
                print("lcm",lcm)
                self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                if int(denom_a) != int(denom_b):
                    print()
                    diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + entry_list[0] + "(" + diff_a + ")" + " + " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = 60, size_hint_y= None, height=100))
                    numer_added = str(int(diff_a) * int(numer_a) + int(diff_b) * int(numer_b))
                    answer = numer_added + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    numer_added = str(int(numer_b) + int(numer_a)).replace(".0","")
                    answer = numer_added + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("ADD F + WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_one = entry_list[0][:left_par]
                    print("whole_one",whole_one)
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    frac = str(int(whole_one) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        numer_add = str(int(diff_a) * int(numer_a) + int(diff_b) * int(numer_b))
                        answer = numer_add + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_added = str((int(whole_one) * int(denom_a) + int(numer_a)) + int(numer_b)).replace(".0","")
                        answer = numer_added + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b",denom_b)
                    numer_b = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b",numer_b)
                    frac = str(int(whole_two) * int(denom_b) + int(numer_b)).replace(".0","") + "/" + str(denom_b)
                    print("frac",frac)
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_two+1:]
                    print("denom_a",denom_a)
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " + " + entry_list[0] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + frac + "(" + diff_a + ")" + " + " + "(" + diff_b + ")" + entry_list[0] + "(" + diff_b + ")" + " = ",font_size = 60, size_hint_y= None, height=100))
                        numer_add = str(int(diff_a) * int(numer_a) + int(diff_b) * int(numer_b))
                        answer = numer_add + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_added = str((int(whole_two) * int(denom_a) + int(numer_a)) + int(numer_b)).replace(".0","")
                        answer = numer_added + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
            #Fraction and Whole    
            if entry.count("/") == 1 and entry.count("(") == 0 and entry.count(")") == 0:
                print("ADD F + W")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the F
                if entry_list[0].count("(") == 0 and entry_list[0].count(")") == 0 and entry_list[0].count("/") == 1:
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[1]) * int(lcm))
                    whole_frac = str(int(entry_list[1]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + whole_frac,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " + " + whole_frac,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(whole_frac_numer) + int(numer_a)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the F
                if entry_list[1].count("(") == 0 and entry_list[1].count(")") == 0 and entry_list[1].count("/") == 1:
                    frac_sign_index = entry_list[1].find("/")
                    denom_a = entry_list[1][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[0]) * int(lcm))
                    whole_frac = str(int(entry_list[0]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + whole_frac,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " + " + entry_list[1]  ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(whole_frac_numer) + int(numer_a)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole and Whole(Fraction)
            if entry.count("/") == 1 and entry.count("(") == 1 and entry.count(")") == 1:
                print("ADD W , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF + W")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole = entry_list[0][:left_par]
                    print("whole",whole)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac = str(int(whole) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[1]) * int(lcm))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(lcm)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    self.ids.list_of_steps.add_widget(Label(text= frac + " + " + whole_frac + " = ",font_size = 60, size_hint_y= None, height=100))
                    answer = str(int(whole_numer) + int(frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    
                # If the second is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("W + WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole = entry_list[1][:left_par]
                    print("whole",whole)
                    frac_sign_index = entry_list[1].find("/")
                    numer_a = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac = str(int(whole) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    print("frac",frac)                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " + " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[0]) * int(lcm))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(lcm)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " + " + frac + " = ",font_size = 60, size_hint_y= None, height=100))
                    answer = str(int(whole_numer) + int(frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole(Fraction) and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 2 and entry.count(")") == 2:
                print("ADD WF , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF + WF")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac_a = str(int(whole_a) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_a_sign = frac_a.find("/")
                    frac_numer_a = frac_a[:frac_a_sign]
                    
                    frac_sign_two = entry_list[1].find("/")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    numer_b = entry_list[1][left_par+1:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:right_par]
                    whole_b = entry_list[1][:left_par]
                    frac_b = str(int(whole_b) * int(denom_b) + int(numer_b)).replace(".0","") + "/" + str(denom_b)
                    frac_b_sign = frac_b.find("/")
                    frac_numer_b = frac_b[:frac_b_sign]
                    
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac_a + " + " + frac_b ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + frac_a + "(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + " + " + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")" +frac_b + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")",font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    lcm_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    lcm_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    numer_conv_a = str(int(frac_numer_a) * int(lcm_a)).replace(".0","")
                    numer_conv_b = str(int(frac_numer_b) * int(lcm_b)).replace(".0","")
                    answer = str(int(numer_conv_a) + int(numer_conv_b)) + "/" + str(lcm)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= numer_conv_a + "/" + str(lcm) + " + " + numer_conv_b + "/" + str(lcm),font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("ADD W , W")
                entry = entry.replace("$"," + ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry + " = ",font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
 
            #FRACTION ANSWER REDUCER               
            print("trying to reduce")    
            if answer != "" and sol == "":
                numer_sol_list = str(answer).split("/")
                print("numer_sol_list",numer_sol_list)
                if int(numer_sol_list[0]) > int(numer_sol_list[1]):
                    denom_sol = int(numer_sol_list[1])
                    numer_sol = int(numer_sol_list[0])
                    diff = numer_sol / denom_sol
                    print("diff",diff)
                    dec_index = str(diff).find(".")
                    print("dec_index",dec_index)
                    diff = str(diff)[:dec_index]
                    print("diff",diff)
                    remainder = str(numer_sol % denom_sol)
                    print("remainder ",remainder)
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder) + "/" + str(denom_sol) + ")",font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                   answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                   self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = 60, size_hint_y= None, height=100))
                   self.layouts.append(layout)  
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)  
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input " ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)

    def sub(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            answer = ""
            #Fraction and Fraction
            if entry.count("/") == 2 and entry.count("(") == 0 and entry.count(")") == 0:
                print("SUB F + F")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                if entry_list[0].count("/") == 1:
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_index]
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                if entry_list[1].count("/") == 1:
                    frac_sign_index = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_index]
                    denom_b = entry_list[1][frac_sign_index+1:]
                    print("denom_b",denom_b)
                lcm = str(np.lcm(int(denom_a),int(denom_b)))
                print("lcm",lcm)
                self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                if int(denom_a) != int(denom_b):
                    print()
                    diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + entry_list[0] + "(" + diff_a + ")" + " - " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = 60, size_hint_y= None, height=100))
                    numer_sub = str(int(diff_a) * int(numer_a) - int(diff_b) * int(numer_b))
                    answer = numer_sub + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    numer_sub = str(int(numer_b) - int(numer_a)).replace(".0","")
                    answer = numer_sub + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("SUB F + WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF - F")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_one = entry_list[0][:left_par]
                    print("whole_one",whole_one)
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    frac = str(int(whole_one) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + frac + "(" + diff_a + ")" + " - " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = 60, size_hint_y= None, height=100))
                        numer_sub = str(int(diff_a) * int(numer_a) - int(diff_b) * int(numer_b))
                        answer = numer_sub + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_sub = str((int(whole_one) * int(denom_a) + int(numer_a)) - int(numer_b)).replace(".0","")
                        answer = numer_sub + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("F - WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b",denom_b)
                    numer_b = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b",numer_b)
                    frac = str(int(whole_two) * int(denom_b) + int(numer_b)).replace(".0","") + "/" + str(denom_b)
                    print("frac",frac)
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_two+1:]
                    print("denom_a",denom_a)
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text=  entry_list[0] + " - "  + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + frac + "(" + diff_a + ")" + " - " + "(" + diff_b + ")" + entry_list[0] + "(" + diff_b + ")" + " = ",font_size = 60, size_hint_y= None, height=100))
                        numer_sub = str(int(diff_a) * int(numer_a) - int(diff_b) * int(numer_b))
                        answer = numer_sub + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_sub = str((int(numer_b) - int(whole_two) * int(denom_a) + int(numer_a))).replace(".0","")
                        answer = numer_sub + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
            #Fraction and Whole    
            if entry.count("/") == 1 and entry.count("(") == 0 and entry.count(")") == 0:
                print("SUB F - W")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the F
                if entry_list[0].count("(") == 0 and entry_list[0].count(")") == 0 and entry_list[0].count("/") == 1:
                    print("F - W")
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[1]) * int(lcm))
                    whole_frac = str(int(entry_list[1]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + whole_frac,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " - " + whole_frac,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(numer_a) - int(whole_frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the F
                if entry_list[1].count("(") == 0 and entry_list[1].count(")") == 0 and entry_list[1].count("/") == 1:
                    print("W - F")
                    frac_sign_index = entry_list[1].find("/")
                    denom_a = entry_list[1][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[0]) * int(lcm))
                    whole_frac = str(int(entry_list[0]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + whole_frac,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " - " + entry_list[1]  ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(whole_frac_numer) - int(numer_a)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole and Whole(Fraction)
            if entry.count("/") == 1 and entry.count("(") == 1 and entry.count(")") == 1:
                print("SUB W , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF - W")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole = entry_list[0][:left_par]
                    print("whole",whole)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac = str(int(whole) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[1]) * int(lcm))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(lcm)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    self.ids.list_of_steps.add_widget(Label(text= frac + " - " + whole_frac + " = ",font_size = 60, size_hint_y= None, height=100))
                    answer = str(int(frac_numer) - int(whole_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("W - WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole = entry_list[1][:left_par]
                    print("whole",whole)
                    frac_sign_index = entry_list[1].find("/")
                    numer_a = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac = str(int(whole) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    print("frac",frac)                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " - " + frac ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[0]) * int(lcm))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(lcm)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " - " + frac + " = ",font_size = 60, size_hint_y= None, height=100))
                    answer = str(int(whole_numer) - int(frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole(Fraction) and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 2 and entry.count(")") == 2:
                print("Sub WF , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF - WF")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    frac_a = str(int(whole_a) * int(denom_a) + int(numer_a)).replace(".0","") + "/" + str(denom_a)
                    frac_a_sign = frac_a.find("/")
                    frac_numer_a = frac_a[:frac_a_sign]
                    
                    frac_sign_two = entry_list[1].find("/")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    numer_b = entry_list[1][left_par+1:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:right_par]
                    whole_b = entry_list[1][:left_par]
                    frac_b = str(int(whole_b) * int(denom_b) + int(numer_b)).replace(".0","") + "/" + str(denom_b)
                    frac_b_sign = frac_b.find("/")
                    frac_numer_b = frac_b[:frac_b_sign]
                    
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac_a + " - " + frac_b ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + frac_a + "(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + " + " + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")" +frac_b + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")",font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    lcm_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    lcm_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    numer_conv_a = str(int(frac_numer_a) * int(lcm_a)).replace(".0","")
                    numer_conv_b = str(int(frac_numer_b) * int(lcm_b)).replace(".0","")
                    answer = str(int(numer_conv_a) - int(numer_conv_b)) + "/" + str(lcm)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= numer_conv_a + "/" + str(lcm) + " - " + numer_conv_b + "/" + str(lcm),font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("SUB W , W")
                entry = entry.replace("$"," - ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry + " = ",font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
 
            #FRACTION ANSWER REDUCER               
            print("trying to reduce")    
            if answer != "" and sol == "":
                num = 0
                if answer.count("-") > 0:
                    answer = answer.replace("-","")
                    num = 1
                numer_sol_list = str(answer).split("/")
                print("numer_sol_list",numer_sol_list)
                if int(numer_sol_list[0]) > int(numer_sol_list[1]):
                    denom_sol = int(numer_sol_list[1])
                    numer_sol = int(numer_sol_list[0])
                    diff = numer_sol / denom_sol
                    print("diff",diff)
                    dec_index = str(diff).find(".")
                    print("dec_index",dec_index)
                    diff = str(diff)[:dec_index]
                    print("diff",diff)
                    remainder = str(numer_sol % denom_sol)
                    print("remainder ",remainder)
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0:
                        if num > 0:
                            diff = "-" + diff
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        if num > 0:
                            diff = "-" + diff
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder) + "/" + str(denom_sol) + ")",font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    if num > 0:
                        answer = "-" + answer
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])
                    if num > 0:
                        answer = "-" + answer
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])
                    if num > 0:
                        answer = "-" + answer
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                   answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                   self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = 60, size_hint_y= None, height=100))
                   self.layouts.append(layout)  
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)  
                
                if num > 0:
                    answer = "-" + answer
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)

    def mult(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            if entry.count("/") == 2:
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                #a
                if entry_list[0].count("/") == 1:
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:].replace(")","")
                    print("denom_a",denom_a)
                
                if entry_list[1].count("/") == 1:
                    frac_sign_index = entry_list[1].find("/")
                    denom_b = entry_list[1][frac_sign_index+1:].replace(")","")
                    print("denom_b",denom_b)
                    
                self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout) 
                if entry_list[0].count("/") == 1:
                    frac_sign_index = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)
                    if numer_a.count("(") == 1:
                        left_par = numer_a.find("(")
                        whole_a = numer_a[:left_par]
                        par_sign_index = numer_a.find("(")
                        numer_a = numer_a[par_sign_index+1:]
                        print("numer_a",numer_a)
                        print("whole a",whole_a)
                        numer_a = str(int(whole_a) * int(denom_a) + int(numer_a))
                        self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " = " + numer_a + "/" + denom_a ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)  
                            
                if entry_list[1].count("/") == 1:
                    frac_sign_index = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_index]
                    print("numer_b",numer_b)
                    if numer_b.count("(") == 1:
                        left_par = numer_b.find("(")
                        whole_b = numer_b[:left_par]
                        par_sign_index = numer_b.find("(")
                        numer_b = numer_b[par_sign_index+1:]
                        print("numer_b",numer_b)
                        print("whole b",whole_b)
                        numer_b = str(int(whole_b) * int(denom_b) + int(numer_b))
                        self.ids.list_of_steps.add_widget(Label(text= entry_list[1] + " = " + numer_b + "/" + denom_b ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)  
                        
                numer_sol = str(int(numer_a) * int(numer_b)).replace(".0","")
                denom_sol = str(int(denom_a) * int(denom_b)).replace(".0","")
                self.ids.list_of_steps.add_widget(Label(text="Numerators: " + numer_a + " x " + numer_b + " = " + numer_sol,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text="Denomenators: " + denom_a + " x " + denom_b + " = " + denom_sol.replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= numer_sol + "/" + denom_sol,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)  
                
                sol = numer_sol + "/" + denom_sol
                numer_sol_list = sol.split("/")
                print("numer_sol_list",numer_sol_list)
                if int(numer_sol_list[0]) > int(numer_sol_list[1]):
                    denom_sol = int(numer_sol_list[1])
                    numer_sol = int(numer_sol_list[0])
                    diff = numer_sol / denom_sol
                    print("diff",diff)
                    dec_index = str(diff).find(".")
                    print("dec_index",dec_index)
                    diff = str(diff)[:dec_index]
                    print("diff",diff)
                    remainder = str(numer_sol % denom_sol)
                    print("remainder ",remainder)
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + remainder + "/" + str(denom_sol) + ")" ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    if int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                        print("Module 2")
                        while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                            numer_sol_list[0] = int(numer_sol_list[0]) / 2
                            print("numer_sol_list[0]",numer_sol_list[0])
                            numer_sol_list[1] = int(numer_sol_list[1]) / 2
                            print("numer_sol_list[1]",numer_sol_list[1])
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    if int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                        print("Module 3")
                        while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                            numer_sol_list[0] = int(numer_sol_list[0]) / 3
                            print("numer_sol_list[0]",numer_sol_list[0])
                            numer_sol_list[1] = int(numer_sol_list[1]) / 3
                            print("numer_sol_list[1]",numer_sol_list[1])
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    if int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                        print("Module 5")
                        while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                            numer_sol_list[0] = int(numer_sol_list[0]) / 5
                            print("numer_sol_list[0]",numer_sol_list[0])
                            numer_sol_list[1] = int(numer_sol_list[1]) / 5
                            print("numer_sol_list[1]",numer_sol_list[1])
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    if int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                       answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                       self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = 60, size_hint_y= None, height=100))
                       self.layouts.append(layout)  
                    
                    if int(numer_sol_list[0]) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
            elif entry.count("/") < 2:
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                if entry_list[0].count("/") == 0 and entry_list[1].count("/") > 0:
                    whole = int(entry_list[0])
                    print("whole",whole)
                    frac = entry_list[1]
                    print("frac",frac)
                    sign = frac.find("/")
                    print("sign",sign)
                    numera = int(str(frac)[:sign])
                    print("numera",numera)
                    numer = str(whole * numera).replace(".0","")
                    print("numer",numer)
                    answer = str(numer) + "/" + str(frac[sign+1:])
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + str(whole) + " x " + str(frac) ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(whole) + " x " + str(numera) + " = " + str(numer),font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    numer_sol_list = answer.split("/")
                    print("numer_sol_list",numer_sol_list)
                    if int(numer_sol_list[0]) > int(numer_sol_list[1]):
                        denom_sol = int(numer_sol_list[1])
                        numer_sol = int(numer_sol_list[0])
                        diff = numer_sol / denom_sol
                        print("diff",diff)
                        dec_index = str(diff).find(".")
                        print("dec_index",dec_index)
                        diff = str(diff)[:dec_index]
                        print("diff",diff)
                        remainder = str(numer_sol % denom_sol)
                        print("remainder ",remainder)
                        sol = "(" + remainder + "/" + str(denom_sol) + ")"
                        if int(remainder) == 0:
                            sol = ""
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + sol ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        if int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                            print("Module 2")
                            while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                                numer_sol_list[0] = int(numer_sol_list[0]) / 2
                                print("numer_sol_list[0]",numer_sol_list[0])
                                numer_sol_list[1] = int(numer_sol_list[1]) / 2
                                print("numer_sol_list[1]",numer_sol_list[1])
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        if int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                            print("Module 3")
                            while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                                numer_sol_list[0] = int(numer_sol_list[0]) / 3
                                print("numer_sol_list[0]",numer_sol_list[0])
                                numer_sol_list[1] = int(numer_sol_list[1]) / 3
                                print("numer_sol_list[1]",numer_sol_list[1])
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        if int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                            print("Module 5")
                            while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                                numer_sol_list[0] = int(numer_sol_list[0]) / 5
                                print("numer_sol_list[0]",numer_sol_list[0])
                                numer_sol_list[1] = int(numer_sol_list[1]) / 5
                                print("numer_sol_list[1]",numer_sol_list[1])
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        if int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                           answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                           self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = 60, size_hint_y= None, height=100))
                           self.layouts.append(layout)  
                        
                        if int(numer_sol_list[0]) == 0:
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = 60, size_hint_y= None, height=100))
                            self.layouts.append(layout)
                
                elif entry_list[0].count("/") > 0 and entry_list[1].count("/") == 0:
                    whole = int(entry_list[1])
                    print("whole",whole)
                    frac = entry_list[0]
                    print("frac",frac)
                    sign = frac.find("/")
                    print("sign",sign)
                    numera = int(str(frac)[:sign])
                    print("numera",numera)
                    numer = str(whole * numera).replace(".0","")
                    print("numer",numer)
                    answer = str(numer) + "/" + str(frac[sign+1:])
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + str(whole) + " x " + str(frac) ,font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(whole) + " x " + str(numera) + " = " + str(numer),font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    numer_sol_list = answer.split("/")
                    print("numer_sol_list",numer_sol_list)
                    if int(numer_sol_list[0]) > int(numer_sol_list[1]):
                        denom_sol = int(numer_sol_list[1])
                        numer_sol = int(numer_sol_list[0])
                        diff = numer_sol / denom_sol
                        print("diff",diff)
                        dec_index = str(diff).find(".")
                        print("dec_index",dec_index)
                        diff = str(diff)[:dec_index]
                        print("diff",diff)
                        remainder = str(numer_sol % denom_sol)
                        print("remainder ",remainder)
                        sol = "(" + remainder + "/" + str(denom_sol) + ")"
                        if int(remainder) == 0:
                            sol = ""
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + sol ,font_size = 60, size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        if int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                            print("Module 2")
                            while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                                numer_sol_list[0] = int(numer_sol_list[0]) / 2
                                print("numer_sol_list[0]",numer_sol_list[0])
                                numer_sol_list[1] = int(numer_sol_list[1]) / 2
                                print("numer_sol_list[1]",numer_sol_list[1])
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        if int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                            print("Module 3")
                            while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                                numer_sol_list[0] = int(numer_sol_list[0]) / 3
                                print("numer_sol_list[0]",numer_sol_list[0])
                                numer_sol_list[1] = int(numer_sol_list[1]) / 3
                                print("numer_sol_list[1]",numer_sol_list[1])
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        if int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                            print("Module 5")
                            while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                                numer_sol_list[0] = int(numer_sol_list[0]) / 5
                                print("numer_sol_list[0]",numer_sol_list[0])
                                numer_sol_list[1] = int(numer_sol_list[1]) / 5
                                print("numer_sol_list[1]",numer_sol_list[1])
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = 60, size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        if int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                           answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                           self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = 60, size_hint_y= None, height=100))
                           self.layouts.append(layout)  
                        
                        if int(numer_sol_list[0]) == 0:
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = 60, size_hint_y= None, height=100))
                            self.layouts.append(layout)
                
                else:
                    entry_list = entry.split("$")
                    print("entry_list",entry_list)
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1],font_size = 60, size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(int(entry_list[0]) * int(entry_list[1])).replace(".0",""),font_size = 60, size_hint_y= None, height=100))
                    self.layouts.append(layout)  
                
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)

    def div(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            if entry.count("/") == 2:
                
                
                self.ids.list_of_steps.add_widget(Label(text= "d" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)

class Homepage(Screen):
    pass            
           
sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Fractions(name="Fractions"))     
sm.current = "Homepage"   


class Fractions(App):
    def build(app):
        return sm

if __name__ == '__main__':
    Fractions().run()
    

