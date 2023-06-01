#!/usr/bin/env python
# coding: utf-8

# In[2]:


import os

#Criando layout
import PySimpleGUI as sg
from fpdf import FPDF


def open_pdf():
    os.startfile('Orçamento.pdf')
layout=[
    [sg.Text("Digite a descrição do projeto")],
    [sg.InputText(key='projeto')],
    [sg.Text("Digite o total de horas estimadas")],
    [sg.InputText(key='horas_estimadas')],
    [sg.Text("Digite o valor da hora trabalhada")],
    [sg.InputText(key='valor_hora')],
    [sg.Text("Digite o prazo estimado")],
    [sg.InputText(key='prazo')],
    [sg.Button("Gerar Orçamento")],
    [sg.Button("Abrir PDF", key="open_pdf")],
    [sg.Text("",key='texto_orcamento')],
]

# In[3]:


#Gerando PDF
janela = sg.Window("Orçamento",layout)

while True:
    evento, valores = janela.read()
    if evento == sg.WIN_CLOSED:
        break
    if evento == "Gerar Orçamento":
        janela['texto_orcamento'].update("Orçamento Gerado com Sucesso")
        
        pdf = FPDF()

        pdf.add_page()

        pdf.set_font("Arial")
        pdf.image("template.png", x=0,y=0)

        pdf.text(115, 145, valores['projeto'])
        pdf.text(115, 160, valores['horas_estimadas'])
        pdf.text(115, 175, valores['valor_hora'])
        pdf.text(115, 190, valores['prazo'])
        
        horas_estimadas = int(valores['horas_estimadas'].replace(' hora', ''))
        valor_total = horas_estimadas * int(valores['valor_hora'])



        pdf.text(115,205, str(valor_total))
        pdf.output("Orçamento.pdf")
        print("Orçamento gerado com sucesso")
    elif evento == 'open_pdf':
        open_pdf()

janela.close()



