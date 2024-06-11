import os
from dataclasses import dataclass

os.system("cls || clear")

QUANTIDADE_LIVROS = 2

@dataclass
class Livros:
    titulo: str
    autor: str
    paginas: int
    preco: float

livros = []

for i in range(QUANTIDADE_LIVROS):
    titulo = input("\nDigite o título do livro: ")
    autor = input("Digite o nome do autor do livro inserido: ")
    paginas = int(input("Digite o número de páginas presente no livro: "))
    preco = float(input("Digite o preço do livro inserido:R$ "))
    livro = Livros(titulo = titulo, autor = autor, paginas = paginas, preco = preco)
    livros.append(livro)

for cadastro_livro in livros:
    print(f"\nTítulo: {cadastro_livro.titulo}")
    print(f"Autor: {cadastro_livro.autor}")
    print(f"Quantidade de paginas: {cadastro_livro.paginas}")
    print(f"Preço:R$ {cadastro_livro.preco}")