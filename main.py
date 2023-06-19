
from tkinter import *

alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

janela = Tk()
janela.title("Cifra de Ceaser")
janela.geometry('500x600')
# janela.configure(bg="white")

var = StringVar()
var.set("Selecione ")

texto1 = Label(janela, text="Selecione qual processo deseja realizar: ")
texto1.pack(padx=5, pady=5)

opcoes_menu = OptionMenu(janela, var, "Criptografar" , "Desincriptografar")
opcoes_menu.pack(padx=7, pady=7)

texto = Label(janela, text="Escreva o texto que você quer realizar o processo: ")
texto.pack(padx=5, pady=5)

entrada = Entry(janela)
entrada.pack(padx=15, pady=15)

texto3 = Label(janela, text="Escreva o valor que quer empurrar: ")
texto3.pack(padx=5, pady=5)

empurra = Entry(janela)
empurra.pack(padx=15, pady=15)

def selecionar_opcao():
    selected_option = var.get()
    try:
        valorstring = empurra.get()
        quant_troca = int(valorstring)
        if selected_option == 'Criptografar':
            resultado = caesarencode(texto_inicial=entrada.get(), quant_troca=quant_troca, var=var.get())
            resultado_label.config(text="Texto criptografado: " + resultado)
        elif selected_option == 'Desincriptografar':
            resultado = caesardecode(texto_inicial=texto.get(), quant_troca=quant_troca, var=var.get())
            resultado_label.config(text="Texto criptografado: " + resultado)
    except ValueError:
        print('Insira um valor válido')


def caesarencode(texto_inicial, quant_troca, var):
  texto_final = ""
  var == "criptografia"
  for letra in texto_inicial:
    if letra in alfabeto:
      posicao = alfabeto.index(letra)
      nova_posicao = posicao + quant_troca
      texto_final += alfabeto[nova_posicao]
  print("Aqui está:")
  return texto_final

def caesardecode(texto_inicial, quant_troca, var):
  texto_final = ""
  if var == "descriptografar":
    var == "descriptografia"
  for letra in texto_inicial:
    if letra in alfabeto:
      posicao = alfabeto.index(letra)
      nova_posicao = posicao - quant_troca
      texto_final += alfabeto[nova_posicao]
  return texto_final


finalizar = False

button = Button(janela, text="Começar", command = selecionar_opcao)
button.pack(padx=30, pady=30)

resultado_label = Label(janela, text="")
resultado_label.pack(padx=5, pady=5)

janela.mainloop()
