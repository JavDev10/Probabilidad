import tkinter as tk, random
from tkinter import ttk , messagebox as MessageBox
from PIL import ImageTk, Image

#Crear ventana
ventana = tk.Tk()
ventana.title("Probabilidad Dados")
ventana.resizable(0,0)
ventana.geometry("840x620")
#Ventana principal
ventana.configure()
frameMain = tk.Frame(ventana,bg="#2b2c30")
frameTitle = tk.Frame(ventana,bg="#2b2c30")
frameResult = tk.Frame(ventana,bg="#ddf0ff")
frameDado = tk.Frame(ventana, bg="#35566d")
frameBottom = tk.Frame(ventana,bg="#ddf0ff" )

frameTitle.pack(side="top",expand=False,fill="both")
frameBottom.pack(side="bottom",expand=False,fill="both",ipady=20)
frameMain.pack(side="left",expand=False,fill="both",ipadx=50)
frameDado.pack(side="left",expand=False,fill="both")
frameResult.pack(side="left",expand=True,fill="both")

#icono
ico = Image.open(r"C:\Users\javi2\OneDrive\Escritorio\Programacion\Python\Probabilidad-main\dado_icon.ico")
photo = ImageTk.PhotoImage(ico)
ventana.wm_iconphoto(False, photo)

#Cargar imagen
image1 = Image.open(r"C:\Users\javi2\OneDrive\Escritorio\Programacion\Python\Probabilidad-main\dado2.png")
dado = ImageTk.PhotoImage(image1)

#Entrys
entry_Evento1 = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")
entry_Evento2 = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")
entry_Evento3 = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")
entry_Evento4 = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")
entry_NumeroT = ttk.Entry(frameMain,width=8,justify="center",style="E.TEntry")

#Estilos
styleLabelT = ttk.Style()
styleLabelT2 = ttk.Style()
styleLabelT3 = ttk.Style()
styleLabel1 = ttk.Style()
styleLabel2 = ttk.Style()
styleLabel3 = ttk.Style()
styleLabelR = ttk.Style()

styleLabelT.configure("T.TLabel", background="#2b2c30", foreground="white", font=("Consolas", 20, "bold"))
styleLabelT2.configure("T2.TLabel", background="#2b2c30", foreground="white", font=("Consolas", 14, "bold"))
styleLabelT3.configure("T3.TLabel", background="#ddf0ff", foreground="#2b2c30", font=("Consolas", 18, "bold"))
styleLabel1.configure("L.TLabel", background="#2b2c30", foreground="white", font=("Consolas", 13, "normal"))
styleLabel2.configure("L2.TLabel", background="#35566d", foreground="white", font=("Consolas", 16, "italic"))
styleLabel3.configure("L3.TLabel", background="#ddf0ff", foreground="#2b2c30", font=("Consolas", 15, "normal"))
styleLabelR.configure("R.TLabel", background="#ddf0ff", foreground="#35566d", font=("Consolas", 32, "bold"))

styleButton = ttk.Style()
styleButton.configure("B.TButton")

styleEntry = ttk.Style()
styleEntry.configure("E.TEntry",font=("Segoe UI", 16, "normal"))

#Labels
#Titulo
lbl_titulo = ttk.Label(frameTitle, text="Calcular probabilidad", style="T.TLabel")
#Eventos
lbl_titulo2 = ttk.Label(frameMain, text="Ingrese valores entre 1 y 6", style="T2.TLabel")
lbl_Evento1 = ttk.Label(frameMain, text="Evento 1:", style="L.TLabel")
lbl_Evento2 = ttk.Label(frameMain, text="Evento 2:", style="L.TLabel")
lbl_Evento3 = ttk.Label(frameMain, text="Evento 3:", style="L.TLabel")
lbl_Evento4 = ttk.Label(frameMain, text="Evento 4:", style="L.TLabel")
lbl_NumTiradas = ttk.Label(frameMain, text="Numero de lanzamientos:", style="T2.TLabel")
#Resultado
lbl_tituloResult = ttk.Label(frameResult, text="Resultados", style="T3.TLabel")
lbl_result1 = ttk.Label(frameResult, text="Evento 1", style="L3.TLabel")
lbl_result1_P = ttk.Label(frameResult, text="0%", style="R.TLabel")
lbl_result2 = ttk.Label(frameResult, text="Evento 2", style="L3.TLabel")
lbl_result2_P = ttk.Label(frameResult, text="0%", style="R.TLabel")
lbl_result3 = ttk.Label(frameResult, text="Evento 3", style="L3.TLabel")
lbl_result3_P = ttk.Label(frameResult, text="0%", style="R.TLabel")
lbl_result4 = ttk.Label(frameResult, text="Evento 4", style="L3.TLabel")
lbl_result4_P = ttk.Label(frameResult, text="0%", style="R.TLabel")
#Dado
lbl_dado = ttk.Label(frameDado, text="Lanzar!", style="L2.TLabel")

#Variables
evento1 = tk.IntVar()
evento2 = tk.IntVar()
evento3 = tk.IntVar()
evento4 = tk.IntVar()
cantLanzamientos = tk.IntVar()
resulLanzamientos = []
espacio_muestral = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

def MessageBoxError1():
    MessageBox.showwarning("ERROR", "Ingresa el número de lanzamientos")

def Cal_Lanzamiento():
    cantLanzamientos.set(entry_NumeroT.get())
    resulLanzamientos.clear()

    for i in range(cantLanzamientos.get()):
            resulLanzamientos.append(random.randint(1,6))

    for element in resulLanzamientos:
        espacio_muestral[element] += 1
    AsignarEventos()

def AsignarEventos():
    evento1.set(entry_Evento1.get())
    evento2.set(entry_Evento2.get())
    evento3.set(entry_Evento3.get())
    evento4.set(entry_Evento4.get())

    for e in espacio_muestral:
        if e == evento1.get():
            value1 = round(int(espacio_muestral[e]) / cantLanzamientos.get(),2) * 100
            lbl_result1_P.configure(text=str(value1)+"%")
        elif e == evento2.get():  
            value2 = round(int(espacio_muestral[e]) / cantLanzamientos.get(),2) * 100
            lbl_result2_P.configure(text=str(value2)+"%")
        elif e == evento3.get(): 
            value3 = round(int(espacio_muestral[e]) / cantLanzamientos.get(),2) * 100
            lbl_result3_P.configure(text=str(value3)+"%") 
        elif e == evento4.get():
            value4 = round(int(espacio_muestral[e]) / cantLanzamientos.get(),2) * 100
            lbl_result4_P.configure(text=str(value4)+"%") 
    
#Buttons
foto1 = tk.Button(frameDado, image=dado, cursor="dot", command= lambda: [Cal_Lanzamiento()])
foto1.image = dado

#Mostrar en pantalla
#FrameTitulo------------------
lbl_titulo.pack(pady=5)
#FrameMain--------------------
lbl_titulo2.pack(ipady=8)
lbl_Evento1.pack(pady=10)
entry_Evento1.pack(ipady=8)
lbl_Evento2.pack(pady=10) 
entry_Evento2.pack(ipady=8)
lbl_Evento3.pack(pady=10) 
entry_Evento3.pack(ipady=8)
lbl_Evento4.pack(pady=10)
entry_Evento4.pack(ipady=8)
lbl_NumTiradas.pack(pady=10,ipady=10)
entry_NumeroT.pack(ipady=8)
#FrameResultado---------------
lbl_tituloResult.pack(pady=10)
lbl_result1.pack(pady=10)
lbl_result1_P.pack()
lbl_result2.pack(pady=10)
lbl_result2_P.pack()
lbl_result3.pack(pady=10)
lbl_result3_P.pack()
lbl_result4.pack(pady=10)
lbl_result4_P.pack()
#FrameDado--------------------
lbl_dado.pack(ipady=80)
foto1.pack()
    
ventana.mainloop()