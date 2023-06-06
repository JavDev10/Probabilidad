import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image  

#Crear ventana
ventana = tk.Tk()
ventana.title("Probabilidad Dados")
ventana.resizable(0,0)
ventana.geometry("800x600")

ico = Image.open(r"C:\Users\javi2\OneDrive\Escritorio\Programacion\Python\Probabilidad-main\dado_icon.png")
photo = ImageTk.PhotoImage(ico)
ventana.wm_iconphoto(False, photo)

#Cargar imagen
image1 = Image.open(r"C:\Users\javi2\OneDrive\Escritorio\Programacion\Python\Probabilidad-main\dado2.png")
dado = ImageTk.PhotoImage(image1)

#Ventana principal
ventana.configure()
frameMain = tk.Frame(ventana,bg="#2b2c30")
frameTitle = tk.Frame(ventana,bg="#2b2c30")
frameResult = tk.Frame(ventana,bg="#ddf0ff")
frameDado = tk.Frame(ventana, bg="#35566d")
frameBottom = tk.Frame(ventana,bg="#ddf0ff" )

frameTitle.pack(side="top",expand=False,fill="both")
frameBottom.pack(side="bottom",expand=False,fill="both",ipady=20)
frameMain.pack(side="left",expand=False,fill="both",ipadx=45)
frameDado.pack(side="left",expand=False,fill="both")
frameResult.pack(side="left",expand=True,fill="both")



#Estilos
styleLabelT = ttk.Style()
styleLabel1 = ttk.Style()
styleLabel2 = ttk.Style()
styleLabelT2 = ttk.Style()
styleLabel1.configure("T.TLabel", background="#2b2c30", foreground="white", font=("Segoe UI", 20, "italic"))
styleLabelT2.configure("T2.TLabel", background="#2b2c30", foreground="white", font=("Segoe UI", 15, "bold"))
styleLabel1.configure("L.TLabel", background="#2b2c30", foreground="white", font=("Segoe UI", 13, "normal"))
styleLabel2.configure("L2.TLabel", background="#35566d", foreground="white", font=("Segoe UI", 14, "italic"))

styleButton = ttk.Style()
styleButton.configure("B.TButton")

styleEntry = ttk.Style()
styleEntry.configure("E.TEntry",font=("Segoe UI", 16, "normal"))

#Labels
lbl_titulo = ttk.Label(frameTitle, text="Calcular probabilidad", style="T.TLabel")
lbl_titulo2 = ttk.Label(frameMain, text="Ingrese valores entre 1 y 6", style="T2.TLabel")
lbl_Evento1 = ttk.Label(frameMain, text="Evento 1:", style="L.TLabel")
lbl_Evento2 = ttk.Label(frameMain, text="Evento 2:", style="L.TLabel")
lbl_Evento3 = ttk.Label(frameMain, text="Evento 3:", style="L.TLabel")
lbl_Evento4 = ttk.Label(frameMain, text="Evento 4:", style="L.TLabel")
lbl_NumTiradas = ttk.Label(frameMain, text="Numero de lanzamientos:", style="T2.TLabel")
lbl_dado = ttk.Label(frameDado, text="Lanzar!", style="L2.TLabel")

#Entrys
entry_Evento1 = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")
entry_Evento2 = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")
entry_Evento3 = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")
entry_Evento4 = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")
entry_NumeroT = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")

#Buttons
foto1 = tk.Button(frameDado, image=dado, cursor="dot")
foto1.image = dado

#Mostrar en pantalla

#FrameTitulo------------------
lbl_titulo.pack(pady=5)
#FrameMain--------------------
lbl_titulo2.pack(pady=8)
lbl_Evento1.pack(pady=10)
entry_Evento1.pack(ipady=8)
lbl_Evento2.pack(pady=10) 
entry_Evento2.pack(ipady=8)
lbl_Evento3.pack(pady=10) 
entry_Evento3.pack(ipady=8)
lbl_Evento4.pack(pady=10)
entry_Evento4.pack(ipady=8)
lbl_NumTiradas.pack(pady=10)
entry_NumeroT.pack(ipady=8)
#FrameResultado---------------
#FrameDado--------------------
lbl_dado.pack(ipady=80)
foto1.pack()

#Variables
espacioMuestral = {1,2,3,4,5,6}
evento1 = 0
evento2 = 0
evento3 = 0
evento4 = 0
cantLanzamientos = 0




ventana.mainloop()