from tkinter import *
from funcoes import verifica_erros, inicio_fim, get_images

# Constantes
BACKGROUND = "#282634"


def verify():
    """Verifica se o arquivo selecionado é um pdf e se o local é um diretório mesmo"""

    pdf = pdf_adress.get().replace("file:///", "").replace("%20", " ")
    local = local_adress.get().replace("%20", " ")
    inicio = inicio_entry.get().strip()
    fim = fim_entry.get().strip()

    if verifica_erros(pdf, local):
        if inicio_fim(inicio, fim):
            get_images(pdf, local, inicio, fim)


def limpa_valores():
    """Limpa os valores dos entrys"""
    pdf_adress.delete(0, END)
    local_adress.delete(0, END)
    inicio_entry.delete(0, END)
    fim_entry.delete(0, END)
    inicio_entry.insert(0, '0')
    fim_entry.insert(0, '0')


# Criando a tela
screen = Tk()
screen.title("Extrator de imagens")
screen.configure(bg=BACKGROUND, padx=20, pady=20)
screen.minsize(height=400, width=600)
screen.maxsize(height=400, width=600)


# Imagens
# Colocando a imagem do computador
comp_img = PhotoImage(file="images/computador.png")
computer_image = Label(screen, image=comp_img, highlightthickness=0, bg=BACKGROUND)
computer_image.grid(column=0, row=0)

# Colocando imagem do programador
prog_img = PhotoImage(file="images/programador.png")
programmer_image = Label(screen, image=prog_img, highlightthickness=0, bg=BACKGROUND)
programmer_image.grid(column=5, row=7)


# Labels
# Criando o texto do do PDF
txt_pdf = Label(text="Informe o local do PDF:", font=("Ariel", 15, "bold"), fg="white", bg=BACKGROUND, padx=10)
txt_pdf.grid(column=1, row=1, columnspan=3)

# Criando o texto do do PDF
txt_local = Label(text="Informe o PATH para salvar as fotos:", font=("Ariel", 15, "bold"), fg="white", bg=BACKGROUND,
                  pady=10,)
txt_local.grid(column=1, row=3, columnspan=3)

# Criando o texto do início
txt_inicio = Label(text="Início:", font=("Ariel", 10, "bold"), fg="white", bg=BACKGROUND)
txt_inicio.grid(column=1, row=5)

# Criando o texto do fim
txt_fim = Label(text="Fim:", font=("Ariel", 10, "bold"), fg="white", bg=BACKGROUND)
txt_fim.grid(column=3, row=5)


# Entrys
# Criando a entry do local do PDF
pdf_adress = Entry(width=50, font=("Ariel", 10, "bold"), bg="grey", fg="White")
pdf_adress.grid(column=1, row=2, columnspan=3)
pdf_adress.focus()

# Criando a entry do local onde os arquivos serão salvos
local_adress = Entry(width=50, font=("Ariel", 10, "bold"), bg="grey", fg="White")
local_adress.grid(column=1, row=4, columnspan=3)

# Criando a entry do início
inicio_entry = Entry(width=5, font=("Ariel", 10, "bold"), bg="grey", fg="White")
inicio_entry.insert(0, '0')
inicio_entry.grid(column=1, row=6)

# Criando a entry do fim
fim_entry = Entry(width=5, font=("Ariel", 10, "bold"), bg="grey", fg="White")
fim_entry.insert(0, '0')
fim_entry.grid(column=3, row=6)


# Criando Botão
botao_extrair = Button(text="Extrair", font=("Ariel", 10, "bold"), bg="purple", fg="white", command=verify)
botao_extrair.grid(column=2, row=6)

# Botão Limpar campos
botao_limpar = Button(text="Limpar", font=("Ariel", 10, "bold"), bg="purple", fg="white", command=limpa_valores)
botao_limpar.grid(column=2, row=7)

# Loop para manter a tela aberta
if __name__ == '__main__':
    screen.mainloop()
