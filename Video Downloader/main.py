from os import system
try: import youtube_dl, pystyle
except: system("pip install -r requirements.txt")
from pystyle import Colors, Colorate, Write, Center
style = f"[{Colors.blue}*{Colors.reset}] "
ako = """
 __      ___     _              _____                      _                 _           
 \ \    / (_)   | |            |  __ \                    | |               | |          
  \ \  / / _  __| | ___  ___   | |  | | _____      ___ __ | | ___   __ _  __| | ___ _ __ 
   \ \/ / | |/ _` |/ _ \/ _ \  | |  | |/ _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
    \  /  | | (_| |  __/ (_) | | |__| | (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   Made by Ako
     \/   |_|\__,_|\___|\___/  |_____/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_| github.com/Ako-fr
                                                                                         
                                                                                         
"""
def downloader():
    print(Colorate.Vertical(Colors.red_to_blue, Center.XCenter(ako)))
    url = Write.Input("[>] Indiquez l'url de la video : ", Colors.white)
    youtube_option = {"format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"}
    with youtube_dl.YoutubeDL(youtube_option) as ytb: ytb.download([url]), print(style + "Video Dowload, Appuyez pour continuer"), input(), system("cls"), downloader()
downloader()