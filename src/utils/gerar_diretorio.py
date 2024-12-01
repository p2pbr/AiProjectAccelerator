import json
import os

class PlanejarProjeto:

    @staticmethod
    def criar_pastas_e_arquivos(json_data):
        try:
            # Carrega o JSON com tratamento para caracteres inválidos
            data = json.loads(json_data, strict=False)
            
            base_dir = ''
            
            # Inicializa a lista de nós a serem processados com o nó raiz
            nodes_to_process = [(base_dir, data['data'])]
            
            while nodes_to_process:
                diretorio_pai, conteudo = nodes_to_process.pop(0)
                
                for diretorio, subconteudo in conteudo.items():
                    diretorio = diretorio.lstrip('/')
                    
                    # Substitui caracteres inválidos no nome do diretório
                    diretorio = diretorio.replace(':', '_')
                    
                    diretorio_completo = os.path.join(diretorio_pai, diretorio)
                    
                    # Verifica se o conteúdo é um diretório
                    if isinstance(subconteudo, dict):
                        if not os.path.exists(diretorio_completo):
                            os.makedirs(diretorio_completo)
                        # Adiciona subdiretório para processamento futuro
                        nodes_to_process.append((diretorio_completo, subconteudo))
                    
                    # Verifica se o conteúdo é um arquivo
                    elif isinstance(subconteudo, str):
                        # Substitui caracteres inválidos no nome do arquivo
                        nome_arquivo = diretorio.replace(':', '_')
                        
                        try:
                            # Tenta criar o arquivo apenas se não terminar com extensão de diretório conhecida
                            with open(os.path.join(diretorio_pai, nome_arquivo), 'w') as f:
                                f.write(subconteudo)
                        except Exception as e:
                            print(f"Erro ao criar arquivo '{nome_arquivo}': {str(e)}")

        except json.JSONDecodeError as json_err:
            print(f"Erro de decodificação JSON: {json_err}")
        except Exception as e:
            print(f"Ocorreu um erro ao criar os diretórios e arquivos: {str(e)}")



    
    @staticmethod
    def criar_diretorios_e_arquivos(json_data):
        try:
            # Carrega o JSON
            data = json.loads(json_data)

            # Navega pelos dados do JSON
            for diretorio, conteudo in data['data']['workspace']['src'].items():
                # Cria o diretório se ainda não existir
                caminho_diretorio = os.path.join('workspace', 'src', diretorio)
                if not os.path.exists(caminho_diretorio):
                    os.makedirs(caminho_diretorio)

                # Navega pelo conteúdo de cada diretório
                for subdiretorio, arquivos in conteudo.items():
                    if isinstance(arquivos, str):
                        # Cria o arquivo no diretório
                        caminho_arquivo = os.path.join(caminho_diretorio, subdiretorio)
                        with open(caminho_arquivo, 'w') as f:
                            f.write(arquivos)
                        print(f'Criado arquivo: {caminho_arquivo}')
                    elif isinstance(arquivos, dict):
                        # Cria o subdiretório se ainda não existir
                        caminho_subdiretorio = os.path.join(caminho_diretorio, subdiretorio)
                        if not os.path.exists(caminho_subdiretorio):
                            os.makedirs(caminho_subdiretorio)
                        
                        # Cria cada arquivo no subdiretório com seu conteúdo
                        for nome_arquivo, codigo in arquivos.items():
                            caminho_arquivo = os.path.join(caminho_subdiretorio, nome_arquivo)
                            with open(caminho_arquivo, 'w') as f:
                                f.write(codigo)
                            print(f'Criado arquivo: {caminho_arquivo}')
                    else:
                        print(f'Conteúdo inválido para o diretório {subdiretorio}')

            print("Diretórios e arquivos criados com sucesso!")

        except Exception as e:
            print(f"Ocorreu um erro ao criar os diretórios e arquivos: {str(e)}")
