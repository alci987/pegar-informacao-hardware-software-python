import psutil
import platform
from datetime import datetime


def get_size(bytes, suffix="B"):
    """
    Escala os bytes para o formato padrão
    ex:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


print("="*40, "Informações do Sistema", "="*40)
uname = platform.uname()
print(f"Sistema: {uname.system}")
print(f"Usuário: {uname.node}")
print(f"Release: {uname.release}")
print(f"Versão: {uname.version}")
print(f"Arquitetura: {uname.machine}")
print(f"Processador: {uname.processor}")


# Pega o horário do último boot
print("="*40, "Hora do boot", "="*40)
boot_time_timestamp = psutil.boot_time() # recebe no formato timestamps
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"Hora do boot: {bt.day}/{bt.month}/{bt.year} {bt.hour}:{bt.minute}:{bt.second}")


# número de cores
print("Cores físicos:", psutil.cpu_count(logical=False))
print("Total de cores:", psutil.cpu_count(logical=True))
# Frequência da CPU
cpufreq = psutil.cpu_freq()
print(f"Frequência máxima: {cpufreq.max:.2f}Mhz")
print(f"Frequência mínima: {cpufreq.min:.2f}Mhz")
print(f"Frequência atual: {cpufreq.current:.2f}Mhz")
# Uso da CPU
print("Uso da CPU por Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f"Core {i}: {percentage}%")
print(f"Uso total da CPU: {psutil.cpu_percent()}%")

# Informação de memória
print("="*40, "Informação de memória", "="*40)
# pega os detalhes da memória
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Disponível: {get_size(svmem.available)}")
print(f"Usado: {get_size(svmem.used)}")
print(f"Porcentagem: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
# pega os detalhes da memória swap memory details (caso exista)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Livre: {get_size(swap.free)}")
print(f"Usedo: {get_size(swap.used)}")
print(f"Porcentagem: {swap.percent}%")

# Informações do disco
print("="*40, "Informações de Disco", "="*40)
print("Partições e uso:")
# pega todas as partições
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Disco: {partition.device} ===")
    print(f"  Ponto de montagem: {partition.mountpoint}")
    print(f"  Sistema de arquivos: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        # Ese erro pode ser pegado, caso o disco não esteja pronto ou montado
        continue
    print(f"  Tamanho total: {get_size(partition_usage.total)}")
    print(f"  Usedo: {get_size(partition_usage.used)}")
    print(f"  Livre: {get_size(partition_usage.free)}")
    print(f"  Porcentagem: {partition_usage.percent}%")
# pega informações de estatus de IO desde o boot
disk_io = psutil.disk_io_counters()
print(f"Total lido: {get_size(disk_io.read_bytes)}")
print(f"Total escrito: {get_size(disk_io.write_bytes)}")

# Informações de rede
print("="*40, "Informações de Rede", "="*40)
# pega todas as interfaces de rede (virtuais e físicas)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
# pega informações de estatus de IO desde o boot
net_io = psutil.net_io_counters()
print(f"Total de Bytes enviados: {get_size(net_io.bytes_sent)}")
print(f"Total de Bytes recebidos: {get_size(net_io.bytes_recv)}")

# Informações da bateria. (Somente se vc estiver em um notebook)
print("="*40, "Uso da bateria", "="*40)
print(psutil.sensors_battery().percent, "%")

# Informações de GPU
import GPUtil
from tabulate import tabulate
print("="*40, "Detalhes da GPU", "="*40)
gpus = GPUtil.getGPUs()

if(gpus):
    list_gpus = []
    for gpu in gpus:
        # pega o Id da GPU
        gpu_id = gpu.id
        # nome da GPU
        gpu_name = gpu.name
        # pega a porcentage de uso da GPU
        gpu_load = f"{gpu.load * 100}%"
        # pega a memória livre no formato MB
        gpu_free_memory = f"{gpu.memoryFree}MB"
        # pega a memória usada
        gpu_used_memory = f"{gpu.memoryUsed}MB"
        # pega o total de memória
        gpu_total_memory = f"{gpu.memoryTotal}MB"
        # pega a temperatura da GPU em ° Celsius
        gpu_temperature = f"{gpu.temperature} °C"
        gpu_uuid = gpu.uuid
        list_gpus.append((
            gpu_id, gpu_name, gpu_load, gpu_free_memory, gpu_used_memory,
            gpu_total_memory, gpu_temperature, gpu_uuid
        ))

    print(tabulate(list_gpus, headers=("id", "nome", "load", "memória livre", "memória usada", "total de memória",
                                       "temperatura", "uuid")))
else:
    print("Sem uso de GPU!!!")
