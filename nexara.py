import os
import subprocess
from pystyle import Colors, Colorate

def zeidenfonc1():
    os.system('cls' if os.name == 'nt' else 'clear')

def zeidenfonc2():
    zeidenfonc3 = r"""
         _nnnn_                      
        dGGGGMMb     ,"""""""""""""""""".
       @p~qp~~qMb    | Get a doxed negga|
       M|@||@) M|   _;..................'
       @,----.JM| -'
      JS^\__/  qKL
     dZP        qKRb
     dZP          qKKb
   fZP            SMMb
   HZM            MMMM
   FqM            MMMM
 __| ".        |\dS"qML
 |    `.       | `' \Zq
_)      \.___.,|     .'
\____   )MMMMMM|   .'
     `-'       `--'  
    """
    print(Colorate.Horizontal(Colors.red_to_yellow, zeidenfonc3))
    input("Press Enter...")
    zeidenfonc1()

def zeidenfonc4():
    zeidenfonc5 = """
▗▖  ▗▖▗▄▄▄▖▗▖  ▗▖ ▗▄▖ ▗▄▄▖  ▗▄▖ 
▐▛▚▖▐▌▐▌    ▝▚▞▘ ▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌
▐▌ ▝▜▌▐▛▀▀▘  ▐▌  ▐▛▀▜▌▐▛▀▚▖▐▛▀▜▌
▐▌  ▐▌▐▙▄▄▖▗▞▘▝▚▖▐▌ ▐▌▐▌ ▐▌▐▌ ▐▌

  Dev by zeiden | .gg/cfxdata
"""
    print(Colorate.Horizontal(Colors.red_to_yellow, zeidenfonc5))

    zeidenfonc6 = "Welcome to Nexara the OSINT directory V3"
    zeidenfonc7 = "Choose an option :"

    print("\n" + zeidenfonc6.center(os.get_terminal_size().columns))
    print(zeidenfonc7.center(os.get_terminal_size().columns))

def zeidenfonc8():
    zeidenfonc9 = [
        "1. OSINT",
        "2. Tool info",
        "3. Leave"
    ]

    zeidenfonc10 = os.get_terminal_size().columns
    zeidenfonc11 = (
        zeidenfonc9[0].ljust(zeidenfonc10 // 3) + 
        zeidenfonc9[1].center(zeidenfonc10 // 3) + 
        zeidenfonc9[2].rjust(zeidenfonc10 // 3)
    )

    print("\n" + zeidenfonc11 + "\n")

def zeidenfonc12():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Choose an option :"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "1. IP Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "2. Mail Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "3. Username Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "4. Image Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "5. Number Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "6. Name and First Name Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "7. Free DB"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "8. Google Advanced"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "9. Scraping Instagram"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "10. Back to main menu"))  

def zeidenfonc13():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Tool info:"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "Created by Zeiden"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "Created on 01/08/24 / update on 18/08/24"))

def zeidenfonc14():
    print(Colorate.Horizontal(Colors.red_to_yellow, "IP lookup & location : https://www.iplocation.net/"))

def zeidenfonc15():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Mail lookup : https://thatsthem.com/reverse-email-lookup"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://epieos.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://haveibeenpwned.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://leakcheck.io/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://dehashed.com/"))

def zeidenfonc16():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Username lookup : https://whatsmyname.app/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://instantusername.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://www.peekyou.com/username"))

def zeidenfonc17():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Image lookup : https://tineye.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://pimeyes.com/fr"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://facecheck.id/fr"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://lens.google/intl/fr/"))

def zeidenfonc18():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Numéro lookup : https://www.capeutservir.com/telephonie/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://www.emobiletracker.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://www.pagesjaunes.fr/annuaireinverse"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "\nAstuce : Pour rechercher des informations en utilisant un numéro de téléphone, commencez par l'ajouter à vos contacts. Pour ensuite le renommer en quelque chose que vous allez retenir, ensuite aller sur les réseaux sociaux qui permettent de retrouver des utilisateurs par leur numéro, comme WhatsApp, Snapchat, Telegram, ou Messenger. Et une fois dessus vous pouvez vous rendre dans un onglet pour ajouter une personne en ami depuis ses contacts, donc grâce à cette technique vous obtiendrez les réseaux sociaux associés à un numéro de téléphone."))

def zeidenfonc19():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Name and First Name lookup :"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "Facebook : https://www.facebook.com"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "Pages Jaunes : https://www.pagesjaunes.fr"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "LinkedIn : https://www.linkedin.com"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "Infobel : https://www.infobel.com/fr/france"))

def zeidenfonc20():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Do advanced research on Google : https://www.google.com/advanced_search"))

def zeidenfonc21():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Free DB ---) Snusbase, Seekbase, Nazapi => https://discord.gg/cfxdata"))

def zeidenfonc22():
    zeidenfonc2()
    zeidenfonc4()
    while True:
        zeidenfonc8()
        zeidenfonc23 = input("Enter your choice : ")

        if zeidenfonc23 == '1':
            while True:
                zeidenfonc1()
                zeidenfonc4()
                zeidenfonc12()
                zeidenfonc24 = input("Enter your choice : ")

                if zeidenfonc24 == '1':
                    zeidenfonc1()
                    zeidenfonc4()
                    zeidenfonc14()
                    input("Press Enter to return to the OSINT screen ...")
                elif zeidenfonc24 == '2':
                    zeidenfonc1()
                    zeidenfonc4()
                    zeidenfonc15()
                    input("Press Enter to return to the OSINT screen ...")
                elif zeidenfonc24 == '3':
                    zeidenfonc1()
                    zeidenfonc4()
                    zeidenfonc16()
                    input("Press Enter to return to the OSINT screen ...")
                elif zeidenfonc24 == '4':
                    zeidenfonc1()
                    zeidenfonc4()
                    zeidenfonc17()
                    input("Press Enter to return to the OSINT screen ...")
                elif zeidenfonc24 == '5':
                    zeidenfonc1()
                    zeidenfonc4()
                    zeidenfonc18()
                    input("Press Enter to return to the OSINT screen ...")
                elif zeidenfonc24 == '6':
                    zeidenfonc1()
                    zeidenfonc4()
                    zeidenfonc19()
                    input("Press Enter to return to the OSINT screen ...")
                elif zeidenfonc24 == '7':
                    zeidenfonc1()
                    zeidenfonc4()
                    zeidenfonc21()
                    input("Press Enter to return to the OSINT screen ...")
                elif zeidenfonc24 == '8':
                    zeidenfonc1()
                    zeidenfonc4()
                    zeidenfonc20()
                    input("Press Enter to return to the OSINT screen ...")
                elif zeidenfonc24 == '9':
                    subprocess.run(["python", "tools/instagram_scraper.py"])
                    input("Press Enter to return to the OSINT screen ...")
                elif zeidenfonc24 == '10':
                    zeidenfonc1()
                    zeidenfonc4()
                    break
                else:
                    print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid choice, please try again."))
        elif zeidenfonc23 == '2':
            zeidenfonc1()
            zeidenfonc4()
            zeidenfonc13()
            input("Press Enter to return to the main menu...")
        elif zeidenfonc23 == '3':
            print(Colorate.Horizontal(Colors.red_to_yellow, "Goodbye!"))
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid choice, please try again."))

if __name__ == "__main__":
    zeidenfonc22()
