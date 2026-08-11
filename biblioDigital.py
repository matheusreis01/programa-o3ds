class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return f"Título: {self.titulo} | Autor: {self.autor} | Páginas: {self.paginas}"

# Solicitação dos dados ao usuário
print("--- Cadastro de Livro ---")
titulo_input = input("Digite o título do livro: ")
autor_input = input("Digite o autor do livro: ")
paginas_input = input("Digite a quantidade de páginas: ")

# Criação do objeto Livro
livro_cadastrado = Livro(titulo_input, autor_input, paginas_input)

# Exibição da descrição formatada utilizando o método __str__()
print("\n--- Dados do Livro Cadastrado ---")
print(livro_cadastrado)
