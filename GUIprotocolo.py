import tkinter as tk
from tkinter import ttk
import textwrap
from tkinter import messagebox
class ProtocoloTransmision(tk.Tk):
    
    def __init__(self):
        super().__init__()
        self.nframe=0
        self.contador = 1
        self.permiso = 0
        self.frames = []
        self.mensaje_final = ''

        self.title("Protocolo de Transmisión de datos")
        self.geometry("1300x350")

        # Transmisor
        tk.Label(self, text="TRANSMISOR").grid(row=0, column=0, columnspan=4)
        tk.Label(self, text="MENSAJE A TRANSMITIR:").grid(row=1, column=0)
        self.mensaje_entry = tk.Entry(self)
        self.mensaje_entry.grid(row=1, column=1)
        
        tk.Label(self, text="NÚMERO DE FRAMES:").grid(row=1, column=2)
        self.frames_entry = tk.Entry(self)
        self.frames_entry.grid(row=1, column=3)
        
        tk.Label(self, text="INDICADOR").grid(row=3, column=4)
        tk.Label(self, text="PPT").grid(row=3, column=5)
        tk.Label(self, text="PT").grid(row=3, column=6)
        tk.Label(self, text="DE").grid(row=3, column=7)
        tk.Label(self, text="DR").grid(row=3, column=8)
        tk.Label(self, text="NUM").grid(row=3, column=9)
        tk.Label(self, text="INFORMACIÓN").grid(row=3, column=10)
        
        self.indicador_trans = tk.Entry(self)
        self.indicador_trans.grid(row=4, column=4)
        self.ppt_trans = tk.Entry(self, width=4)
        self.ppt_trans.grid(row=4, column=5)
        self.ppt_trans.insert(0,'0')
        self.pt_trans = tk.Entry(self, width=4)
        self.pt_trans.grid(row=4, column=6)
        self.pt_trans.insert(0,'0')
        self.de_trans = tk.Entry(self, width=4)
        self.de_trans.grid(row=4, column=7)
        self.de_trans.insert(0,'0')
        self.dr_trans = tk.Entry(self, width=4)
        self.dr_trans.grid(row=4, column=8)
        self.dr_trans.insert(0,'0')
        self.num_trans = tk.Entry(self, width=4)
        self.num_trans.grid(row=4, column=9)
        self.info_trans = tk.Entry(self, width=13)
        self.info_trans.grid(row=4, column=10, columnspan=2)
        
        self.enviar_button = tk.Button(self, text="ENVIAR", command=self.enviar)
        self.enviar_button.grid(row=4, column=12)
        
        self.radio_ppt_vartr = tk.IntVar()
        self.radio_ppttr = tk.Checkbutton(self,variable=self.radio_ppt_vartr, onvalue=1, offvalue=0, command=lambda: self.update_entry(self.radio_ppt_vartr,self.ppt_trans))
        self.radio_ppttr.grid(row=5, column=5)
        self.radio_pt_vartr = tk.IntVar()
        self.radio_pttr = tk.Checkbutton(self,variable=self.radio_pt_vartr, onvalue=1, offvalue=0, command=lambda: self.update_entry(self.radio_pt_vartr,self.pt_trans))
        self.radio_pttr.grid(row=5, column=6)
        self.radio_de_vartr = tk.IntVar()
        self.radio_detr = tk.Checkbutton(self,variable=self.radio_de_vartr, onvalue=1, offvalue=0, command=lambda: self.update_entry(self.radio_de_vartr,self.de_trans))
        self.radio_detr.grid(row=5, column=7)
        self.radio_dr_vartr = tk.IntVar()
        self.radio_drtr = tk.Checkbutton(self,variable=self.radio_dr_vartr, onvalue=1, offvalue=0, command=lambda: self.update_entry(self.radio_dr_vartr,self.dr_trans))
        self.radio_drtr.grid(row=5, column=8)


        self.semantica_label = tk.Label(self, text="SEMÁNTICA: TRAMA DE DATOS")
        self.semantica_label.grid(row=5, column=0, columnspan=4)
        
        # Receptor
        tk.Label(self, text="RECEPTOR").grid(row=6, column=0)
        
        tk.Label(self, text="TRAMA RECIBIDA:").grid(row=7, column=0)
        self.header_rec = tk.Entry(self)
        self.header_rec.grid(row=7, column=1)
        self.info_rec = tk.Entry(self)
        self.info_rec.grid(row=7, column=2)
        self.trailer_rec = tk.Entry(self)
        self.trailer_rec.grid(row=7, column=3)
        
        tk.Label(self, text="HEADER").grid(row=8, column=1)
        tk.Label(self, text="INFORMACIÓN").grid(row=8, column=2)
        tk.Label(self, text="TRAILER").grid(row=8, column=3)
        
        tk.Label(self, text="RESPUESTA:").grid(row=10, column=3)
        tk.Label(self, text="INDICADOR").grid(row=9, column=4)
        tk.Label(self, text="PPT").grid(row=9, column=5)
        tk.Label(self, text="PT").grid(row=9, column=6)
        tk.Label(self, text="DE").grid(row=9, column=7)
        tk.Label(self, text="DR").grid(row=9, column=8)
        tk.Label(self, text="NUM").grid(row=9, column=9)
        tk.Label(self, text="INFORMACIÓN").grid(row=9, column=10)
        
        self.indicador_resp = tk.Entry(self)
        self.indicador_resp.grid(row=10, column=4)
        self.ppt_resp = tk.Entry(self, width=5)
        self.ppt_resp.grid(row=10, column=5)
        self.ppt_resp.insert(0,'0')
        self.pt_resp = tk.Entry(self, width=5)
        self.pt_resp.grid(row=10, column=6)
        self.pt_resp.insert(0,'0')
        self.de_resp = tk.Entry(self, width=5)
        self.de_resp.grid(row=10, column=7)
        self.de_resp.insert(0,'0')
        self.dr_resp = tk.Entry(self, width=5)
        self.dr_resp.grid(row=10, column=8)
        self.dr_resp.insert(0,'0')
        self.num_resp = tk.Entry(self, width=5)
        self.num_resp.grid(row=10, column=9)
        self.info_resp = tk.Entry(self, width=13)
        self.info_resp.grid(row=10, column=10,columnspan=2)
        
        self.responder_button = tk.Button(self, text="RESPONDER", command=self.responder)
        self.responder_button.grid(row=10, column=12)

        self.radio_ppt_varres = tk.IntVar()
        self.radio_pptres = tk.Checkbutton(self,variable=self.radio_ppt_varres, onvalue=1, offvalue=0, command=lambda: self.update_entry(self.radio_ppt_varres,self.ppt_resp))
        self.radio_pptres.grid(row=11, column=5)
        self.radio_pt_varres = tk.IntVar()
        self.radio_ptres = tk.Checkbutton(self,variable=self.radio_pt_varres, onvalue=1, offvalue=0, command=lambda: self.update_entry(self.radio_pt_varres,self.pt_resp))
        self.radio_ptres.grid(row=11, column=6)
        self.radio_de_varres = tk.IntVar()
        self.radio_deres = tk.Checkbutton(self,variable=self.radio_de_varres, onvalue=1, offvalue=0, command=lambda: self.update_entry(self.radio_de_varres,self.de_resp))
        self.radio_deres.grid(row=11, column=7)
        self.radio_dr_varres = tk.IntVar()
        self.radio_drres = tk.Checkbutton(self,variable=self.radio_dr_varres, onvalue=1, offvalue=0, command=lambda: self.update_entry(self.radio_dr_varres,self.dr_resp))
        self.radio_drres.grid(row=11, column=8)

        self.semantica_resp_label = tk.Label(self, text="SEMÁNTICA: TRAMA DE CONTROL, TRAMA RECIBIDA CON ÉXITO")
        self.semantica_resp_label.grid(row=12, column=0, columnspan=4)
        
        tk.Label(self, text="MENSAJE RECIBIDO:").grid(row=13, column=0)
        self.mensaje_recibido = tk.Entry(self)
        self.mensaje_recibido.grid(row=13, column=1)
        
        # Secuencia de Tramas
        tk.Label(self, text="SECUENCIA DE TRAMAS:").grid(row=0, column=13)
        self.secuencia_tramas = tk.Listbox(self, width=50)
        self.secuencia_tramas.grid(row=1, column=13, rowspan=14)
        
    def enviar(self):
        n_frames = self.frames_entry.get()
        self.frames = self.dividir_string_por_longitud(self.mensaje_entry.get(),int(n_frames))
        if self.radio_ppt_vartr.get() == 1 and self.radio_pt_vartr.get() == 0 and self.radio_dr_vartr.get() == 0 and self.radio_de_vartr.get() == 0:
            self.secuencia_tramas.insert(tk.END, f"Trama " + str(self.contador) + " (Tx): Control, Permiso para transmitir.")
            self.contador += 1
            self.ppt_trans.delete(0, tk.END)
            self.ppt_trans.insert(0,'0')
            self.radio_ppt_vartr.set(0)
            self.num_resp.insert(0, self.frames_entry.get())
            self.num_trans.insert(0, self.frames_entry.get())
        elif self.radio_de_vartr.get() == 1 and self.radio_pt_vartr.get() == 0 and self.radio_dr_vartr.get() == 0 and self.radio_ppt_vartr.get() == 0 and self.permiso == 1:
            self.secuencia_tramas.insert(tk.END, f"Trama " + str(self.contador) + " (Tx): Datos, Trama 1.")
            self.contador += 1
        else:
            messagebox.showinfo("Alerta", "Está incumpliendo las reglas de transmisión")
            
    def responder(self):
        if self.radio_pt_varres.get()==1 and self.radio_ppt_varres.get() == 0 and self.radio_de_varres.get() == 0 and self.radio_dr_varres.get() == 0 and self.contador==2:
            self.secuencia_tramas.insert(tk.END, f"Trama " + str(self.contador) + " (Rx): Control, Permiso concedido para transmitir.")
            self.info_trans.insert(0, self.frames[self.nframe])
            self.permiso = 1
            self.contador += 1
            self.nframe += 1
            self.pt_resp.delete(0, tk.END)
            self.pt_resp.insert(0,'0')
            self.radio_pt_varres.set(0)
        elif self.radio_pt_varres.get()==0 and self.radio_ppt_varres.get() == 0 and self.radio_de_varres.get() == 0 and self.radio_dr_varres.get() == 1 and self.contador > 3:
            if self.nframe < int(self.frames_entry.get()):
                self.mensaje_final += self.info_trans.get()
                self.info_trans.delete(0, tk.END)
                self.info_trans.insert(0, self.frames[self.nframe])
                self.nframe += 1
            else:
                self.mensaje_final += self.info_trans.get()
                self.mensaje_recibido.insert(0, self.mensaje_final)
        elif self.radio_pt_varres.get()==0 and self.radio_ppt_varres.get() == 0 and self.radio_de_varres.get() == 0 and self.radio_dr_varres.get() == 0 and self.contador > 3:
            if self.nframe < int(self.frames_entry.get()):
                self.info_trans.delete(0, tk.END)
                self.info_trans.insert(0, self.frames[self.nframe])
                self.nframe += 1
            else:
                self.mensaje_recibido.insert(0, self.mensaje_final)

    def update_entry(self, intvar, entry):
        # Actualizar el valor del Entry según el estado del Checkbutton
        if intvar.get() == 1:
            entry.delete(0, tk.END)  # Limpiar el Entry antes de insertar el nuevo valor
            entry.insert(0, '1')
        else:
            entry.delete(0, tk.END)  # Limpiar el Entry antes de insertar el nuevo valor
            entry.insert(0, '0')

    def dividir_string_por_longitud(self, s, n):
        longitud = len(s)
        partes = []

        # Calcular el tamaño base de cada parte
        base_size = longitud // n
        remainder = longitud % n

        start = 0
        for i in range(n):
            # Si hay un residuo, añadir 1 al tamaño de la parte actual
            if i < remainder:
                part_size = base_size + 1
            else:
                part_size = base_size
        
            end = start + part_size
            partes.append(s[start:end])
            start = end
    
        return partes

