import tkinter
import random
import string
import itertools
from tkinter import *
from tkinter import messagebox
class generator:
    def __init__(self,app):
        self.app=app
        self.no_of_characters=0
        self.no_of_sa=0
        self.no_of_ca=0
        self.no_of_spch=0
        self.no_of_digits=0
        
        self.e_no_of_characters=""
        self.e_no_of_sa=""
        self.e_no_of_ca=""
        self.e_no_of_spch=""
        self.e_no_of_digits=""

        self.frame3=Frame(self.app)#for generate button and output field
        self.frame3.grid(row='2',column='1')

        self.__generated_pass=StringVar()#used to dynamically change the output{avoids overlaps}
    def start(self):
        frame1=Frame(self.app)#for heading and instruction
        frame1.grid(row='0',column='1')
        heading=Label(frame1, text='Password Generator' ,font=('Edwardian Script ITC', '34', 'bold'),fg='dark blue')
        heading.grid(row='0',column='0')
        note=Label(frame1, text='The no. of characters will be generate with minimum given requirements' ,font=('Times New Roman', '13', 'bold'),fg='dark blue')
        note.grid(row='1',column='0')

        frame2=Frame(self.app)#for input labels and entry fields
        frame2.grid(row='1',column='1')
        l_no_of_characters=Label(frame2, text="Enter no of characters:",font=('Times New Roman', '15', 'bold italic'))
        l_no_of_characters.grid(row="0",column="0")
        self.e_no_of_characters=Entry(frame2)
        self.e_no_of_characters.grid(row="0",column="1")

        l_no_of_sa=Label(frame2, text="Enter no of small alphabets:",font=('Times New Roman', '15', 'bold italic'))
        l_no_of_sa.grid(row="1",column="0")
        self.e_no_of_sa=Entry(frame2)
        self.e_no_of_sa.grid(row="1",column="1")

        l_no_of_ca=Label(frame2, text="Enter no of capital alphabets:",font=('Times New Roman', '15', 'bold italic'))
        l_no_of_ca.grid(row="2",column="0")
        self.e_no_of_ca=Entry(frame2)
        self.e_no_of_ca.grid(row="2",column="1")

        l_no_of_spch=Label(frame2, text="Enter no of special characters:",font=('Times New Roman', '15', 'bold italic'))
        l_no_of_spch.grid(row="3",column="0")
        self.e_no_of_spch=Entry(frame2)
        self.e_no_of_spch.grid(row="3",column="1")

        l_no_of_digits=Label(frame2, text="Enter no of digits:",font=('Times New Roman', '15', 'bold italic'))
        l_no_of_digits.grid(row="4",column="0")
        self.e_no_of_digits=Entry(frame2)
        self.e_no_of_digits.grid(row="4",column="1")

        generate_button=Button(self.frame3,text="Generate",font=('Times New Roman', '18', 'bold italic'),bg="red",fg="white",command=self.get)#calls get
        generate_button.grid(row="0",column="0")
    def get(self):
        try:#getting input
            self.no_of_characters=int(self.e_no_of_characters.get())
            self.no_of_sa=int(self.e_no_of_sa.get())
            self.no_of_ca=int(self.e_no_of_ca.get())
            self.no_of_spch=int(self.e_no_of_spch.get())
            self.no_of_digits=int(self.e_no_of_digits.get())
            if(self.no_of_characters<(self.no_of_sa+self.no_of_ca+self.no_of_spch+self.no_of_digits)):#if no of characters is < sum of all other inputs
               raise  (ArithmeticError)
            self.genpass()#calling generation of password
        except ArithmeticError:
            messagebox.showinfo("WARNING",'Total Characters is less than that of the parameters')
        except ValueError:#incase any field is empty
            messagebox.showinfo("WARNING",'SOMETHING IS NOT RIGHT')
    def genpass(self):
        temp=""
        for i in range(self.no_of_digits):#choosing and adding digits
            temp=temp+str(random.randint(0,9))
        for i in range(self.no_of_sa):#choosing and adding lowercase
            temp=temp+str(random.choice(string.ascii_lowercase))
        for i in range(self.no_of_ca):#choosing and adding uppercase
            temp=temp+str(random.choice(string.ascii_uppercase))
        for i in range(self.no_of_spch):#choosing and adding special character
            temp=temp+str(random.choice(string.punctuation))
        while(len(temp)<self.no_of_characters):#if total length is not satisfied as the total no of characters
            ch=random.randint(0,3)#choose any one set and among them randomly choose one and add it to the password
            if(ch==0):
                temp=temp+str(random.choice(string.ascii_lowercase))
            elif(ch==1):
                temp=temp+str(random.choice(string.ascii_uppercase))
            elif(ch==2):
                temp=temp+str(random.choice(string.punctuation))
            else:
                temp=temp+str(random.randint(0,9))
        temp="".join(random.choice(list(itertools.permutations(temp))))#Compute all Permutations of the string ->Choose any one->generate the string by making list into one string
        self.__generated_pass=StringVar()
        self.__generated_pass.set(temp)#setting the output to stringvar
        frame4=Frame(self.app)
        frame4.grid(row='3',column='1')
        pass_p_label=Label(frame4,text="Generated Password:",font=('Times New Roman', '14', 'bold italic'))
        pass_p_label.grid(row="1",column="0")
        pass_label=Entry(frame4,textvariable=self.__generated_pass,font=('Times New Roman', '14', 'bold'),state='readonly',relief=FLAT)#using entry to make it copiable
        pass_label.grid(row="1",column="1")#the textvariable(not text) is of type stringvar to change dynamically ensuring clean interface and no overlap
        

app=Tk()#creating base
app.title('Password Generator')
app.geometry('550x320')
app.resizable(width=FALSE,height=FALSE)
g=generator(app)
g.start()#starting everything
app.mainloop()#to avoid immediate closing
