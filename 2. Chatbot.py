import speech_recognition as sr
from gtts import gTTS
import transformers
import os
import time
import datetime
import numpy as np
import ChatBotModule as ChatBot

if __name__ == "__main__":
    ai = ChatBot(name="sri")
    nlp = transformers.pipeline("conversational", model="microsoft/DialoGPT-medium")
    os.environ["TOKENIZERS_PARALLELISM"] = "true"
    
    ex = True
    while ex:
        ai.speech_to_text()
        print("xxxxxxxxxxxx")
        print(ai.text)

        if ai.wake_up(ai.text) is True:
            res = "Hello I am Sri the AI, what can I do for you?"
        elif "time" in ai.text:
            res = ai.action_time()
        elif any(i in ai.text for i in ["thank you", "thanks"]):
            res = np.random.choice(["you're welcome!", "anytime!", "no problem!", "cool!", "I'm here if you need me!", "mention not"])
        elif any(i in ai.text for i in ["exit", "close"]):
            res = np.random.choice(["Tata", "Have a good day", "Bye", "Goodbye", "Hope to meet soon", "peace out!"])
            ex = False
        else:   
            if ai.text == "ERROR":
                res = "Sorry, come again?"
            else:
                chat = nlp(transformers.Conversation(ai.text), pad_token_id=50256)
                res = str(chat)
                res = res[res.find("bot >> ")+6:].strip()

        ai.text_to_speech(res)
    print("----- Closing down sri -----")
    
#Bot-Army©️