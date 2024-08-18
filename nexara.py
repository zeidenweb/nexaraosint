import os
from pystyle import Colors, Colorate

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def afficher_humouristique():
    humouristique_titre = r"""
         _nnnn_                      
        dGGGGMMb     ,"""""""""""""""""".
       @p~qp~~qMb    | Get Doxxed Nigga |
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
    print(Colorate.Horizontal(Colors.red_to_yellow, humouristique_titre))
    input("Press Enter...")
    clear_screen()  # Clear the screen after pressing Enter

def afficher_titre():
    titre = """
       ______    _     _             
      |___  /   (_)   | |            
         / / ___ _  __| | ___ _ __   
        / / / _ \ |/ _` |/ _ \ '_ \  
       / /_|  __/ | (_| |  __/ | | | 
      /_____\___|_|\__,_|\___|_| |_| 
    """
    print(Colorate.Horizontal(Colors.red_to_yellow, titre))

    welcome_message = "Welcome to Nexara the OSINT directory V2"
    choose_option = "Choose an option :"

    print("\n" + welcome_message.center(os.get_terminal_size().columns))
    print(choose_option.center(os.get_terminal_size().columns))

def menu_principal():
    options = [
        "1. OSINT",
        "2. Tool info",
        "3. Leave"
    ]

    columns = os.get_terminal_size().columns
    formatted_options = (
        options[0].ljust(columns // 3) + 
        options[1].center(columns // 3) + 
        options[2].rjust(columns // 3)
    )

    print("\n" + formatted_options + "\n")

def menu_osint():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Choose an option :"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "1. IP Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "2. Mail Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "3. Username Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "4. Image Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "5. Number Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "6. Free DB"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "7. Google Advanced"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "8. Back to main menu"))

def tool_info():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Tool info:"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "Created by Zeiden"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "Created on 01/08/24 / update on 18/08/24"))

def ip_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "IP lookup & location : https://www.iplocation.net/"))

def mail_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Mail lookup : https://thatsthem.com/reverse-email-lookup"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://epieos.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://haveibeenpwned.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://leakcheck.io/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://dehashed.com/"))

def username_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Username lookup : https://whatsmyname.app/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://instantusername.com/"))

def image_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Image lookup : https://tineye.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://pimeyes.com/fr"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://facecheck.id/fr"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://lens.google/intl/fr/"))

def numero_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Numéro lookup : https://www.capeutservir.com/telephonie/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://www.emobiletracker.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://www.pagesjaunes.fr/annuaireinverse"))

def google_advanced():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Do advanced research on Google : https://www.google.com/advanced_search"))

def free_db():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Free DB ---) https://discord.com/invite/lookup"))

def main():
    afficher_humouristique()  # Affiche l'humour uniquement au démarrage
    afficher_titre()  # Affiche le titre principal
    while True:
        menu_principal()
        choix = input("Enter your choice : ")

        if choix == '1':
            while True:
                clear_screen()
                afficher_titre()
                menu_osint()
                sous_choix = input("Enter your choice : ")

                if sous_choix == '1':
                    clear_screen()
                    afficher_titre()
                    ip_lookup()
                    input("Press Enter to return to the OSINT screen ...")
                elif sous_choix == '2':
                    clear_screen()
                    afficher_titre()
                    mail_lookup()
                    input("Press Enter to return to the OSINT screen ...")
                elif sous_choix == '3':
                    clear_screen()
                    afficher_titre()
                    username_lookup()
                    input("Press Enter to return to the OSINT screen ...")
                elif sous_choix == '4':
                    clear_screen()
                    afficher_titre()
                    image_lookup()
                    input("Press Enter to return to the OSINT screen ...")
                elif sous_choix == '5':
                    clear_screen()
                    afficher_titre()
                    numero_lookup()
                    input("Press Enter to return to the OSINT screen ...")
                elif sous_choix == '6':
                    clear_screen()
                    afficher_titre()
                    free_db()
                    input("Press Enter to return to the OSINT screen ...")
                elif sous_choix == '7':
                    clear_screen()
                    afficher_titre()
                    google_advanced()
                    input("Press Enter to return to the OSINT screen ...")
                elif sous_choix == '8':
                    clear_screen()
                    afficher_titre()
                    break
                else:
                    print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid choice, please try again."))
        elif choix == '2':
            clear_screen()
            afficher_titre()
            tool_info()
            input("Press Enter to return to the main menu...")
        elif choix == '3':
            print(Colorate.Horizontal(Colors.red_to_yellow, "Goodbye!"))
            break
        else:
            print(Colorate.Horizontal(Colors.red_to_yellow, "Invalid choice, please try again."))

if __name__ == "__main__":
    main()
