import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.title("Probabilidad Dados")
ventana.resizable(0,0)
ventana.geometry("800x480")

#Ventana principal
ventana.configure()
frameMain = tk.Frame(ventana,bg="#2b2c30")
frameTitle = tk.Frame(ventana,bg="#2b2c30")
frameResult = tk.Frame(ventana,bg="#0a516d")
frameDado = tk.Frame(ventana, bg="#0a516d")
frameTitle.pack(side="top",expand=False,fill="both",ipady=20)
frameDado.pack(side="bottom",expand=False,fill="both",ipady=20)
frameMain.pack(side="left",expand=True,fill="both")
frameResult.pack(side="right",expand=True,fill="both")

#Estilos
styleLabelT = ttk.Style()
styleLabelT.configure("T.TLabel", background="#2b2c30", foreground="white", font=("Segoe UI", 13, "normal"))

#Labels
lbl_Evento1 = ttk.Label(frameMain, text="Evento 1:", style="T.TLabel")
lbl_Evento2 = ttk.Label(frameMain, text="Evento 2:", style="T.TLabel")
lbl_Evento3 = ttk.Label(frameMain, text="Evento 3:", style="T.TLabel")
lbl_Evento4 = ttk.Label(frameMain, text="Evento 4:", style="T.TLabel")

#Entrys
entry_Evento1 = ttk.Entry(frameMain)
entry_Evento2 = ttk.Entry(frameMain)
entry_Evento3 = ttk.Entry(frameMain)
entry_Evento4 = ttk.Entry(frameMain)

#Buttons
bttn_Calcular = ttk.Button(frameDado,text="CALCULAR")

#Mostrar en pantalla
lbl_Evento1.pack(pady=10)
entry_Evento1.pack()
lbl_Evento2.pack(pady=10) 
entry_Evento2.pack()
lbl_Evento3.pack(pady=10) 
entry_Evento3.pack()
lbl_Evento4.pack(pady=10)
entry_Evento4.pack()
bttn_Calcular.pack()

espacioMuestral = {1,2,3,4,5,6}
evento1 = 0
evento2 = 0
evento3 = 0
evento4 = 0

ventana.mainloop()