# -*- coding: utf-8 -*-
from IPython.display import display,Markdown,HTML #, Math , Latex
import Tkinter
def get_doc(data):
    """Формує рядок довідки з даних data"""
    res=[]
    for i,row in enumerate(data): # для кожного об'єкта списка data
        res.append(str(i)+" - "+row[0])
    return "\n".join(res)

db=[] # список бази даних

############################################################################
class DB:
    """Основний час для точіння, розточування, свердління  
$T_o = \\frac{l}{{n}{s}}$  
де  
*l* - довжина робочого ходу  
*n* - частота обертів  
*s* - подача""" # новий рядок в Markdown - два пробіли вкінці рядка
    @classmethod
    def doc(cls):
        return Markdown(cls.__doc__.decode("utf-8"))
    def __init__(self, l=None, n=None, s=None):
        self.l=l
        self.n=n
        self.s=s
    def time(self): # функція розраховує час
        return self.l/(self.n*self.s)
       
db.append(DB) # додати об'єкт у базу даних

############################################################################
class DB:
    """Час на установку і зняття заготовки в самоцентруючому патроні  
m - маса  
k - тип (список типів: get_doc(db[i].data)):  
"""
    data=[
    ("Самоцентруюючий патрон, кріплення ключем",{0.5:0.15, 1:0.17, 3:0.23, 5:0.12}),
    ("Самоцентруюючий патрон, пневмозатиск",{0.5:0.07, 1:0.08, 3:0.1, 5:0.27})]
    @classmethod
    def doc(cls):
        n=cls.__doc__ +"  \n"
        d=""
        for r in cls.data:
            c="<td>%s</td>"%r[0]
            for k in sorted(r[1].keys()):
                c+="<td>m=%s t=%s</td>"%(k,r[1][k])
            d+="<tr>%s</tr>"%c
        d="<table>%s</table>"%d
        return display(Markdown(n.decode("utf-8")),HTML(d.decode("utf-8")))
        # в даному випадку допустимо просто return Markdown(d.decode("utf-8"))
        # оскільки Markdown дозволяє включення тегів html    
    def __init__(self, k=None, m=None):
        self.k=k
        self.m=m
    def time(self):
        row=self.data[self.k][1]
        keys=sorted(row.keys())
        keys2=[x for x in keys if x<=self.m]
        if keys2: key=keys2[-1]
        else: key=keys[0]
        return row[key]
    def gui(self):
        root=Tkinter.Tk()
        root.attributes("-topmost", True)
        self.list=Tkinter.Listbox(root)
        listData=[k[0] for k in self.data]
        for x in listData: #заповнити список
            self.list.insert(Tkinter.END,x)
        self.list.pack() 
        self.entry=Tkinter.Entry(root)
        self.entry.pack()
        btn=Tkinter.Button(root,text="Ok",command=self.gui_ok)
        btn.pack()
        self.root=root
        root.mainloop()
    def gui_ok(self):
        self.k=int(self.list.curselection()[0])
        self.m=float(self.entry.get())
        self.root.destroy()
        self.root.quit()

db.append(DB) # додати об'єкт у базу даних


############################################################################
# атрибут документації модуля
__doc__="Введіть db[i] та db[i].__doc___ для допомоги, де i:\n"
docList=[str(i)+" - "+x.__doc__.split("\n")[0] for i,x in enumerate(db)]
__doc__+="\n".join(docList)

if __name__=='__main__':
    # Приклади застосування:
    print __doc__
    print
    print db[0].__doc__
    print
    print db[0].doc()
    print
    t=db[0](100.0, 700.0, 0.1)
    print t.time()
    
    print db[1].__doc__
    print get_doc(db[1].data)
    # або
    #print repr(db[1].data).decode('string_escape')
    print
    print db[1].doc()
    print
    t=db[1](1, 5.0)
    print t.time()
    t.gui()
    print t.time()