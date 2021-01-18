from tkinter import *
from matplotlib import pyplot as plt
import numpy as np
from PIL import Image,ImageTk
object=Tk()
a=["carbohdrates","fat","protiens"]
w=0.2

def call():
    def parlie():
        plt.pie([73,23,3],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
            explode=[0.1,0,0],shadow="True",radius=1.0,labeldistance=1.1,
            textprops={"fontweight":"bold","fontsize":16},
            wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("PARLE-G"
                  "\nCALORIES:125" ,color="yellow")
        plt.legend()
        plt.show()
    def bparlie():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="forestgreen",)
        plt.bar(bar2,[73,23,3],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("PARLE-G")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()

    def nimkin():
        plt.pie([63,32,7],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
                explode=[0.1,0,0],shadow="True",radius=1.0,labeldistance=1.1,
                textprops={"fontweight":"bold","fontsize":16},
                wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("NIMKIN"
                  "\nCALORIES:63" ,color="yellow")
        plt.legend()
        plt.show()
    def bnimkin():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="forestgreen",)
        plt.bar(bar2,[62,32,7],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("NIMKIN")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()

    def milkshakti():
        plt.pie([67,28,3],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
                explode=[0.1,0,0],shadow="True",radius=1.0,labeldistance=1.1,
                textprops={"fontweight":"bold","fontsize":16},
                wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("MILK SHAKTI"
                  "\nCALORIES:266",color="yellow")
        plt.legend()
        plt.show()
    def bmilkshakti():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="forestgreen",)
        plt.bar(bar2,[67,28,5],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("MILK SHAKTI")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()

    def krackjack():
        plt.pie([55,40,4],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
                explode=[0.1,0,0],shadow="True",radius=1.0,labeldistance=1.1,
                textprops={"fontweight":"bold","fontsize":16},
                wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("KRACKJACK"
                  "\nCALORIES:270" ,color="yellow")
        plt.legend()
        plt.show()
    def bkrackjack():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="forestgreen",)
        plt.bar(bar2,[55,40,4],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("KRACKJACK")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()

    def cokies():
        plt.pie([58,10,5],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
                explode=[0.1,0,0],shadow="True",radius=1.0,labeldistance=1.1,
                textprops={"fontweight":"bold","fontsize":16},
                wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("20-20 COOKIES"
                  "\nCALORIES:245" ,color="yellow")
        plt.legend()
        plt.show()
    def bcokies():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="forestgreen",)
        plt.bar(bar2,[58,10,5],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("20-20 COOKIES")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()

    def happy():
        plt.pie([59,37,4],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
                explode=[0.1,0,0],shadow="True",radius=1.0,labeldistance=1.1,
                textprops={"fontweight":"bold","fontsize":16},
                wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("HAPPY HAPPY"
                  "\nCALORIES:489" ,color="chocolate")
        plt.legend()
        plt.show()
    def bhappy():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="forestgreen",)
        plt.bar(bar2,[5,37,4],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("HAPPY HAPPY")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()

    def monoco():
        plt.pie([57,49,4],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
                explode=[0.1,0,0],shadow="True",radius=1.0,labeldistance=1.1,
                textprops={"fontweight":"bold","fontsize":16},
                wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("MONOCO"
                  "\nCALORIES:124" ,color="yellow")
        plt.legend()
        plt.show()
    def bmonoco():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="forestgreen",)
        plt.bar(bar2,[57,49,4],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("MONOCO")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()

    def m():
        plt.pie([63,27,6],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
                explode=[0.1,0,0],shadow="True",radius=1.0,labeldistance=1.1,
                textprops={"fontweight":"bold","fontsize":16},
                wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("MILK BIKIES"
                  "\nCALORIES:130" ,color="brown")
        plt.legend()
        plt.show()
    def bm():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="forestgreen",)
        plt.bar(bar2,[63,27,6],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("MILK BIKIES")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()

    def o():
        plt.pie([64,38,0.1],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
                explode=[0,0,0.2],shadow="True",radius=1.0,labeldistance=1.1,
                textprops={"fontweight":"bold","fontsize":16},
                wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("OREO"
                  "\nCALORIES:55" ,color="brown")
        plt.legend()
        plt.show()
    def bo():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="forestgreen",)
        plt.bar(bar2,[64,38,0],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("OREO")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()

    def marie():
        plt.pie([70,24,5],labels=["cabohydrates","fat","protiens"],autopct="%0.0f%%",colors=["orange","brown","blue"],startangle=90,
                explode=[0.1,0,0],shadow="True",radius=1.0,labeldistance=1.1,
                textprops={"fontweight":"bold","fontsize":16},
                wedgeprops={"linewidth":3,"edgecolor":"white"})
        plt.title("MARIE GOLD"
                  "\nCALORIES:156" ,color="brown")
        plt.legend()
        plt.show()
    def bmarie():
        bar1=np.arange(len(a))
        bar2=[w+i for i in bar1]
        plt.bar(bar1,[60,28,12],w,label="LIMIT VALUE", color="green",)
        plt.bar(bar2,[70,24,5],w,label="CALORIES PER BUISCUTE",color="indianred")
        plt.title("MARIE GOLD")
        plt.xlabel("calories")
        plt.ylabel("limit")
        plt.xticks(bar1,a)
        plt.legend()
        plt.show()


    l1=Label(object,text="MARIE GOLD",bg="teal",font="bold",fg="white")
    l1.place(x=225,y=100)
    b2=Button(object, text="calories", bg="deepskyblue", fg="purple", activebackground="chocolate",
                activeforeground="red", command=marie)
    b2.place(x=252,y=128)
    b2=Button(object, text="comparision", bg="hotpink", fg="purple", activebackground="chocolate",
                activeforeground="red", command=bmarie)
    b2.place(x=240,y=156)


    l2=Label(object,text="PARLE-G",bg="teal",font="bold",fg="white")
    l2.place(x=235,y=190)
    b2=Button(object,text="calories",bg="deepskyblue",fg="purple",activebackground="chocolate",
             activeforeground="red",command=parlie)
    b2.place(x=252,y=216)
    b2=Button(object,text="comparision",bg="hotpink",fg="purple",activebackground="chocolate",
             activeforeground="red",command=bparlie)
    b2.place(x=240,y=244)

    l3=Label(object,text="NIMKIN",bg="teal",font="bold",fg="white")
    l3.place(x=249,y=280)
    b3=Button(object,text="calories",bg="deepskyblue",fg="purple",activebackground="chocolate",
             activeforeground="red",command=nimkin)
    b3.place(x=252,y=306)
    b3=Button(object,text="comparision",bg="hotpink",fg="purple",activebackground="chocolate",
             activeforeground="red",command=bnimkin)
    b3.place(x=240,y=332)

    l4=Label(object,text="MILK SHAKTI",bg="teal",font="bold",fg="white")
    l4.place(x=225,y=370)
    b4=Button(object,text="calories",bg="deepskyblue",fg="purple",activebackground="chocolate",
             activeforeground="red",command=milkshakti)
    b4.place(x=252,y=396)
    b4=Button(object,text="comparision",bg="hotpink",fg="purple",activebackground="chocolate",
             activeforeground="red",command=bmilkshakti)
    b4.place(x=240,y=421)

    l5=Label(object,text="KRACKJACK",bg="teal",font="bold",fg="white")
    l5.place(x=725,y=100)
    b5=Button(object,text="calories",bg="deepskyblue",fg="purple",activebackground="chocolate",
             activeforeground="red",command=krackjack)
    b5.place(x=752,y=128)
    b5=Button(object,text="comparision",bg="hotpink",fg="purple",activebackground="chocolate",
             activeforeground="red",command=bkrackjack)
    b5.place(x=740,y=156)

    l6=Label(object,text="20-20 COOKIES",bg="teal",font="bold",fg="white")
    l6.place(x=725,y=190)
    b6=Button(object,text="calories",bg="deepskyblue",fg="purple",activebackground="chocolate",
             activeforeground="red",command=cokies)
    b6.place(x=752,y=216)
    b6=Button(object,text="comparision",bg="hotpink",fg="purple",activebackground="chocolate",
             activeforeground="red",command=bcokies)
    b6.place(x=740,y=244)

    l7=Label(object,text="HAPPY HAPPY",bg="teal",font="bold",fg="white")
    l7.place(x=720,y=280)
    b7=Button(object,text="calories",bg="deepskyblue",fg="purple",activebackground="chocolate",
             activeforeground="red",command=happy)
    b7.place(x=752,y=306)
    b7=Button(object,text="comparision",bg="hotpink",fg="purple",activebackground="chocolate",
             activeforeground="red",command=bhappy)
    b7.place(x=740,y=332)

    l8=Label(object,text="MONOCO",bg="teal",font="bold",fg="white")
    l8.place(x=735,y=370)
    b8=Button(object,text="calories",bg="deepskyblue",fg="purple",activebackground="chocolate",
             activeforeground="red",command=monoco)
    b8.place(x=752,y=396)
    b8=Button(object,text="comparision",bg="hotpink",fg="purple",activebackground="chocolate",
             activeforeground="red",command=bmonoco)
    b8.place(x=740,y=421)

    l9=Label(object,text="MILK BIKIES",bg="teal",font="bold",fg="white")
    l9.place(x=488,y=300)
    b9=Button(object,text="calories",bg="deepskyblue",fg="purple",activebackground="chocolate",
             activeforeground="red",command=m)
    b9.place(x=510,y=326)
    b9=Button(object,text="comparision",bg="hotpink",fg="purple",activebackground="chocolate",
             activeforeground="red",command=bm)
    b9.place(x=498,y=352)

    l9 = Label(object, text="OREO", bg="teal", font="bold", fg="white")
    l9.place(x=510, y=150)
    b9 = Button(object, text="calories", bg="deepskyblue", fg="purple", activebackground="chocolate",
                activeforeground="red", command=o)
    b9.place(x=510, y=180)
    b9 = Button(object, text="comparision", bg="hotpink", fg="purple", activebackground="chocolate",
                activeforeground="red", command=bo)
    b9.place(x=498, y=208)
    ll1.destroy()

    m = ["MARIE", "PARLE-G", "NIMKIN", "MILKSHAKTI", "KRACKJACK", "20-20COOKIES", "HAPPYHAPPY", "MONOCO", "MILKBIKIES",
         "OREO"]
    n = [156, 125, 63, 266, 270, 245, 489, 124, 130, 64]
    def overall():
        plt.pie(n,labels=m,radius=1.0, shadow="true",
                colors=["orange", "brown", "blue","goldenrod","rosybrown",
                        "firebrick","aqua","orchid","khaki","darkorange"],
                autopct="%0i%%", startangle=45, labeldistance=1.1,
                textprops={"fontweight": "bold", "fontsize": 12},
                wedgeprops={"linewidth":3, "edgecolor":"gainsboro"})
        plt.title("CALORIES PRESENT IN THE BISCUITES")
        plt.show()
    bb2 = Button(object, text="OVERALL", bg="light blue",
                 fg="black", activebackground="chocolate",
                 activeforeground="yellow", command=overall)
    bb2.place(x=500, y=400)

    def pop():
        plt.bar(["MILKBIKIES"],[50],width=0.4,color="brown")
        plt.bar(["HAPPYHAPPY"],[20],width=0.4,color="blue")
        plt.bar(["MILKSHAKTHI"],[30],width=0.4,color="green")
        plt.xlabel("famous biscuites among children")
        plt.ylabel("percentage")
        plt.show()
    bb3 = Button(object, text="MOST LIKED BISCUITES", bg="light blue", fg="black",
                 activebackground="chocolate", command=pop)
    bb3.place(x=465, y=450)
    object.configure(background="aquamarine")


object.title("CALORIES OF FAMOUS THE BISCUITE PRODUCTS")
ll1=Label(object,text="CLICK THE BUTTON TO CHECK THE CALORIES OF THE FAMOUS BUISCUTE PRODUCTS",
          bg="teal", font="bold", fg="white")
ll1.place(x=250,y=25)
bb1=Button(object,text="COOKIES",bg="mediumturquoise",
           fg="black",activebackground="chocolate",
            activeforeground="blue",command=call)
bb1.place(x=505,y=80)
object.configure(background="khaki")
object.mainloop()
