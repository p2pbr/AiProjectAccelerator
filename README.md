# AiProjectAccelerator
https://github.com/p2pbr/AiProjectAccelerator


**Descrição:** O AiProjectAccelerator é uma ferramenta inovadora desenvolvida em Python que utiliza inteligência artificial para acelerar o processo de codificação dos desenvolvedores. Com um design independente de qualquer IDE, esta solução pode ser integrada a diversas plataformas de desenvolvimento, oferecendo flexibilidade e eficiência.

## 🌟 Diferenciais

- **Geração Automática de Estruturas:** Ao inserir prompts específicos, como "elabore um projeto Java com classes de modelo e um método que executa as operações", o AiProjectAccelerator cria automaticamente a estrutura de diretórios e as classes necessárias, permitindo que o desenvolvedor inicie rapidamente seu projeto sem se preocupar com a configuração inicial.

- **Refatoração Inteligente:** A ferramenta monitora e analisa as alterações no código em tempo real. Se necessário, ela sugere correções e melhorias, ajudando a garantir que o código esteja sempre otimizado e livre de erros.

## 🚀 Como Começar

### 1. Instalação

Instruções passo a passo sobre como instalar e configurar o projeto.

#### 1.1. Instale o Python

- Python 3.10.6 ou superior.

#### 1.2. Instale o Git para clonar o projeto

1. Abra o prompt de comandos do Windows: `cmd`.
2. Crie a pasta: `C:\agent` com o comando `C:\>mkdir agent`.
3. Acesse a pasta: `agent` usando `C:\>cd agent`.

#### 1.3. Clone o projeto

Execute o comando:
C:\agent>git clone https://github.com/p2pbr/AiProjectAccelerator.git

#### 1.4. Crie um ambiente virtual na pasta: `C:\agent`

Para criar um ambiente virtual, use o comando:
C:\agent>python -m venv venv

#### 1.5. Ative o ambiente virtual

Navegue até a pasta Scripts do ambiente virtual com os seguintes comandos:
C:\agent>cd venv
C:\agent\venv>cd Scripts
C:\agent\venv\Scripts>activate
Verifique se o ambiente está ativado, que ficará assim: `(venv) C:\agent\venv\Scripts>`.

#### 1.6. Crie a pasta para suas chaves API Gemini

Crie a pasta com os comandos:
C:\agent>mkdir api_key
C:\agent>cd api_key

Dentro da pasta `C:\agent\api_key`, crie os seguintes arquivos `.txt` para salvar suas chaves API:

- **chave-api-mvd.txt:** Cole a sua chave API na primeira linha do arquivo.
- **chave-api-p2p.txt:** Cole a sua chave API na primeira linha do arquivo.

> **ATENÇÃO:** É necessário 2 chaves API do Google Gemini para realizar as solicitações ao Google Gemini, e as configurações de armazenamento estão fora do repositório por questão de segurança e para evitar o vazamento dessas informações.

5. Uso: Exemplos de como usar o projeto, incluindo comandos e opções. 
após clonar o projeto 
ative o ambiente virtual
instalar gemini: $ pip install google-generativeai

acesso o diretório do projeto e execute o arquivo execute.py

digie o seu prompt passando os requisito para o agente


🛠️ Contribuições

Autores:
