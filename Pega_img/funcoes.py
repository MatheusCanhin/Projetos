import io
import os
from tkinter import messagebox
import fitz as ft
from PIL import Image

# Constantes
EXTENSOES = ["jpeg", "jpg", "png"]


def inicio_fim(inicio, fim):
    """Pega os valores dos entrys de início e fim e verifica se são somentes digitos"""
    if inicio.isdigit() and fim.isdigit():
        inicio_int = int(inicio)
        fim_int = int(fim)
        if intervalo_paginas(inicio_int, fim_int):
            return True
    else:
        messagebox.showerror(title="Erro nas páginas", message="Verifique o que foi digitado em início e fim e corrija")


def intervalo_paginas(pag_inicio, pag_fim):
    """Verifica o valor de do intervalo das páginas"""
    if pag_inicio > pag_fim != 0:
        messagebox.showerror(title="Erro de página", message="A página de inicio é maior que a página final")
        return False
    elif pag_inicio < 0 or pag_fim < 0:
        messagebox.showerror(title="Erro de página", message="Existem páginas com valor negativo")
        return False
    else:
        return True


def get_images(pdf, local, inicio, fim):
    """Tem a função de percorrer as páginas do arquivo e verificar a existência de fotos"""

    pdf_file = ft.open(pdf)
    inicio_int = int(inicio)
    fim_int = int(fim)
    tamanho_pdf = len(pdf_file)

    if inicio_int > tamanho_pdf or fim_int > tamanho_pdf:
        messagebox.showerror(title="Intervalo inválido", message="O intervalo está invalido o arquivo tem "
                                                                 f"{tamanho_pdf} paginas")
    elif fim_int == 0:
        for page_index in range(inicio_int, tamanho_pdf):
            page = pdf_file[page_index]
            image_list = page.get_images()

            if len(image_list) > 0:
                create_image(image_list, pdf_file, page_index, local)
        messagebox.showinfo(title="processo finalizado", message="O processo foi finalizado")
    else:
        for page_index in range(inicio_int, fim_int):
            page = pdf_file[page_index]
            image_list = page.get_images()

            if len(image_list) > 0:
                create_image(image_list, pdf_file, page_index, local)
        messagebox.showinfo(title="processo finalizado", message="O processo foi finalizado")


def create_image(images_list, pdf_file, page_index, caminho_arquivo):
    """Tem a função de criar uma pasta com a página do arquivo e criar o arquivo da foto na pasta"""

    for image_index, img in enumerate(images_list, start=0):

        xref = img[0]
        imagem = pdf_file.extract_image(xref)
        image_bytes = imagem["image"]

        # Verifica a extensão da imagem, cria o diretório(se não existir) e salva a foto no diretório criado.
        if imagem["ext"] in EXTENSOES:
            if os.path.isdir(f"{caminho_arquivo}/pagina{page_index+1}"):
                b = bytearray(image_bytes)
                img_n = Image.open(io.BytesIO(b))
                img_n.save(f"{caminho_arquivo}/pagina{page_index+1}/pagina{page_index+1}--{image_index}.{imagem['ext']}"
                           , quality=100)
            else:
                os.makedirs(f"{caminho_arquivo}/pagina{page_index+1}")
                b = bytearray(image_bytes)
                img_n = Image.open(io.BytesIO(b))
                img_n.save(f"{caminho_arquivo}/pagina{page_index+1}/pagina{page_index+1}--{image_index}.{imagem['ext']}"
                           , quality=100)


def verifica_erros(pdf, local):
    """Realiza as verificações iniciais no arquivo e PATH"""

    if len(pdf) > 0 and len(local) > 0:
        if verifica_pdf(pdf) and verifica_path(local):
            return True
    elif len(pdf) > 0 and len(local) == 0:
        messagebox.showerror(title="Erro", message="O campo do 'PATH' está em branco")
    elif len(pdf) == 0 and len(local) > 0:
        messagebox.showerror(title="Erro", message="O campo do 'PDF' está em branco")
    else:
        messagebox.showerror(title="Erro", message="Os campos 'PDF' e 'PATH' estão em branco")


def verifica_pdf(pdf):
    """Verifica se o arquivo passado é um pdf e se é de fato um arquivo"""

    if os.path.isfile(pdf):
        if pdf[-3::] == "pdf":
            return True
        else:
            messagebox.showerror(title="Erro no arquivo", message="O arquivo não é um 'PDF'")
    else:
        messagebox.showerror(title="Erro no arquivo", message="O caminho passado não é de um arquivo")


def verifica_path(local):
    """Verifica se o caminho passado pelo usuário de fato é um diretório """

    if os.path.isdir(local):
        return True
    else:
        messagebox.showerror(title="Erro no diretório", message="O Path passado não corresponde a um diretório")
