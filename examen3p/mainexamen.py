from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladoresBD import *
controlador=controladorBD()



def ejecutainsert():
   controlador.guardar(varmer.get(),varpai.get())
    

def ejecutaSelectPais():
    
    RSConUsu=controlador.consultar(varpaib.get())
    tabla.delete(*tabla.get_children())
    for usu in RSConUsu:
        tabla.insert("","end",text=usu[0],values=(usu[1],usu[2],usu[3]))
            

def ejecutaeliminar():
    RespElimYN=messagebox.askyesno("Eliminar",message=f"Desea eliminar el Usuario\nID: {varID.get()}")
    if(RespElimYN==True):
        controlador.eliminar(varID.get())
    

ventana=Tk()
ventana.title("Importaciones de Europa")
ventana.geometry("500x300")

panel=ttk.Notebook(ventana)
panel.pack(fill="both",expand="yes")

pestaña1=ttk.Frame(panel)
pestaña2=ttk.Frame(panel)
pestaña3=ttk.Frame(panel)

itulo=Label(pestaña1,text="Registro Importaciones",fg="Black",font=("Arial",12)).pack()

varmer=tk.StringVar()
lblmer=Label(pestaña1,text="Nombre de la Mercancia: ").pack()
txtmer=Entry(pestaña1,textvariable=varmer).pack()

varpai=tk.StringVar()
lblpai=Label(pestaña1,text="Pais de procedencia: ").pack()
txtpai=Entry(pestaña1,textvariable=varpai).pack()

btnGuardar=Button(pestaña1,text="Guardar Importación",command=ejecutainsert).pack()




varbususu=tk.StringVar
varpaib=tk.StringVar()
lblpai=Label(pestaña2,text="Pais de procedencia: ").pack()
txtpai=Entry(pestaña2,textvariable=varpaib).pack()
btnbususu=Button(pestaña2,text="Consultar Por pais",command=ejecutaSelectPais).pack()

subus=Label(pestaña2,text="Pais",fg="Blue",font=("Modern",15)).pack()
tabla=ttk.Treeview(pestaña2)
tabla["columns"]=("Mercancia","Pais")
tabla.column("#0",width=60,minwidth=60)
tabla.column("Mercancia",width=100,minwidth=100)
tabla.column("Pais",width=200,minwidth=200)
tabla.heading("#0",text="ID",anchor=tk.CENTER)
tabla.heading("Mercancia",text="Mercancia",anchor=tk.CENTER)
tabla.heading("Pais",text="Pais",anchor=tk.CENTER)
tabla.pack()

#Eliminar
varID=tk.StringVar()
titulo=Label(pestaña3,text="Eliminar Importación",fg="red",font=("arial",12)).pack()
lbID2=Label(pestaña3,text="ID de la entrada a Eliminar: ").pack()
txtID2=Entry(pestaña3,textvariable=varID).pack()
btnEliminar=Button(pestaña3,text="Eliminar Importación",command=ejecutaeliminar).pack()


#Paso 3
panel.add(pestaña1,text="Agregar importación")
panel.add(pestaña2,text="Buscar Importación")
panel.add(pestaña3,text="Eliminar Importacion")


ventana.mainloop()
