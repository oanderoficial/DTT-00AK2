import os
import platform

class WifiAttackTool:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    GREEN = '\033[92m'
    RESET = '\033[0m'

    def __init__(self):
        self.is_mac = self.is_macos()

    def is_macos(self):
        """Verifica se o sistema operacional é macOS."""
        return platform.system() == "Darwin"

    def scan_wifi_networks(self):
        """Escaneia redes Wi-Fi disponíveis usando 'airport' no macOS."""
        if self.is_mac:
            print(self.GREEN + "Escaneando redes Wi-Fi..." + self.RESET)
            os.system("airport -s")
        else:
            print(self.RED + "Este comando só funciona no macOS." + self.RESET)

    def capture_wifi_traffic(self):
        """Captura tráfego de rede usando tcpdump (alternativa ao airodump-ng)."""
        if self.is_mac:
            interface = input(self.GREEN + "Digite a interface de rede (ex: en0): " + self.RESET)
            print(self.GREEN + f"Iniciando captura de tráfego na interface {interface}..." + self.RESET)
            os.system(f"sudo tcpdump -i {interface} -I -y IEEE802_11_RADIO")
        else:
            print(self.RED + "Este comando só funciona no macOS." + self.RESET)

    def perform_deauthentication_attack(self):
        """Simula um ataque de desautenticação (não suportado nativamente no macOS)."""
        if self.is_mac:
            print(self.RED + "Atenção: Ataques de desautenticação não são suportados nativamente no macOS." + self.RESET)
            print(self.YELLOW + "Você precisará de um adaptador USB Wi-Fi compatível com modo monitor." + self.RESET)
        else:
            print(self.RED + "Este comando só funciona no Linux." + self.RESET)

    def run(self):
        """Menu principal do script."""
        while True:
            print(self.RED + """
                     _..---..__
                   ,'          `-.
                  .'` .          )             DTT-00AK2
                  |     `;.__.._.'               V.1.1
                   \ .`--.(##)(#).    Wi-Fi Analysis Tool for macOS
                    `-->;--' pWq`>              BY:AND3R
                      < <"v\,,,,]
                       `\`^-''''7
                         `~"--^-'
            """ + self.RESET)
            print(self.RED + "1- Escanear redes Wi-Fi disponíveis" + self.RESET)
            print(self.YELLOW + "2- Capturar tráfego de rede (modo monitor)" + self.RESET)
            print(self.RED + "3- Realizar ataque de desautenticação (não suportado no macOS)" + self.RESET)
            print(self.YELLOW + "4- Sair" + self.RESET)
            menu = input(self.RED + "Digite uma opção >> " + self.RESET)

            if menu == "1":
                self.scan_wifi_networks()
            elif menu == "2":
                self.capture_wifi_traffic()
            elif menu == "3":
                self.perform_deauthentication_attack()
            elif menu == "4":
                break
            else:
                print(self.RED + "Opção inválida!" + self.RESET)

if __name__ == "__main__":
    tool = WifiAttackTool()
    tool.run()
