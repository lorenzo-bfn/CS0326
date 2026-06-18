# Author: lorenzo-bfn

import os, sys, queue
from threading import Thread
from threading import Event as threadingEvent

if ( sys.version_info.major == 3 and sys.version_info.minor >= 9) or sys.version_info.major >= 4 :
    from google import genai as google_genai
    from google.genai import types as google_genai_types
else:
    from google import generativeai as google_genai
    from google.generativeai import client as google_genai_client
    from google.generativeai import types as google_genai_types
    
def inputStringa( msg_prompt = None, max_n_tentativi_input = 3, accetta_str_vuote = False ):
    n_tentativo_input_corr = 1
    string = None
    
    while n_tentativo_input_corr <= max_n_tentativi_input:
        string = input("%s: " % msg_prompt ).strip()
        if string.strip() == '' and not accetta_str_vuote:
            print("AVVISO!: E' stata inserita una stringa vuota. Riprovare ( Tentativi: %d/%d )" % (n_tentativo_input_corr, max_n_tentativi_input) )
            n_tentativo_input_corr = n_tentativo_input_corr + 1    
        else:
            break
    
    return string

class ChatbotSecurityAssistant :
    
    class ChatBotWorker ( Thread ):
        def __init__(self, q_utente, q_cb, gemini_token = None, model_name='gemini-2.5-flash', model_temp = 0.2 ):
            self.model_temp = model_temp
            self.q_utente = q_utente
            self.q_cb = q_cb
            google_genai.configure( api_key = gemini_token )
            self.gemini_model = google_genai.GenerativeModel(model_name='gemini-2.5-flash')
            super().__init__()
            self._stop_event = threadingEvent()
            self.model_config = google_genai_types.GenerateContentConfig( 
                temperature = self.model_temp,
                system_instruction = "Impersonifica un professionista del settore della Cybersecurity"
            )

        def run(self):
            while not self.stopped():
                
                try:
                    prompt_utente = self.q_utente.get_nowait()
                    self.q_utente.task_done()
                    dati_risposta = self.gemini_model.generate_content(prompt_utente, generation_config = self.model_config )
                    self.q_cb.put( dati_risposta )
                except queue.Empty:
                    continue
            print("[[ CHATBOT TERMINATO ]]")
        
        def stop(self):
            self._stop_event.set()

        def stopped(self):
            return self._stop_event.is_set()     
    
    def __init__( self, gemini_token = None, model_name='gemini-2.5-flash' , model_temp = 0.2):
        self.token_info = {"token_prompt_count" : 0, "token_candidates_count": 0, "total_token_count": 0} 
        self.chatUtenteQueue = queue.Queue()
        self.chatBotQueue = queue.Queue()
        self.gemini_model_name = model_name
        if not gemini_token:
            gemini_token = os.environ.get("GEMINI_TOKEN", inputStringa("Inserisci il token di uso del servizio Gemini AI da Google AI Studio"))
        self.worker = self.ChatBotWorker( self.chatUtenteQueue, self.chatBotQueue, gemini_token=gemini_token,model_name=self.gemini_model_name)
        self.worker.start()
    
    def cambiaTempModello( self, nuova_temperatura = None ):
        if isinstance( nuova_temperatura, str ):
            nuova_temperatura = float(arg_prompt.replace(',','.'))
            
        if isinstance( nuova_temperatura, float ):
            if nuova_temperatura >= 0.0 and nuova_temperatura <= 1.0:
                print("[[ IMPOSTAZIONE TEMPERATURA CHATBOT A %.1f]]" % nuova_temperatura )
            else:
                print("[[ Errore: Il valore della temperatura non è compreso tra 0.0 e 1.0. ]]")
                     
    def trasmettiPrompt( self, prompt ):
        self.chatUtenteQueue.put( prompt )
        
        try:
            risposta = self.chatBotQueue.get(timeout=30)
            print(f"[Chatbot]: {risposta.text}")
            self.chatBotQueue.task_done()
            
            self.token_info["token_prompt_count"] = self.token_info["token_prompt_count"] + risposta.usage_metadata.prompt_token_count
            self.token_info["token_candidates_count"] = self.token_info["token_candidates_count"] + risposta.usage_metadata.candidates_token_count
            self.token_info["total_token_count"] = self.token_info["total_token_count"] + risposta.usage_metadata.total_token_count
            
            return risposta.text
        except queue.Empty:
            print("[[ Errore: Il chatbot ha impiegato troppo tempo a rispondere. ]]")
        
    def stopWorker(self):
        if self.worker:
            print("[[ TERMINAZIONE DEL CHATBOT IN CORSO ]]")
            self.worker.stop()
       
if __name__ == '__main__':
    gemini_token = os.environ.get("GEMINI_API_TOKEN", inputStringa("Inserisci il token di uso del servizio Gemini AI da Google AI Studio [ Per evitare questo prompt, aggiungi la chiave in ""GEMINI_API_TOKEN"" nella variabili di ambiente di Windows o nei file .bashrc/.zxrc in Linux con la sinstassi ""export""]\nToken: "))
    
    csa = ChatbotSecurityAssistant( gemini_token = gemini_token)
    print("[[ CHATBOT SECURITY ASSISTANT ]]\n")
    print("-- Bangwords -----------------------------------------------")
    print(" - !stop : termina la chat")
    print(" - !conteggio_token: mostra il conteggio dei token Gemini")
    print(" - !cambia_temperatura <temperatura>: cambia la temperatura del chatbot")
    print("\n----------------------------------------------------------")
    
    while True:
        try:
            prompt = inputStringa("[UTENTE] ", accetta_str_vuote=False)
            if prompt.strip() == "!stop":
                csa.stopWorker()
                break
            elif prompt.strip() == "!conteggio_token":
                print("[[ Conteggio token di prompt: %d ]]\n[[ Conteggio token di risposta (candidates): %d ]]\n[[ Conteggio token totali: %d ]]" % (
                        csa.token_info["token_prompt_count"], csa.token_info["token_candidates_count"], csa.token_info["total_token_count"], 
                ) )
            elif prompt.strip().startswith('!cambia_temperatura'):
                arg_prompt = prompt.strip().split(' ')
                if arg_prompt.__len__() > 1: 
                    csa.cambiaTempModello( nuova_temperatura = arg_prompt[1] )
            else: csa.trasmettiPrompt(prompt)
        except KeyboardInterrupt:
            csa.stopWorker()
            break