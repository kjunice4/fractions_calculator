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
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "Tap anywhere to continue"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left"         
                
        Button:
            font_size: 50
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared-Mathematics : Fractions Calculator"
            on_release:
                app.root.current = "Menu"
                root.manager.transition.direction = "left" 
""")

# Menu
Builder.load_string("""
<Menu>
    id:Menu
    name:"Menu"
    
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
                text: "Menu"
            
            Button:
                text: "Fraction Steps Calculator"   
                font_size: 75
                background_color: 0, 0 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Fractions"
                    root.manager.transition.direction = "left" 
            
            Button:
                text: "Fraction Converter"  
                font_size: 75
                background_color: 0, 1 , 1 , 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Fractions_converter"
                    root.manager.transition.direction = "left"         
            
            Button:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Visit KSquared-Mathematics"
                on_release:
                    import webbrowser
                    webbrowser.open('https://www.ksquaredmathematics.com/subscribe') 
            
            Button:
                font_size: 75
                background_color: 1, 0, 1, 1
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new?"
                on_release:
                    app.root.current = "updates"
                    root.manager.transition.direction = "left"
                    
            Label:
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Share KSquared-Mathematics"
                    
            Image:
                source: 'KSquared_QR.png'
                size_hint_y: None
                height: 1000
                width: 1000
""")

#Updates
Builder.load_string("""
<updates>
    id:updates
    name:"updates"
    
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
                font_size: 60
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "What's new at KSquared-Mathematics?"
            
            Button:
                id: steps
                text: "Menu"   
                font_size: 75
                size_hint_y: None
                background_color: 0, 0 , 1 , 1
                height: 200
                padding: 10, 10
                on_release:
                    app.root.current = "Menu"
                    root.manager.transition.direction = "right" 
                    
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Fractions Calculator v0.1"
                
            Label:
                font_size: 40
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "No new updates as of 1/26/2022"
            
""")

# Fractions Calculator
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
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Fraction Steps Calculator"
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    text: "Menu"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        a.text = ""
                        b.text = ""
                        list_of_steps.clear_widgets()            
                    
            Label:
                font_size: '15sp'
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
        
                TextInput:
                    id: a
                    text: a.text
                    hint_text: "Fraction 1:"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5        
                                                    
                TextInput:
                    id: b
                    text: b.text
                    hint_text:  "Fraction 2:"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5  
    
                Button:
                    id: steps
                    text: "+"   
                    font_size: '20sp'
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
                    font_size: '20sp'
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
                    font_size: '20sp'
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
                    font_size: '20sp'
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
                self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                if int(denom_a) != int(denom_b):
                    print()
                    diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + entry_list[0] + "(" + diff_a + ")" + " + " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " + " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    numer_added = str(int(diff_a) * int(numer_a) + int(diff_b) * int(numer_b))
                    answer = numer_added + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    numer_added = str(int(numer_b) + int(numer_a)).replace(".0","")
                    answer = numer_added + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("ADD F & WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF + F")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_one = entry_list[0][:left_par]
                    print("whole_one",whole_one)
                    frac_sign_index = entry_list[0].find("/")
                    denom_a_pre = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a_pre",denom_a_pre)
                    numer_a_pre = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a_pre",numer_a_pre)
                    wf = str(int(whole_one) * int(denom_a_pre) + int(numer_a_pre)).replace(".0","") + "/" + str(denom_a_pre)
                    print("wf",wf)
                    frac_sign_index = wf.find("/")
                    denom_a = wf[frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = wf[:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    frac = entry_list[1]
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]
                    
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + wf ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= wf + " + " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + wf + "(" + diff_a + ")" + " + " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " + " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))                        
                        numer_add = str(int(diff_a) * int(numer_a) + int(diff_b) * int(numer_b))
                        answer = numer_add + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_added = str(int(numer_a) + int(numer_b)).replace(".0","")
                        answer = numer_added + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b_pre = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b_pre",denom_b_pre)
                    numer_b_pre = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b_pre",numer_b_pre)
                    wf = str(int(whole_two) * int(denom_b_pre) + int(numer_b_pre)).replace(".0","") + "/" + str(denom_b_pre)
                    print("wf",wf)
                    frac_sign_index = wf.find("/")
                    denom_b = wf[frac_sign_index+1:]
                    print("denom_b",denom_b)
                    numer_b = wf[:frac_sign_index]
                    print("numer_b",numer_b)
                    
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[0].find("/")
                    numer_a = entry_list[0][:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = entry_list[0][frac_sign_two+1:]
                    print("denom_a",denom_a)
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + wf ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " + " + wf ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + entry_list[0] + "(" + diff_a + ")" + " + " + "(" + diff_b + ")" + wf + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " + " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))                        
                        numer_add = str(int(diff_a) * int(numer_a) + int(diff_b) * int(numer_b))
                        answer = numer_add + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_added = str(int(numer_a) + int(numer_b)).replace(".0","")
                        answer = numer_added + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        
            #Fraction and Whole    
            if entry.count("/") == 1 and entry.count("(") == 0 and entry.count(")") == 0:
                print("ADD F + W")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the F
                if entry_list[0].count("(") == 0 and entry_list[0].count(")") == 0 and entry_list[0].count("/") == 1:
                    print("F + W")
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[1]) * int(lcm))
                    whole_frac = str(int(entry_list[1]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " + " + whole_frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(whole_frac_numer) + int(numer_a)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the F
                if entry_list[1].count("(") == 0 and entry_list[1].count(")") == 0 and entry_list[1].count("/") == 1:
                    print("w + F")
                    frac_sign_index = entry_list[1].find("/")
                    denom_a = entry_list[1][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][:frac_sign_index]
                    print("numer_a",numer_a)
                    lcm = denom_a
                    print("lcm",lcm)
                    whole_frac_numer = str(int(entry_list[0]) * int(lcm))
                    whole_frac = str(int(entry_list[0]) * int(lcm)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " + " + entry_list[1] + " = "  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(whole_frac_numer) + int(numer_a)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
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
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[1]) * int(lcm))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(lcm)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    frac_denom = frac[frac_div_sign+1:]
                    lcm_diff = str(int(lcm) / int(frac_denom)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= "(" + lcm_diff + ")" + frac + "(" + lcm_diff + ")" + " + " + whole_frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(int(lcm_diff) * int(frac_numer)) + "/"  + str(int(lcm_diff) * int(frac_denom)) + " + " + whole_frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    frac_numer = str(int(lcm_diff) * int(frac_numer))
                    answer = str(int(whole_numer) + int(frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
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
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " + " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[0]) * int(lcm))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(lcm)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    frac_denom = frac[frac_div_sign+1:]
                    lcm_diff = str(int(lcm) / int(frac_denom)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " + " + "(" + lcm_diff + ")" + frac + "(" + lcm_diff + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text=   whole_frac + " + " + str(int(lcm_diff) * int(frac_numer)) + "/" + str(int(lcm_diff) * int(frac_denom))  + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    frac_numer = str(int(lcm_diff) * int(frac_numer))
                    answer = str(int(whole_numer) + int(frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
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
                    self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry_list[0] + " + " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac_a + " + " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + frac_a + "(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + " + " + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")" +frac_b + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    lcm_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    lcm_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    numer_conv_a = str(int(frac_numer_a) * int(lcm_a)).replace(".0","")
                    numer_conv_b = str(int(frac_numer_b) * int(lcm_b)).replace(".0","")
                    answer = str(int(numer_conv_a) + int(numer_conv_b)) + "/" + str(lcm)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= numer_conv_a + "/" + str(lcm) + " + " + numer_conv_b + "/" + str(lcm),font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("ADD W , W")
                entry = entry.replace("$"," + ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Add: " + entry + " = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = '15sp', size_hint_y= None, height=100))
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
                    
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0 and int(remainder) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                            while int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 2
                                print("remainder reduced further 2: ",remainder)
                                denom_sol = int(denom_sol) / 2
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 3
                                print("remainder reduced further 3: ",remainder)
                                denom_sol = int(denom_sol) / 3
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 5
                                print("remainder reduced further 5: ",remainder)
                                denom_sol = int(denom_sol) / 5
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                   answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                   self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = '15sp', size_hint_y= None, height=100))
                   self.layouts.append(layout)  
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)  
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input " ,font_size = '15sp', size_hint_y= None, height=100))
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
                print("SUB F - F")
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
                self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                if int(denom_a) != int(denom_b):
                    print()
                    diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + entry_list[0] + "(" + diff_a + ")" + " - " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " - " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    numer_sub = str(int(diff_a) * int(numer_a) - int(diff_b) * int(numer_b))
                    answer = numer_sub + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    numer_sub = str(int(numer_a) - int(numer_b)).replace(".0","")
                    answer = numer_sub + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("SUB F - WF")
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
                    denom_a_pre = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a_pre",denom_a_pre)
                    numer_a_pre = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a_pre",numer_a_pre)
                    frac = str(int(whole_one) * int(denom_a_pre) + int(numer_a_pre)).replace(".0","") + "/" + str(denom_a_pre)
                    frac_sign_index = frac.find("/")
                    denom_a = frac[frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = frac[:frac_sign_index]
                    print("numer_a",numer_a)
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    denom_b = entry_list[1][frac_sign_two+1:]
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_a + ")" + frac + "(" + diff_a + ")" + " - " + "(" + diff_b + ")" + entry_list[1] + "(" + diff_b + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " - " + str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        numer_sub = str(int(diff_a) * int(numer_a) - int(diff_b) * int(numer_b))
                        answer = numer_sub + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_sub = str(int(numer_a) - int(numer_b)).replace(".0","")
                        print("numer_sub",numer_sub)
                        answer = numer_sub + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("F - WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b_pre = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b_pre",denom_b_pre)
                    numer_b_pre = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b_pre",numer_b_pre)
                    frac = str(int(whole_two) * int(denom_b_pre) + int(numer_b_pre)).replace(".0","") + "/" + str(denom_b_pre)
                    print("frac",frac)
                    frac_sign_two = frac.find("/")
                    numer_a = frac[:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = frac[frac_sign_two+1:]
                    print("denom_a",denom_a)
                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]
                    
                    lcm = str(np.lcm(int(denom_a),int(denom_b)))
                    print("lcm",lcm)
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text=  entry_list[0] + " - "  + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    if int(denom_a) != int(denom_b):
                        print()
                        diff_a = str(int(lcm) / int(denom_a)).replace(".0","")
                        diff_b = str(int(lcm) / int(denom_b)).replace(".0","")
                        self.ids.list_of_steps.add_widget(Label(text= "(" + diff_b + ")" + entry_list[0] + "(" + diff_b + ")" + " - " + "(" + diff_a + ")" + frac + "(" + diff_a + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        self.ids.list_of_steps.add_widget(Label(text= str(int(diff_b) * int(numer_b)).replace(".0","") + "/" + str(int(diff_b) * int(denom_b)).replace(".0","") + " - " + str(int(diff_a) * int(numer_a)).replace(".0","") + "/" + str(int(diff_a) * int(denom_a)).replace(".0","") + " = ",font_size = '15sp', size_hint_y= None, height=100))
                        numer_sub = str(int(diff_b) * int(numer_b) - int(diff_a) * int(numer_a))
                        answer = numer_sub + "/" + str(lcm) 
                        self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        numer_sub = str(int(numer_b) - int(numer_a)).replace(".0","")
                        answer = numer_sub + "/" + str(lcm)
                        self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
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
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " - " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(numer_a) - int(whole_frac_numer)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
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
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + whole_frac,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " - " + entry_list[1]  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(whole_frac_numer) - int(numer_a)) + "/" + str(lcm)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
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

                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " - " + entry_list[1] + " = " ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[1]) * int(denom_a))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(denom_a)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    self.ids.list_of_steps.add_widget(Label(text= frac + " - " + whole_frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    
                    answer = str(int(frac_numer) - int(whole_numer)) + "/" + str(denom_a)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
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

                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " - " + frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    whole_numer = str(int(entry_list[0]) * int(denom_a))
                    print("whole_numer",whole_numer)
                    whole_frac = whole_numer + "/" + str(denom_a)
                    print("whole_frac",whole_frac)
                    frac_div_sign = frac.find("/")
                    frac_numer = frac[:frac_div_sign]
                    self.ids.list_of_steps.add_widget(Label(text= whole_frac + " - " + frac + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    
                    answer = str(int(whole_numer) - int(frac_numer)) + "/" + str(denom_a)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
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
                    self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry_list[0] + " - " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac_a + " - " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + lcm ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text="(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + frac_a + "(" + str(int(lcm) / int(denom_a)).replace(".0","") + ")" + " - " + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")" +frac_b + "(" + str(int(lcm) / int(denom_b)).replace(".0","") + ")" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    lcm_a = str(int(lcm) / int(denom_a)).replace(".0","")
                    lcm_b = str(int(lcm) / int(denom_b)).replace(".0","")
                    numer_conv_a = str(int(frac_numer_a) * int(lcm_a)).replace(".0","")
                    numer_conv_b = str(int(frac_numer_b) * int(lcm_b)).replace(".0","")
                    answer = str(int(numer_conv_a) - int(numer_conv_b)) + "/" + str(lcm)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= numer_conv_a + "/" + str(lcm) + " - " + numer_conv_b + "/" + str(lcm) + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("SUB W , W")
                entry = entry.replace("$"," - ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Subtract: " + entry + " = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = '15sp', size_hint_y= None, height=100))
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
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0 and int(remainder) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                            remainder = int(remainder) / 2
                            print("remainder reduced further",remainder)
                            denom_sol = int(denom_sol) / 2
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                            remainder = int(remainder) / 3
                            print("remainder reduced further",remainder)
                            denom_sol = int(denom_sol) / 3
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                            remainder = int(remainder) / 5
                            print("remainder reduced further",remainder)
                            denom_sol = int(denom_sol) / 5
                            self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder) + "/" + str(denom_sol) + ")",font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0:
                            while int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0:
                                remainder = int(remainder) / 2
                                print("remainder reduced further 2:",remainder)
                                denom_sol = int(denom_sol) / 2
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0:
                            while int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0:
                                remainder = int(remainder) / 3
                                print("remainder reduced further",remainder)
                                denom_sol = int(denom_sol) / 3
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0:
                            while int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0:
                                remainder = int(remainder) / 5
                                print("remainder reduced further",remainder)
                                denom_sol = int(denom_sol) / 5
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])

                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ answer  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)  
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)

    def mult(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            answer = ""
            #Fraction and Fraction
            if entry.count("/") == 2 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Mult F * F")
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
                    
                Numerators = numer_a + " x " + numer_b
                Denomenators = denom_a + " x " + denom_b
                N_sol = str(int(numer_a) * int(numer_b))
                D_sol = str(int(denom_a) * int(denom_b))
                self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                Numerators = str(int(numer_a) * int(numer_b))
                Denomenators = str(int(denom_a) * int(denom_b))
                answer = Numerators + "/" + Denomenators
                self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)     
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("Mult F * WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF * F")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_one = entry_list[0][:left_par]
                    print("whole_one",whole_one)
                    frac_sign_index = entry_list[0].find("/")
                    denom_a_pre = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a_pre",denom_a_pre)
                    numer_a_pre = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a_pre",numer_a_pre)
                    frac = str(int(whole_one) * int(denom_a_pre) + int(numer_a_pre)).replace(".0","") + "/" + str(denom_a_pre)
                    frac_sign_index = frac.find("/")
                    denom_a = frac[frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = frac[:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    print("numer_b",numer_b)
                    denom_b = entry_list[1][frac_sign_two+1:]
                    print("denom_b",denom_b)
                    
                    Numerators = str(numer_a + " x " + numer_b)
                    N_sol = str(int(numer_a) * int(numer_b))
                    Denomenators = str(denom_a + " x " + denom_b)
                    D_sol = str(int(denom_a) * int(denom_b))

                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol + "/" + D_sol)
                    
                    self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("F * WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b_pre = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b_pre",denom_b_pre)
                    numer_b_pre = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b_pre",numer_b_pre)
                    frac = str(int(whole_two) * int(denom_b_pre) + int(numer_b_pre)).replace(".0","") + "/" + str(denom_b_pre)
                    print("frac",frac)
                    frac_sign_two = frac.find("/")
                    numer_a = frac[:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = frac[frac_sign_two+1:]
                    print("denom_a",denom_a)
                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]
                    
                    Numerators = str(numer_a + " x " + numer_b)
                    N_sol = str(int(numer_a) * int(numer_b))
                    Denomenators = str(denom_a + " x " + denom_b)
                    D_sol = str(int(denom_a) * int(denom_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text=  entry_list[0] + " x "  + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol + "/" + D_sol)
                    
                    self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                        
            #Fraction and Whole    
            if entry.count("/") == 1 and entry.count("(") == 0 and entry.count(")") == 0:
                print("MULT F * W")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the F
                if entry_list[0].count("(") == 0 and entry_list[0].count(")") == 0 and entry_list[0].count("/") == 1:
                    print("F * W")
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)

                    Numerators = str(numer_a + " x " + entry_list[1])
                    Denomenators = str(denom_a + " x " + str(1))
                    Numerators_sol = str(int(numer_a) * int(entry_list[1]))
                    Denomenators_sol = str(int(denom_a) * int(1))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " x " + entry_list[1]+ "/1" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(numer_a) * int(entry_list[1])) + "/" + str(int(denom_a) * int(1))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the F
                if entry_list[1].count("(") == 0 and entry_list[1].count(")") == 0 and entry_list[1].count("/") == 1:
                    print("W * F")
                    frac_sign_index = entry_list[1].find("/")
                    denom_a = entry_list[1][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    Numerators = str(entry_list[0] + " x " + numer_a)
                    Denomenators = str(denom_a + " x " + str(1))
                    Numerators_sol = str(int(numer_a) * int(entry_list[0]))
                    Denomenators_sol = str(int(denom_a) * int(1))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + "/1" + " x " + entry_list[1] + " = " ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators +" = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer =  str(int(numer_a) * int(entry_list[0])) + "/" + str(int(1) * int(denom_a))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole and Whole(Fraction)
            if entry.count("/") == 1 and entry.count("(") == 1 and entry.count(")") == 1:
                print("MULT W , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF * W")
                    frac_sign_index = entry_list[0].find("/")
                    right_par = entry_list[0].find(")")
                    left_par = entry_list[0].find("(")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    wf = str(int(whole_a) * int(denom_a) + int(numer_a)) + "/" + str(denom_a)
                    wf_numer = str(int(whole_a) * int(denom_a) + int(numer_a))
                    
                    Numerators = str(wf_numer + " x " + entry_list[1])
                    Denomenators = str(denom_a + " x " + str(1))
                    Numerators_sol = str(int(wf_numer) * int(entry_list[1]))
                    Denomenators_sol = str(int(denom_a) * int(1))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + wf,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= wf + " x " + entry_list[1] + "/1" + " = ",font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(int(wf_numer) * int(entry_list[1])) + "/" + str(int(denom_a) * int(1))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1 and entry_list[1].count("/") == 1:
                    print("W * WF")
                    frac_sign_index = entry_list[1].find("/")
                    right_par = entry_list[1].find(")")
                    left_par = entry_list[1].find("(")
                    whole_a = entry_list[1][:left_par]
                    print("whole_a",whole_a)
                    denom_a = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    wf = str(int(whole_a) * int(denom_a) + int(numer_a)) + "/" + str(denom_a)
                    wf_numer = str(int(whole_a) * int(denom_a) + int(numer_a))
                    
                    Numerators = str(entry_list[0] + " x " + wf_numer)
                    Denomenators = str(denom_a + " x " + str(1))
                    Numerators_sol = str(int(wf_numer) * int(entry_list[0]))
                    Denomenators_sol = str(int(denom_a) * int(1))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + wf,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= entry_list[0] + " x " + wf + " = " ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators +" = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer =  str(int(wf_numer) * int(entry_list[0])) + "/" + str(int(1) * int(denom_a))
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole(Fraction) and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 2 and entry.count(")") == 2:
                print("MULT WF , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1 and entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("WF * WF")
                    
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
                    
                    Numerator = str(int(frac_numer_a) * int(frac_numer_b))
                    Denomenator = str(int(denom_a) * int(denom_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= frac_a + " x " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + frac_numer_a + " x " + frac_numer_b + " = " + Numerator,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + denom_a + " x " + denom_b + " = " + Denomenator ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)

                    answer = str(Numerator + "/" + Denomenator)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Mult W , W")
                entry = entry.replace("$"," * ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry + " = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = '15sp', size_hint_y= None, height=100))
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
                    
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0 and int(remainder) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                            while int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 2
                                print("remainder reduced further 2: ",remainder)
                                denom_sol = int(denom_sol) / 2
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 3
                                print("remainder reduced further 3: ",remainder)
                                denom_sol = int(denom_sol) / 3
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 5
                                print("remainder reduced further 5: ",remainder)
                                denom_sol = int(denom_sol) / 5
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                   answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                   self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = '15sp', size_hint_y= None, height=100))
                   self.layouts.append(layout)  
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout) 
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)

    def div(self,entry):
        layout = GridLayout(cols=1,size_hint_y= None)
        self.ids.list_of_steps.add_widget(layout)
        self.layouts.append(layout)
        try:
            print("entry",entry)
            answer = ""
            #Fraction and Fraction
            if entry.count("/") == 2 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Div F / F")
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
                    
                Reciprocal = str(denom_b+ "/" + numer_b)
                Numerators = numer_a + " x " + denom_b 
                Denomenators = denom_a + " x " + numer_b
                N_sol = str(int(numer_a) * int(denom_b))
                D_sol = str(int(denom_a) * int(numer_b))
                self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + Reciprocal + " = " ,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                Numerators = str(int(numer_a) * int(denom_b))
                Denomenators = str(int(denom_a) * int(numer_b))
                answer = Numerators + "/" + Denomenators
                self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)     
                
            #Fraction and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 1 and entry.count(")") == 1:
                print("Div F / WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF / F")
                    left_par = entry_list[0].find("(")
                    right_par = entry_list[0].find(")")
                    whole_one = entry_list[0][:left_par]
                    print("whole_one",whole_one)
                    frac_sign_index = entry_list[0].find("/")
                    denom_a_pre = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a_pre",denom_a_pre)
                    numer_a_pre = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a_pre",numer_a_pre)
                    frac = str(int(whole_one) * int(denom_a_pre) + int(numer_a_pre)).replace(".0","") + "/" + str(denom_a_pre)
                    frac_sign_index = frac.find("/")
                    denom_a = frac[frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = frac[:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    #find denom of 2nd frac
                    frac_sign_two = entry_list[1].find("/")
                    numer_b = entry_list[1][:frac_sign_two]
                    print("numer_b",numer_b)
                    denom_b = entry_list[1][frac_sign_two+1:]
                    print("denom_b",denom_b)
                    
                    Reciprocal = str(denom_b+ "/" + numer_b)
                    Numerators = numer_a + " x " + denom_b 
                    Denomenators = denom_a + " x " + numer_b
                    N_sol = str(int(numer_a) * int(denom_b))
                    D_sol = str(int(denom_a) * int(numer_b))

                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + frac + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol + "/" + D_sol)
                    
                    self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second frac is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("F / WF")
                    left_par = entry_list[1].find("(")
                    right_par = entry_list[1].find(")")
                    whole_two = entry_list[1][:left_par]
                    print("whole_two",whole_two)
                    frac_sign_index = entry_list[1].find("/")
                    denom_b_pre = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b_pre",denom_b_pre)
                    numer_b_pre = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b_pre",numer_b_pre)
                    frac = str(int(whole_two) * int(denom_b_pre) + int(numer_b_pre)).replace(".0","") + "/" + str(denom_b_pre)
                    print("frac",frac)
                    frac_sign_two = frac.find("/")
                    numer_a = frac[:frac_sign_two]
                    print("numer_a",numer_a)
                    denom_a = frac[frac_sign_two+1:]
                    print("denom_a",denom_a)
                    
                    frac_sign_two = entry_list[0].find("/")
                    numer_b = entry_list[0][:frac_sign_two]
                    denom_b = entry_list[0][frac_sign_two+1:]
                    
                    Reciprocal = str(denom_a + "/" + numer_a)
                    Numerators = numer_b + " x " + denom_a 
                    Denomenators = denom_b + " x " + numer_a
                    N_sol = str(int(numer_b) * int(denom_a))
                    D_sol = str(int(denom_b) * int(numer_a))

                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + frac + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol + "/" + D_sol)
                    
                    self.ids.list_of_steps.add_widget(Label(text= answer,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                        
            #Fraction and Whole    
            if entry.count("/") == 1 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Div F / W")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first frac is the F
                if entry_list[0].count("(") == 0 and entry_list[0].count(")") == 0 and entry_list[0].count("/") == 1:
                    print("F / W")
                    frac_sign_index = entry_list[0].find("/")
                    denom_a = entry_list[0][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][:frac_sign_index]
                    print("numer_a",numer_a)

                    numer_b = str(entry_list[1])
                    denom_b = str(1)
                    
                    Reciprocal = str(denom_b + "/" + numer_b)
                    Numerators = numer_a + " x " + denom_b 
                    Denomenators = denom_a + " x " + numer_b
                    N_sol = str(int(numer_a) * int(denom_b))
                    D_sol = str(int(denom_a) * int(numer_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol) + "/" + str(D_sol)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the F
                if entry_list[1].count("(") == 0 and entry_list[1].count(")") == 0 and entry_list[1].count("/") == 1:
                    print("W / F")
                    frac_sign_index = entry_list[1].find("/")
                    denom_a = entry_list[1][frac_sign_index+1:]
                    print("denom_a",denom_a)
                    numer_a = entry_list[1][:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    numer_b = str(entry_list[0])
                    denom_b = str(1)
                    
                    whole_frac = numer_b + "/" + denom_b
                    
                    Reciprocal = str(denom_a + "/" + numer_a)
                    Numerators = numer_b + " x " + denom_a
                    Denomenators = denom_b + " x " + numer_a
                    N_sol = str(int(denom_a) * int(numer_b))
                    D_sol = str(int(numer_a) * int(denom_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + whole_frac + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + N_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + D_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(N_sol) + "/" + str(D_sol)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole and Whole(Fraction)
            if entry.count("/") == 1 and entry.count("(") == 1 and entry.count(")") == 1:
                print("Div W , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1:
                    print("WF / W")
                    frac_sign_index = entry_list[0].find("/")
                    right_par = entry_list[0].find(")")
                    left_par = entry_list[0].find("(")
                    whole_a = entry_list[0][:left_par]
                    print("whole_a",whole_a)
                    denom_a = entry_list[0][frac_sign_index+1:right_par]
                    print("denom_a",denom_a)
                    numer_a = entry_list[0][left_par+1:frac_sign_index]
                    print("numer_a",numer_a)
                    
                    wf = str(int(whole_a) * int(denom_a) + int(numer_a)) + "/" + str(denom_a)
                    wf_numer = str(int(whole_a) * int(denom_a) + int(numer_a))
                    
                    Reciprocal = str("1/" + entry_list[1])
                    Numerators = str(wf_numer + " x " + str(1))
                    Denomenators = str(denom_a + " x " + entry_list[1])
                    Numerators_sol = str(int(wf_numer) * int(1))
                    Denomenators_sol = str(int(denom_a) * int(entry_list[1]))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + wf,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + entry_list[1] + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + wf + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(Numerators_sol) + "/" + str(Denomenators_sol)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                # If the second is the WF
                if entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1 and entry_list[1].count("/") == 1:
                    print("W / WF")
                    frac_sign_index = entry_list[1].find("/")
                    right_par = entry_list[1].find(")")
                    left_par = entry_list[1].find("(")
                    whole_b = entry_list[1][:left_par]
                    print("whole_b",whole_b)
                    denom_b = entry_list[1][frac_sign_index+1:right_par]
                    print("denom_b",denom_b)
                    numer_b = entry_list[1][left_par+1:frac_sign_index]
                    print("numer_b",numer_b)
                    
                    wf = str(int(whole_b) * int(denom_b) + int(numer_b)) + "/" + str(denom_b)
                    wf_numer = str(int(whole_b) * int(denom_b) + int(numer_b))
                    
                    Reciprocal = str(denom_b + "/" + wf_numer)
                    Numerators = str(entry_list[0] + " x " + denom_b)
                    Denomenators = str("1" + " x " + wf_numer)
                    Numerators_sol = str(int(entry_list[0]) * int(wf_numer))
                    Denomenators_sol = str(int(1) * int(denom_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + wf,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + wf + " = " + Reciprocal,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + entry_list[0] + "/1" + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + Numerators + " = " + Numerators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + Denomenators + " = " + Denomenators_sol,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    answer = str(Numerators_sol) + "/" + str(Denomenators_sol)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            #Whole(Fraction) and Whole(Fraction)
            if entry.count("/") == 2 and entry.count("(") == 2 and entry.count(")") == 2:
                print("Div WF , WF")
                entry_list = entry.split("$")
                print("entry_list",entry_list)
                
                # If first is the WF
                if entry_list[0].count("(") == 1 and entry_list[0].count(")") == 1 and entry_list[1].count("(") == 1 and entry_list[1].count(")") == 1:
                    print("WF / WF")
                    
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
                    frac_denom_b = frac_b[frac_b_sign+1:]
                    
                    Reciprocal = str(frac_denom_b + "/" + frac_numer_b)
                    Numerator = str(int(frac_numer_a) * int(frac_denom_b))
                    Denomenator = str(int(denom_a) * int(frac_numer_b))
                    
                    self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry_list[0] + " ÷ " + entry_list[1] ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[0] + " = " + frac_a ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Convert: " + entry_list[1] + " = " + frac_b ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Reciprocal: " + frac_b + " = " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Multiply: " + frac_a + " x " + Reciprocal ,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Numerators: " + frac_numer_a + " x " + frac_denom_b + " = " + Numerator,font_size = '15sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= "Denomenators: " + denom_a + " x " + frac_numer_b + " = " + Denomenator ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)

                    answer = str(Numerator + "/" + Denomenator)
                    print("answer",answer)
                    self.ids.list_of_steps.add_widget(Label(text= answer ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
            sol = ""        
            #Whole and Whole   
            if entry.count("/") == 0 and entry.count("(") == 0 and entry.count(")") == 0:
                print("Div W , W")
                entry = entry.replace("$"," / ")
                print("entry",entry)
                sol = str(eval(str(entry)))
                print("sol",sol)
                self.ids.list_of_steps.add_widget(Label(text= "Divide: " + entry + " = ",font_size = '15sp', size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= sol ,font_size = '15sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
 
            #FRACTION ANSWER REDUCER               
            print("trying to reduce")    
            if answer != "" and sol == "":
                numer_sol_list = str(answer).split("/")
                print("numer_sol_list",numer_sol_list)
                
                if int(numer_sol_list[1]) == 0:
                    print("Undefined")
                    self.ids.list_of_steps.add_widget(Label(text="Undefined" ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                
                elif int(numer_sol_list[0]) > int(numer_sol_list[1]):
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
                    
                    if int(numer_sol_list[0]) % int(numer_sol_list[1]) == 0 and int(remainder) == 0:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff ,font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    else:
                        self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                        if int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                            while int(remainder) % 2 == 0 and int(denom_sol) % 2 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 2
                                print("remainder reduced further 2: ",remainder)
                                denom_sol = int(denom_sol) / 2
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 3 == 0 and int(remainder) % 3 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 3
                                print("remainder reduced further 3: ",remainder)
                                denom_sol = int(denom_sol) / 3
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                        elif int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                            while int(denom_sol) % 5 == 0 and int(remainder) % 5 == 0 and int(remainder) != 0:
                                remainder = int(remainder) / 5
                                print("remainder reduced further 5: ",remainder)
                                denom_sol = int(denom_sol) / 5
                                self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ diff + "(" + str(remainder).replace(".0","") + "/" + str(denom_sol).replace(".0","") + ")",font_size = '15sp', size_hint_y= None, height=100))
                                self.layouts.append(layout)
                                
                elif int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 2")
                    while int(numer_sol_list[1]) % 2 == 0 and int(numer_sol_list[0]) % 2 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 2
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 2
                        print("numer_sol_list[1]",numer_sol_list[1])
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 3")
                    while int(numer_sol_list[1]) % 3 == 0 and int(numer_sol_list[0]) % 3 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 3
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 3
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                elif int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0 and int(numer_sol_list[1]) != int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                    print("Module 5")
                    while int(numer_sol_list[1]) % 5 == 0 and int(numer_sol_list[0]) % 5 == 0:
                        numer_sol_list[0] = int(numer_sol_list[0]) / 5
                        print("numer_sol_list[0]",numer_sol_list[0])
                        numer_sol_list[1] = int(numer_sol_list[1]) / 5
                        print("numer_sol_list[1]",numer_sol_list[1])

                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+ str(numer_sol_list[0]).replace(".0","") + "/" + str(numer_sol_list[1]).replace(".0","") ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                elif int(numer_sol_list[1]) == int(numer_sol_list[0]) and int(numer_sol_list[0]) != 0:
                   answer = str(int(numer_sol_list[1]) / int(numer_sol_list[0])).replace(".0","")
                   self.ids.list_of_steps.add_widget(Label(text="Reduces to: "+answer  ,font_size = '15sp', size_hint_y= None, height=100))
                   self.layouts.append(layout)  
                
                elif int(numer_sol_list[0]) == 0:
                    self.ids.list_of_steps.add_widget(Label(text="Reduces to: 0"  ,font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)    
                    
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = '15sp', size_hint_y= None, height=100))
            self.layouts.append(layout)




Builder.load_string("""
<Fractions_converter>
    id: Fractions_converter
    name:"Fractions_converter"
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
                text: "Fractions Converter"   
                font_size: '20sp'
                size_hint_y: None
                height: 200
                padding: 10, 10
                    
            BoxLayout:
                cols: 2
                padding:10
                spacing:10
                size_hint: 1, None
                width:300
                size_hint_y: None
                height: self.minimum_height 
                
                Button:
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    background_color: 0, 0 , 1 , 1
                    text: "Back"
                    on_release:
                        app.root.current = "Menu"
                        root.manager.transition.direction = "right" 
                        
                Button:
                    id: steps
                    text: "Clear All"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 1, 0 , 0 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets()  
                        Whole.text = ""
                        Numerator.text = ""
                        Denomenator.text = ""
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: Whole
                    text: Whole.text
                    hint_text: "Whole:"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(Whole.text)] 
            
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: Numerator
                    text: Numerator.text
                    hint_text: "Numerator"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(Numerator.text)] 
                    
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                
                TextInput:
                    id: Denomenator
                    text: Denomenator.text
                    hint_text: "Denomenator"
                    multiline: False
                    font_size: '35sp'
                    size_hint_y: None
                    height: 200
                    padding: 10
                    input_filter: lambda text, from_undo: text[:8 - len(Denomenator.text)] 
                    
            Label:
                size_hint_y: None
                height: 200
                text: "Convert To:"
                font_size: '20sp'
                
            BoxLayout:
                cols: 2
                id: steps
                size_hint_y: None
                height: self.minimum_height 
                padding: 5,5         
                         
                Button:
                    text: "Percent"   
                    font_size: '20sp'
                    size_hint_y: None
                    height: 200
                    padding: 10, 10
                    background_color: 0, 0 , 1 , 1
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions_converter.convert_frac_to_perc(Whole.text + "(" + Numerator.text + "/" + Denomenator.text + ")")
                        
                Button:
                    id: steps
                    text: "Decimal"   
                    font_size: '20sp'
                    size_hint_y: None
                    background_color: 0, 0 , 1 , 1
                    height: 200
                    padding: 10, 10
                    on_release:
                        list_of_steps.clear_widgets() 
                        Fractions_converter.convert_frac_to_dec(Whole.text + "(" + Numerator.text + "/" + Denomenator.text + ")")
                    
            GridLayout:
                id: list_of_steps
                cols: 1
                size_hint: 1, None
                height: self.minimum_height            
    
""")

class Fractions_converter(Screen):
    def __init__(self, **kwargs):
        super(Fractions_converter, self).__init__(**kwargs)
        
    layouts = []
    def convert_frac_to_perc(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            left_par_index = entry.find("(") 
            whole = entry[:left_par_index] 
            print("whole",whole)
            frac_sign = entry.find("/")
            numerator = entry[left_par_index+1:frac_sign]
            print("numerator",numerator)
            right_par_index = entry.find(")")
            denomenator = entry[frac_sign+1:right_par_index]
            print("denomenator",denomenator)
            if numerator[0] != "-" and denomenator[0] != "-":
                if numerator == "" and denomenator == "":
                    numerator = 1
                    denomenator = 1
                if int(numerator) < int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= str(numerator).replace(".0","") , font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(whole).replace(".0","") + " " + "---" * len(denomenator) + "  " * len(str(whole)), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator).replace(".0",""), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= " to Percentage = ", font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    last_digits = str(int(numerator) / int(denomenator))
                    print("last_digits",last_digits)
                    if str(whole) != "":
                        if str(whole)[0] != "-":
                            percentage = str((float(whole) + float(last_digits)) * 100) + "%"
                            print("percentage",percentage)
                            self.ids.list_of_steps.add_widget(Label(text= percentage, font_size = '20sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                        else:
                            percentage = str((float(whole) - float(last_digits)) * 100) + "%"
                            print("percentage",percentage)
                            self.ids.list_of_steps.add_widget(Label(text= percentage, font_size = '20sp', size_hint_y= None, height=100))
                            self.layouts.append(layout)
                    else:
                        percentage = str((float(last_digits)) * 100) + "%"
                        print("percentage",percentage)
                        self.ids.list_of_steps.add_widget(Label(text= percentage, font_size = '20sp', size_hint_y= None, height=100))
                        self.layouts.append(layout)
                    
                elif int(numerator) == int(denomenator) or str(numerator) == str(denomenator):
                    whole = str(int(whole) * 100) + "%"
                    print("whole",whole)
                    self.ids.list_of_steps.add_widget(Label(text= whole, font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                    self.ids.list_of_steps.add_widget(Label(text="Numerator exceeds Denomenator", font_size = '15sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
            else:
                self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
                self.layouts.append(layout)
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)
            
    def convert_frac_to_dec(self,entry):
        print("entry ",entry)
        layout = GridLayout(cols=1,size_hint_y= None)
        try:
            left_par_index = entry.find("(") 
            whole = entry[:left_par_index] 
            print("whole",whole)
            frac_sign = entry.find("/")
            numerator = entry[left_par_index+1:frac_sign]
            print("numerator",numerator)
            right_par_index = entry.find(")")
            denomenator = entry[frac_sign+1:right_par_index]
            print("denomenator",denomenator)
            
            if numerator[0] != "-" and denomenator[0] != "-":
                if int(numerator) < int(denomenator):
                    self.ids.list_of_steps.add_widget(Label(text= str(numerator), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(whole)+ " " + "---" * len(numerator) + "  " * len(str(whole)), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= str(denomenator), font_size = '20sp', size_hint_y= None, height=100))
                    self.ids.list_of_steps.add_widget(Label(text= " to Decimal = ", font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                    
                    last_digits = str(int(numerator) / int(denomenator))
                    print("last_digits",last_digits)
                    period = last_digits.find(".")
                    dec = last_digits[period+1:]
                    
                    decimal = str(whole) + "." + str(dec)
                    print("decimal",decimal)
                    if decimal.count(".") > 1:
                        index = decimal.find(".")
                        decimal = decimal[:index] + decimal[index+1:]
                    self.ids.list_of_steps.add_widget(Label(text= decimal, font_size = '20sp', size_hint_y= None, height=100))
                    self.layouts.append(layout)
                else:
                  self.ids.list_of_steps.add_widget(Label(text="Numerator exceeds Denomenator", font_size = '20sp', size_hint_y= None, height=100))
                  self.layouts.append(layout)      
            else:
                  self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
                  self.layouts.append(layout)  
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text="Invalid Input", font_size = '20sp', size_hint_y= None, height=100))
            self.layouts.append(layout)  

class Homepage(Screen):
    pass            

class Menu(Screen):
    pass

class updates(Screen):
    pass

sm = ScreenManager()
sm.add_widget(Homepage(name="Homepage"))
sm.add_widget(Menu(name="Menu"))   
sm.add_widget(updates(name="updates"))
sm.add_widget(Fractions(name="Fractions"))    
sm.add_widget(Fractions_converter(name="Fractions_converter"))
sm.current = "Homepage"   


class Fractions(App):
    def __init__(self, **kwargs):
        super(Fractions, self).__init__(**kwargs)
        Window.bind(on_keyboard=self._key_handler)
    
    def _key_handler(self, instance, key, *args):
        print("key:",key)
        if key == 27:
            sm.current = sm.current
            return True
    
    def build(app):
        return sm

if __name__ == '__main__':
    Fractions().run()
