## Importando e formatando interface grafica de cadastro.

from tkinter import *

class Gui():
    x_pad = 5
    y_pad = 3
    width_entry = 30

    ## Nome fantasia da aplicacao.
    
    window = Tk()
    window.wm_title("PYSQL versao 1.0")

    ## Definindo variaveis de imput.
    
    nome = StringVar()
    sobrenome = StringVar()
    email = StringVar()
    cpf = StringVar()

    ## Criando os objetos que farao parte das janelas.

    lblNome = Label(window, text = "Nome")
    lblSobrenome = Label(window, text = "Sobrenome")
    lblEmail = Label(window, text = "Email")
    lblCpf = Label(window, text = "CPF")

    ## Definindo as entradas com as variaveis acima.

    entNome = Entry(window, textvariable = nome, width = width_entry)
    entSobrenome = Entry(window, textvariable = sobrenome, width = width_entry)
    entEmail = Entry(window, textvariable = email,  width = width_entry)
    entCPF = Entry(window, textvariable = cpf, width = width_entry)

    listClientes = Listbox(window, width = 100)

    scrollClientes = Scrollbar(window)

    btnViewAll = Button(window, text = "Ver todos")
    btnBuscar = Button(window, text = "Buscar")
    btnInserir = Button(window, text = "Inserir")
    btnUpdate = Button(window, text = "Atualizar selecionados")
    btnDel = Button(window , text = "Deletar selecionados")
    btnClose = Button(window, text = "Fechar")

    ## Criando o Grid e associando as labels acima.

    lblNome.grid(row = 0, column = 0)
    lblSobrenome.grid(row = 1, column = 0)
    lblEmail.grid(row = 2, column = 0)
    lblCpf.grid(row = 3, column = 0)

    ## Grids da entrada

    entNome.grid(row = 0, column = 1, padx = 50, pady = 50)
    entSobrenome.grid(row = 1, column = 1)
    entEmail.grid(row = 2, column = 1)
    entCPF.grid(row = 3, column = 1)

    listClientes.grid(row = 0, column = 2, rowspan = 10)
    scrollClientes.grid(row = 0, column = 6, rowspan = 10)

    btnViewAll.grid(row = 4, column = 0, columnspan = 2)
    btnBuscar.grid(row = 5, column = 0, columnspan = 2)
    btnInserir.grid(row = 6, column = 0, columnspan = 2)
    btnUpdate.grid(row = 7, column = 0, columnspan = 2)
    btnDel.grid(row = 8, column = 0, columnspan = 2)
    btnClose.grid(row = 9, column = 0, columnspan = 2)

    ## Uniao do Scrollbar com a Listbox.

    listClientes.configure(yscrollcommand = scrollClientes.set)
    scrollClientes.configure(command = listClientes.yview)

    ## Adicionar SWAG (aparencia) a interface.

    for child in window.winfo_children():
        widget_class = child.__class__.__name__
        if widget_class == "Button":
            child.grid_configure(sticky = 'WE', padx = x_pad, pady = y_pad)
        elif widget_class == "Listbox":
            child.grid_configure(padx = 0, pady = 0, sticky = 'NS')
        elif widget_class == "Scrollbar":
            child.grid_configure(padx = 0, pady = 0, sticky = 'NS')
        else:
            child.grid_configure(padx = x_pad, pady = y_pad, sticky = 'N')

    def run(self):
        self.window.mainloop()







