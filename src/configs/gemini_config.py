import google.generativeai as genai


class GeminiConfig:
    """Classe para configurar o Google Gemini com chave API, parâmetros de geração e model."""

    @staticmethod
    def configurar_gemini(arquivo_txt):
        """Método estático para configurar o Gemini com chave API, parâmetros de geração e retornar o model."""

        # Carrega a chave API do arquivo
        with open(arquivo_txt, 'r', encoding='utf-8') as arquivo:
            chave_api = arquivo.read()

        # Configura o Gemini com a chave API
        genai.configure(api_key=chave_api)

        # Define as configurações de geração
        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
        }

        # Define as configurações de segurança
        safety_settings = [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE"
            },
        ]

        # Cria o modelo
        model = genai.GenerativeModel(
            model_name="gemini-1.5-pro-latest",
            generation_config=generation_config,
            safety_settings=safety_settings
        )

        return model