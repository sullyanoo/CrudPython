## Uniao do BackEnd com o FrontEnd (backend.py == crud.py)

## Comando App = Gui() Faz que a variavel app se torne uma instancia da classe Gui, atraves dessa variavel app temos acesso aos elementos da janela.

## Funcao def view_command() e a funcao de visualizacao dos resultados.

## Funcao search_command() e insert_command() realizam a busca e a insercao dos dados do banco.

## Funcao getSelectedRow(event), armazena os valores informados e alimenta os campos de input com as informacoes.

from crud import Gui
from backend import TransactionObject
from tkinter import END

selected = None

def view_command():
    trans = TransactionObject()
    rows = trans.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)


def search_command():
    app.listClientes.delete(0, END)
    rows = TransactionObject().search(app.nome.get(), app.sobrenome.get(), app.email.get(), app.cpf.get())
    for r in rows:
        app.listClientes.insert(END, r)

def insert_command():
    TransactionObject().insert(app.nome.get(), app.sobrenome.get(), app.email.get(), app.cpf.get())
    view_command()

def update_command():
    if selected:
        id = selected[0]
        TransactionObject().update(selected[0], app.nome.get(), app.sobrenome.get(), app.email.get(), app.cpf.get())
        view_command()

def del_command():
    if selected:
        id = selected[0]
        TransactionObject().delete(id)
        view_command()

def getSelectedRow(event):
    global selected
    try:
        index = app.listClientes.curselection()[0]
        selected = app.listClientes.get(index)
        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])
        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])
        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])
        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])
    except IndexError:
        pass

if __name__ == "__main__":
    app = Gui()
    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)
    app.run()
