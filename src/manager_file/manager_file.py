import google.generativeai as genai
import os
import chardet

class ManagerFile:

    @staticmethod
    def erro_codificacao(caminho_arquivo):
        
        with open(caminho_arquivo, 'rb') as f:
            result = chardet.detect(f.read())
            encoding = result['encoding']
        
        return encoding

    @staticmethod
    def atualizar_arquivo(caminho_arquivo, novo_conteudo):

        encode = ManagerFile.erro_codificacao(caminho_arquivo)
        try:
            # Ler o conteúdo atual do arquivo linha a linha
            with open(caminho_arquivo, 'r', encoding=encode) as arquivo:
                conteudo_atual = arquivo.readlines()
        except FileNotFoundError:
            conteudo_atual = []

        novo_conteudo_linhas = novo_conteudo.splitlines(keepends=True)

        # Determinar quais linhas são diferentes ou novas
        linhas_a_atualizar = []
        for i, linha in enumerate(novo_conteudo_linhas):
            if i >= len(conteudo_atual) or linha != conteudo_atual[i]:
                linhas_a_atualizar.append((i, linha))

        if linhas_a_atualizar:
            # Atualizar apenas as linhas diferentes ou novas
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                for i, linha in enumerate(novo_conteudo_linhas):
                    if (i, linha) in linhas_a_atualizar:
                        arquivo.write(linha)
                    else:
                        arquivo.write(conteudo_atual[i])
                        print(f"The file {caminho_arquivo} has been updated.")
        else:
            print(f"The content of the file {caminho_arquivo} is already updated.")

    @staticmethod
    def realizar_leitura_arquivos(arquivo_txt):
        with open(arquivo_txt, 'r', encoding='utf-8', errors='ignore') as arquivo:
            arquivo_leitura = arquivo.read()
        return arquivo_leitura

    @staticmethod
    def upload_to_gemini(path, mime_type):
        file = genai.upload_file(path, mime_type=mime_type)
        print(f"Uploaded file '{file.display_name}' as: {file.uri}")
        return file

    @staticmethod
    def gravar_arquivo(pergunta, path_file):
        with open(path_file, "a", encoding="utf-8") as arquivo:
            arquivo.write(pergunta + "\n")

    @staticmethod
    def read_ementa(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        ementa = []
        current_capitulo = None
        for line in lines:
            line = line.strip()
            if line.startswith("Capítulo"):
                if current_capitulo:
                    ementa.append(current_capitulo)
                current_capitulo = {"capitulo": line, "topicos": []}
            elif line:
                current_capitulo["topicos"].append(line)
        
        if current_capitulo:
            ementa.append(current_capitulo)
        
        return ementa
