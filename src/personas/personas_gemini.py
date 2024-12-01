import os
import google.generativeai as genai
from manager_file.manager_file import ManagerFile
from constants.ai_project_accelerator import AiProjectAcceleratorConstants

class GeminyPersonas:

    @staticmethod
    def upload_history(model, file):

        agile_manager = ManagerFile.realizar_leitura_arquivos(AiProjectAcceleratorConstants.PERSONAS_AGILE_MANAGER)
        script_program = ManagerFile.realizar_leitura_arquivos(file)

        chat_session = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [
                        agile_manager,
                        script_program,
                    ],
                },
                {
                    "role": "model",
                    "parts": [
                        "Analisando ...",
                    ],
                },
            ]
        )
        return chat_session

    @staticmethod
    def configurar_historico_chat(model, arquivo_txt):
        
        conteudo = ManagerFile.realizar_leitura_arquivos(arquivo_txt) 
        convo = model.start_chat(
            history=[
                {
                    "role": "user",
                    "parts": [conteudo],
                },
                {
                    "role": "model",
                    "parts": ["Entendido. \n"],
                },
            ]
        )
        return convo
