def ip_para_inteiro(ip):
    partes = ip.split(".")
    return (int(partes[0]) << 24) | (int(partes[1]) << 16) | (int(partes[2]) << 8) | int(partes[3])


def inteiro_para_ip(valor):
    return f"{(valor >> 24) & 255}.{(valor >> 16) & 255}.{(valor >> 8) & 255}.{valor & 255}"


def calcular_rede(ip_int, mascara):
    mask = (0xFFFFFFFF << (32 - mascara)) & 0xFFFFFFFF
    return ip_int & mask


def calcular_broadcast(rede_int, mascara):
    hosts = (1 << (32 - mascara)) - 1
    return rede_int | hosts


def main():
    entrada = input("Digite o IP no formato IP/MÁSCARA (ex: 192.168.248.250/24): ")

    ip_str, mascara_str = entrada.split("/")
    mascara = int(mascara_str)

    ip_int = ip_para_inteiro(ip_str)
    rede_int = calcular_rede(ip_int, mascara)
    broadcast_int = calcular_broadcast(rede_int, mascara)

    if mascara < 31:
        primeiro_host = rede_int + 1
        ultimo_host = broadcast_int - 1
    else:
        primeiro_host = rede_int
        ultimo_host = broadcast_int

    print("\nResultado:")
    print(f"Rede: {inteiro_para_ip(rede_int)}")
    print(f"Broadcast: {inteiro_para_ip(broadcast_int)}")
    print(f"Hosts: de {inteiro_para_ip(primeiro_host)} a {inteiro_para_ip(ultimo_host)}")


if __name__ == "__main__":
    main()
