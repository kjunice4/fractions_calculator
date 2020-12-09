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
            font_size: 75
            background_color: 0, 0 , 0 , 1
            size_hint_y: None
            height: 200
            text: "KSquared Fractions Solver"
            on_release:
                app.root.current = "Fractions"
                root.manager.transition.direction = "left" 

""")


#EXPONENTS STEPS
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
                text: "Fractions Solver"
                    
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
                font_size: 75
                size_hint_y: None
                height: 200
                padding: 10, 10
                text: "Numerator / Denomenator"       
                   
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
                denom_lcm = str(np.lcm(int(denom_a),int(denom_b)))
                print("denom_lcm",denom_lcm)
                self.ids.list_of_steps.add_widget(Label(text= "Add " + entry_list[0] + " + " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + denom_lcm ,font_size = 60, size_hint_y= None, height=100))
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
                self.ids.list_of_steps.add_widget(Label(text= "(" + str(int(denom_lcm) / int(denom_a)).replace(".0","") + ")" + numer_a + "/" + denom_a + "(" + str(int(denom_lcm) / int(denom_a)).replace(".0","") + ")" + " + " + "(" + str(int(denom_lcm) / int(denom_b)).replace(".0","") + ")" + numer_b + "/" + denom_b + "(" + str(int(denom_lcm) / int(denom_b)).replace(".0","") + ")"  + " = ",font_size = 60, size_hint_y= None, height=100))
                numer_a = str(int(denom_lcm) / int(denom_a) * int(numer_a)).replace(".0","")
                print("numer_a:",numer_a)
                numer_b = str(int(denom_lcm) / int(denom_b) * int(numer_b)).replace(".0","")
                print("numer_b:",numer_b)
                numer_sol = str(int(numer_a) + int(numer_b)).replace(".0","") + "/" + str(denom_lcm)
                print("numer_sol:",numer_sol)
                self.ids.list_of_steps.add_widget(Label(text= numer_a + "/" + denom_lcm + " + " + numer_b + "/" + denom_lcm + " = ",font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= numer_sol ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)  
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
        except Exception:
            self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
            self.layouts.append(layout)

    def sub(self,entry):
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
                denom_lcm = str(np.lcm(int(denom_a),int(denom_b)))
                print("denom_lcm",denom_lcm)
                self.ids.list_of_steps.add_widget(Label(text= "Subtract " + entry_list[0] + " - " + entry_list[1] ,font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= "Least Common Multiple = " + denom_lcm ,font_size = 60, size_hint_y= None, height=100))
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
                self.ids.list_of_steps.add_widget(Label(text= "(" + str(int(denom_lcm) / int(denom_a)).replace(".0","") + ")" + numer_a + "/" + denom_a + "(" + str(int(denom_lcm) / int(denom_a)).replace(".0","") + ")" + " - " + "(" + str(int(denom_lcm) / int(denom_b)).replace(".0","") + ")" + numer_b + "/" + denom_b + "(" + str(int(denom_lcm) / int(denom_b)).replace(".0","") + ")"  + " = ",font_size = 60, size_hint_y= None, height=100))
                numer_a = str(int(denom_lcm) / int(denom_a) * int(numer_a)).replace(".0","")
                print("numer_a:",numer_a)
                numer_b = str(int(denom_lcm) / int(denom_b) * int(numer_b)).replace(".0","")
                print("numer_b:",numer_b)
                numer_sol = str(int(numer_a) - int(numer_b)).replace(".0","") + "/" + str(denom_lcm)
                print("numer_sol:",numer_sol)
                self.ids.list_of_steps.add_widget(Label(text= numer_a + "/" + denom_lcm + " - " + numer_b + "/" + denom_lcm + " = ",font_size = 60, size_hint_y= None, height=100))
                self.ids.list_of_steps.add_widget(Label(text= numer_sol ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)  
            else:
                self.ids.list_of_steps.add_widget(Label(text= "Invalid Input" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)
                
                
                self.ids.list_of_steps.add_widget(Label(text= "s" ,font_size = 60, size_hint_y= None, height=100))
                self.layouts.append(layout)    
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
                
                
                self.ids.list_of_steps.add_widget(Label(text= "m" ,font_size = 60, size_hint_y= None, height=100))
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
    

