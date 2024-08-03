import os
from pystyle import Colors, Colorate

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

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

    welcome_message = "Welcome to Nexara the osint directory"
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
    print(Colorate.Horizontal(Colors.blue_to_purple, "1. IP LOOKUP"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "2. Mail Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "3. Username Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "4. Image Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "5. Number Lookup"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "6. Free DB"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "7. Back to main menu"))

def tool_info():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Tool info:"))
    print(Colorate.Horizontal(Colors.blue_to_purple, "created by zeiden "))
    print(Colorate.Horizontal(Colors.blue_to_purple, "created on 01/08/24"))

def ip_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "IP lookup & location : https://www.iplocation.net/ "))

def mail_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Mail lookup : https://thatsthem.com/reverse-email-lookup"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://epieos.com/"))

def username_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Username lookup : https://whatsmyname.app/"))

def image_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Image lookup : https://tineye.com/"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "https://pimeyes.com/en"))

def numero_lookup():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Numéro lookup : https://www.capeutservir.com/telephonie/"))

def free_db():
    print(Colorate.Horizontal(Colors.red_to_yellow, "Free DB ---) discord.gg/snusbase"))

def main():
    clear_screen()
    afficher_titre()
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
