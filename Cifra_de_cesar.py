from tkinter import *


#    Funão para encrypt    #

def crypt_letra(letra, lista, chave):
    for i in range(len(lista)):
        if letra == ' ':
            return ' '
        elif lista[i]==letra:
            return str(lista[i+chave])
    return ' '


#   Função para decrypt    #

def crypt_letra(letra, lista, token):
    for i in range(len(lista)):
        if letra == ' ':
            return ' '
        elif lista[i]==letra:
            return str(lista[i-token])
    return ' '


#    Funão para o botão de encrypt    #

def bt_onclick():
    messagem_crypt = str()

    for letra in ed.get():
        messagem_crypt += crypt_letra(letra, lista, chave)
    lb.insert(1.0, messagem_crypt)


#    Função para o botão de Decrypt    #

def bt_onclick2():
    messagem_descrypt = str()

    for letra in ed2.get():
        messagem_descrypt += crypt_letra(letra, lista, token)
    lb2.insert(1.0, messagem_descrypt)


# Lista com o alfabeto e os caracteres especiais #

lista = [
        "b","d","g","*","f","r","z","e","y","j","l","á","â","à","å","ã","ä","é","@","ê","è","ë","Ð","ð","í","î","?","ì","ï"," ","ó","ô","ò","ø",
        "õ", "ö", "ú", "û","ù","$","ü","ç","ñ","ý","<",">","&","®","©","a","x","p","n","o","q","u","#","c","v","i","k","m", "s","h","t","w","1",
        "2","3","4","5","6","7","8","9","0"
        ]

      # ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


chave = -9
token = 9


# Configuração da janela

Janela = Tk()
Janela.title("Cifra de César")
Janela.config(padx = 10, pady = 10, background = "white")
Janela.resizable(False, False)


# Label de Título

lb_title = Label(Janela, text = "Cifra de César", background = "#fff", )
lb_title.place(x = 160, y = 120)
lb_title.config(background = "white", fg = "black", pady = 5, font = ("Helvetica", 50, "normal"), border = 0)


#  Botão e caixa de entrada para criptografar #

ed = Entry(Janela, width = 70,)
ed.place(x = 80, y = 280)
ed.config(font = "Helvetica-Bold", background = "white", fg = "black", border = 3)
# ed.insert(0,"Ex: Hello World")


bt = Button(Janela, width = 40, text = "Encrypt", command = bt_onclick)
bt.place(x = 160, y = 333,)
bt.config(background = "#ededed", fg = "black", pady = 5, font = ("Helvetica", 16 , "normal"), border = 0, cursor = "hand2",
          highlightthickness = 0, highlightbackground = "#ccc", highlightcolor = "#ccc", activebackground = "white")


for x in range(len(lista)):
    lista.append(lista[x].upper())


# Botão e caixa de entrada para decriptar  #

ed2 = Entry(Janela, width = 70)
ed2.place(x = 80, y = 510)
ed2.config(font = "Helvetica-Bold", background = "white", fg = "black", border = 3)


bt2 = Button(Janela, width = 40, text = "Decrypt", command = bt_onclick2)
bt2.place(x = 160, y = 563)
bt2.config(background = "#ededed", fg = "black",pady = 5, font = ("Helvetica", 16, "normal"), border = 0, cursor = "hand2",
          highlightthickness = 1, highlightbackground = "#ccc", highlightcolor = "#ccc", activebackground = "white")

for x in range(len(lista)):
    lista.append(lista[x].upper())


#    Label Encrypt    #

lb = Text(Janela, width = 53, height = 3)
lb.place(x = 160, y = 400)
lb.config(font = ("Helvetica-Bold", 13, "normal"), background = "white", fg = "black", border = 0)


#    Label Decrypt    #

lb2 = Text(Janela, width = 53, height = 3)
lb2.place(x = 160, y = 630)
lb2.config(background = "white", fg = "black", font = ("Helvetica", 13, "normal"), border = 0)


Janela.geometry("800x800")
Janela.mainloop()