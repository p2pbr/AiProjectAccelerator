import json
import os
import mimetypes
import time
import threading
import google.generativeai as genai
from configs.gemini_config import GeminiConfig
from personas.personas_gemini import GeminyPersonas
from manager_file.manager_file import ManagerFile
from monitorar.monitore import FileMonitor
from utils.teclado_util import TecladoUtil
from utils.gerar_diretorio import PlanejarProjeto
from constants.ai_project_accelerator import AiProjectAcceleratorConstants

model_p2p = GeminiConfig.configurar_gemini(AiProjectAcceleratorConstants.MODEL_P2P)
model_mvd = GeminiConfig.configurar_gemini(AiProjectAcceleratorConstants.MODEL_MVD)
print(ManagerFile.realizar_leitura_arquivos(AiProjectAcceleratorConstants.DOCS_GREETINGS))

agile_Accelerator = GeminyPersonas.configurar_historico_chat(model_p2p, AiProjectAcceleratorConstants.PERSONAS_AGILE_ACCELERATOR)
pergunta = input(AiProjectAcceleratorConstants.QUESTION)
ManagerFile.gravar_arquivo(pergunta, AiProjectAcceleratorConstants.LOGS_AGILE_ACCELERATOR)

agile_Accelerator.send_message(pergunta)
resposta = agile_Accelerator.last.text
ManagerFile.gravar_arquivo(resposta, AiProjectAcceleratorConstants.LOGS_AGILE_ACCELERATOR)
print(ManagerFile.realizar_leitura_arquivos(AiProjectAcceleratorConstants.DOCS_FEEDBACK))

json_data = resposta
PlanejarProjeto.criar_pastas_e_arquivos(json_data)
time.sleep(3)

diretorio_path = AiProjectAcceleratorConstants.DIRETORIO_PATH 
file_name = FileMonitor.monitorar_diretorio(diretorio_path)
print(file_name)

agile_p2p = GeminyPersonas.upload_history(model_p2p, file_name)
agile_mvd = GeminyPersonas.upload_history(model_mvd, file_name)
time.sleep(2)
pergunta = AiProjectAcceleratorConstants.ANALISE_CODE 

toggle = False

while True:
    toggle = not toggle
    if toggle:
        agile_mvd.send_message(pergunta)
        resposta = agile_mvd.last.text
        print(resposta)
        ManagerFile.atualizar_arquivo(file_name, resposta)
        print(AiProjectAcceleratorConstants.ANSWER_FEEDBACK)
    else:
        agile_p2p.send_message(pergunta)
        resposta = agile_p2p.last.text
        print(resposta)
        ManagerFile.atualizar_arquivo(file_name, resposta)
        print(AiProjectAcceleratorConstants.ANSWER_FEEDBACK)
        
    tecla_f5 = 0x74
    TecladoUtil.pressionar_tecla(tecla_f5)

    model_p2p = None
    model_mvd = None
    model_p2p = GeminiConfig.configurar_gemini(AiProjectAcceleratorConstants.MODEL_P2P)
    model_mvd = GeminiConfig.configurar_gemini(AiProjectAcceleratorConstants.MODEL_MVD)

    FileMonitor.reset_monitoring()
    diretorio_path = None
    file_name = None

    time.sleep(0.1)
    diretorio_path = AiProjectAcceleratorConstants.DIRETORIO_PATH
    file_name = FileMonitor.monitorar_diretorio(diretorio_path)
    print(file_name)
    
    agile_p2p = GeminyPersonas.upload_history(model_p2p, file_name)
    agile_mvd = GeminyPersonas.upload_history(model_mvd, file_name)
    time.sleep(0.1)
    pergunta = AiProjectAcceleratorConstants.ANALISE_CODE