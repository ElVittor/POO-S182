from tkinter import messagebox
import sqlite3


class controladorBD:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/leon_/Documents/UPQ/5° Cuatri/PROGRMACIÓN OO/POO-S182/examen3p/BDImportaciones.db")
            print("Conectado a BD")
            return conexion
        except sqlite3.OperationalError:
            print("No se pudo Conectar")
            
    def guardar(self,mer,pai):
        conx=self.conexionBD()
        if(mer=="" or pai==""):
            messagebox.showwarning("Cuidado","Formulario incompleto")
            conx.close()
        else:
            cursor=conx.cursor()
            sqlinsert="insert into TB_Europa(Mercancia,Pais) values(?,?)"
            datos=(mer,pai)
            cursor.execute(sqlinsert,datos)
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario guardado")
            
    def consultar(self,pai):
        conx=self.conexionBD() #Para acceder a la funcion conexion
        if(pai==""):
                messagebox.showwarning("Cuidado","Escribe un Identificdor")
                conx.close()
        else:
            try:
                cursor=conx.cursor()
                sqlSelect="Select* from TB_Europa where pais = ?"
                pais=(pai)
                cursor.execute(sqlSelect,pais)
                RSusuario=cursor.fetchall()#result set o variable para guardar la información de la consulta, lo que tenga cursor lo pasamos a la variabale para seso sirve la funcion cursor.fetchall()
                conx.close()
                return RSusuario
            except sqlite3.OperationalError:
                print("Error de Consulta")

    def eliminar(self,id):
        pass
        conx=self.conexionBD()
        cursor=conx.cursor()
        sqldelete="DELETE FROM TB_Europa WHERE IDImpo= ? "
        
        if(id==""):
                messagebox.showwarning("Cuidado","Escribe un Identificdor")
                conx.close()
        else:
            try:
                datos=(id)
                cursor.execute(sqldelete,datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Correcto","Entrada Eliminada")
            except sqlite3.OperationalError:
                print("Error de eliminación")