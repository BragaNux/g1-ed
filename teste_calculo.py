from tkinter import *
from PIL import Image, ImageTk
from g1 import calcular

# Estrutura da janela
calculadora = Tk()
calculadora.title(' Calculadora ®')
calculadora.geometry('475x500+500+100')
calculadora.resizable(width=False, height=False)

# Carregar a imagem de fundo
imagem_fundo = Image.open("C:\dado.jpg")
imagem_fundo = imagem_fundo.resize((500, 500), Image.Resampling.BILINEAR)
imagem_fundo = ImageTk.PhotoImage(imagem_fundo)

# Exibir a imagem de fundo
label_fundo = Label(calculadora, image=imagem_fundo)
label_fundo.place(x=0, y=0, relwidth=1, relheight=1)


def btNumeros(numero):  # função que ativa os botões numéricos
    pegaNumero = campoNumeros.get()
    campoNumeros.delete(0, END)
    campoNumeros.insert(0, str(pegaNumero) + str(numero))
    return

def limpaCompo():
    campoNumeros.delete(0, END)
    return

def igual():
    expressao = campoNumeros.get()
    resultado = calcular(expressao)  # Avalia a expressão
    campoNumeros.delete(0, END)
    campoNumeros.insert(0, str(resultado))
    return

# entry
campoNumeros = Entry(calculadora, width=40)
campoNumeros.place(x=120, y=25)

# botões
bt1 = Button(calculadora, text='❶', relief=FLAT, width=10, height=3, command=lambda: btNumeros(1))
bt1.place(x=50, y=150)

bt2 = Button(calculadora, text='❷', relief=FLAT, width=10, height=3, command=lambda: btNumeros(2))
bt2.place(x=150, y=150)

bt3 = Button(calculadora, text='❸', relief=FLAT, width=10, height=3, command=lambda: btNumeros(3))
bt3.place(x=250, y=150)

bt4 = Button(calculadora, text='❹', relief=FLAT, width=10, height=3, command=lambda: btNumeros(4))
bt4.place(x=50, y=225)

bt5 = Button(calculadora, text='❺', relief=FLAT, width=10, height=3, command=lambda: btNumeros(5))
bt5.place(x=150, y=225)

bt6 = Button(calculadora, text='❻', relief=FLAT, width=10, height=3, command=lambda: btNumeros(6))
bt6.place(x=250, y=225)

bt7 = Button(calculadora, text='❼', relief=FLAT, width=10, height=3, command=lambda: btNumeros(7))
bt7.place(x=50, y=300)

bt8 = Button(calculadora, text='❽', relief=FLAT, width=10, height=3, command=lambda: btNumeros(8))
bt8.place(x=150, y=300)

bt9 = Button(calculadora, text='❾', relief=FLAT, width=10, height=3, command=lambda: btNumeros(9), bd=2, highlightbackground="#005ea6")
bt9.place(x=250, y=300)

bt0 = Button(calculadora, text='⓿', relief=FLAT, width=10, height=3, command=lambda: btNumeros(0))
bt0.place(x=150, y=375)

btVirgula = Button(calculadora, text='C', relief=FLAT, width=10, height=3, command=limpaCompo)
btVirgula.place(x=50, y=375)

btIgual = Button(calculadora, text='=', relief=FLAT, width=10, height=3, command=igual)
btIgual.place(x=250, y=375)

btDivisao = Button(calculadora, text='➗', relief=FLAT, width=10, height=3, command=lambda: btNumeros('/'))
btDivisao.place(x=350, y=150)

btMultiplicacao = Button(calculadora, text='✖️', relief=FLAT, width=10, height=3, command=lambda: btNumeros('*'))
btMultiplicacao.place(x=350, y=225)

btSoma = Button(calculadora, text='➕', relief=FLAT, width=10, height=3, command=lambda: btNumeros('+'))
btSoma.place(x=350, y=300)

btSubtracao = Button(calculadora, text='➖', relief=FLAT, width=10, height=3, command=lambda: btNumeros('-'))
btSubtracao.place(x=350, y=375)

btC = Button(calculadora, text='(', relief=FLAT, width=5, height=3, command=lambda: btNumeros('('))
btC.place(x=90, y=75)

btPorcentagem = Button(calculadora, text=')', relief=FLAT, width=5, height=3, command=lambda: btNumeros(')'))
btPorcentagem.place(x=140, y=75)

btPotencia = Button(calculadora, text='^', relief=FLAT, width=5, height=3, command=lambda: btNumeros('^'))
btPotencia.place(x=270, y=75)

btPotencia = Button(calculadora, text='log()', relief=FLAT, width=5, height=3, command=lambda: btNumeros('°'))
btPotencia.place(x=320, y=75)

btRaiz = Button(calculadora, text='√', relief=FLAT, width=5, height=3, command=lambda: btNumeros('√'))
btRaiz.place(x=370, y=75)

desenvolvidoPor = Label(calculadora, text='  DEVs: Daniel & Brayan  ')
desenvolvidoPor.place(x=175, y=455)

calculadora.mainloop()
