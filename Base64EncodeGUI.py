#!/usr/bin/env python3


import base64
import os
import sys
if sys.platform=="win32" or sys.platform=="win64":
	os.system("pip install pyfiglet")
	os.system("pip install tk")
	os.system("cls")
elif sys.platform=="linux":
	os.system("pip install pyfiglet")
	os.system("pip install tk")
	os.system("clear")
import pyfiglet
import tkinter
from tkinter import *


def Base64_Encode_Tool(created_by="ruben leonardo sigalingging"):
	Fungsi_Utama_Base64_Encode_Tool=tkinter.Tk()
	Fungsi_Utama_Base64_Encode_Tool.title("Base64 Encode Tool")
	Fungsi_Utama_Base64_Encode_Tool.geometry("800x500")
	Fungsi_Utama_Base64_Encode_Tool.configure(bg="#000000",cursor="spider")
	Fungsi_Utama_Base64_Encode_Tool.resizable(width=False,height=False)


	Judul_Base64_Encode=tkinter.Label(Fungsi_Utama_Base64_Encode_Tool,text="Base64 Encode Tool",anchor=tkinter.CENTER,bg="#008000",bd=2,cursor="pirate",font=("Ubuntu",35),fg="#ffffff",justify=tkinter.CENTER)
	Judul_Base64_Encode.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP)


	Tombol_Input_Text=tkinter.Entry(Fungsi_Utama_Base64_Encode_Tool,bg="#ffffff",bd=2,cursor="pirate",font=("Times New Roman",23),fg="#008000",justify=tkinter.CENTER,relief=tkinter.FLAT,selectbackground="#008000",selectforeground="#ffffff")
	Tombol_Input_Text.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,padx=25,pady=25)


	def Processor_Function(created_by="ruben leonardo sigalingging"):
		Get_Entry_Button=Tombol_Input_Text.get()
		Base64_Encodings=Get_Entry_Button.encode("ascii")
		Function_B64=base64.b64encode(Base64_Encodings)
		Base64_Code=Function_B64.decode("ascii")


		Label_Hasil=tkinter.Label(Fungsi_Utama_Base64_Encode_Tool,bg="#008000",fg="#ffffff",justify=tkinter.CENTER,font=("Ubuntu",23),cursor="pirate",anchor=tkinter.CENTER)
		Label_Hasil.configure(text="Base64 Code From \n"+Get_Entry_Button+str(" Is:\n"+Base64_Code))
		print(f"Base64 Code From {Get_Entry_Button} Is: {Base64_Code}\n")
		Label_Hasil.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,padx=5,pady=5)


	Tombol_Button_Base64_Encodings=tkinter.Button(Fungsi_Utama_Base64_Encode_Tool,text="Let's Encoding!",activebackground="#ffffff",activeforeground="#008000",bd=2,bg="#008000",fg="#ffffff",font=("Times New Roman",23),justify=tkinter.CENTER,command=Processor_Function)
	Tombol_Button_Base64_Encodings.pack(expand=False,fill=tkinter.BOTH,side=tkinter.TOP,padx=25,pady=25)
	Fungsi_Utama_Base64_Encode_Tool.mainloop()
Base64_Encode_Tool()