from tkinter import *

janela = Tk() #inicializa o tkint

janela.title('Olá mundo') #titulo para a janela
janela.geometry('250x250') #Tamanho que vai ser aberta a janela 

# janela.configure(background= '#141313') #Cor de fundo da janela

# Label = Label(janela, text="Primeiro Label", font=("Arial Bold", 14), fg='green', bg='white') #rótulo e fonte e tamnaho e cor de letra e fundo
# Label.grid(column=0, row=0) #posição da janela

# # botao = Button(janela, text="Clique aqui", bg='black', fg='white') #Cria um botão na janela 
# # botao.grid(column=1, row=2) #  add o botão na janela

# def botao1():
#     print('Olá mundo, eu estou usando python')  #Aparece a mensagem no consola
#     Label.configure(text='Olá, eu estou usasando python') #aparece a mensage na interface grafica

# botao = Button(janela, text='Clique aqui', command= botao1 )
# botao.grid(column=0, row=1)


# entrada = Entry(janela, width=10)
# entrada.grid(column=0, row=2)

# def entrada():
#     resultado = entrada.get()
#     Label.config(text=resultado)

label = Label (janela, text = "Primeiro entry")
label.grid (column = 0, row = 0, padx=15, pady=15)

entrada = Entry(janela,width=10)
entrada.grid(column=1, row=0, padx=5, pady=15)

def ola():
    resultado = entrada.get() * 2
    label.configure(text= resultado)

botao = Button(janela, text="Clica aqui",command = ola)
botao.grid(column=2, row=0, padx=5, pady=15)



janela.mainloop()
                 


