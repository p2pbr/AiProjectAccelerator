import winsound
import time
import win32api
import win32com
       
class TecladoUtil:
       
       @staticmethod
       def pressionar_tecla(tecla):        
        vk_up = tecla
        KEYEVENTF_EXTENDEDKEY= 0x0001
        win32api.keybd_event(vk_up, 0, KEYEVENTF_EXTENDEDKEY, 0)
        time.sleep(0.1)
        winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
