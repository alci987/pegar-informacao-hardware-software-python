#  pegar informacões de hardware e software do Sistem Operacional
## _Script feito em python para pegar informações de hardware e software do sistema operacional. Serão instalados os seguintes pacotes:_

| Pacote | Descrição |
| ------ | ------ |
| psutil |  (python system and process utilities) é uma bilioteca para extrair informações de processos e de sistemas rodando no SO (memória, disco, rede, etc) ```pip install psutil ``` |
| gputil | é um módulo Python para obter o status da GPU das GPUs NVIDA usando nvidia-smi. GPUtil localiza todas as GPUs no computador, determina sua disponibilidade e retorna uma lista ordenada de GPUs disponíveis  ```pip install gputil ``` |
| tabulate | módulo em python usado para imprimir tabelas ```pip install tabulate ``` |

### A saída será algo como mostrado abaixo

```
======================================== Informações do Sistema ========================================
Sistema: Windows
Usuário: Casa
Release: 10
Versão: 10.0.19041
Arquitetura: AMD64
Processador: Intel64 Family 6 Model 78 Stepping 3, GenuineIntel
======================================== Hora do boot ========================================
Hora do boot: 30/3/2022 7:22:42
Cores físicos: 2
Total de cores: 4
Frequência máxima: 1992.00Mhz
Frequência mínima: 0.00Mhz
Frequência atual: 1992.00Mhz
Uso da CPU por Core:
Core 0: 22.9%
Core 1: 12.5%
Core 2: 6.2%
Core 3: 9.4%
Uso total da CPU: 13.0%
======================================== Informação de memória ========================================
Total: 3.89GB
Disponível: 411.18MB
Usado: 3.49GB
Porcentagem: 89.7%
==================== SWAP ====================
Total: 4.75GB
Livre: 3.20GB
Usedo: 1.55GB
Porcentagem: 32.6%
======================================== Informações de Disco ========================================
Partições e uso:
=== Disco: C:\ ===
  Ponto de montagem: C:\
  Sistema de arquivos: NTFS
  Tamanho total: 237.90GB
  Usedo: 209.14GB
  Livre: 28.76GB
  Porcentagem: 87.9%
=== Disco: D:\ ===
  Ponto de montagem: D:\
  Sistema de arquivos: NTFS
  Tamanho total: 232.88GB
  Usedo: 196.03GB
  Livre: 36.85GB
  Porcentagem: 84.2%
Total lido: 6.17GB
Total escrito: 2.44GB
======================================== Informações de Rede ========================================
=== Interface: Ethernet ===
=== Interface: Ethernet ===
  IP: 169.254.112.190
  Netmask: 255.255.0.0
  Broadcast IP: None
=== Interface: Ethernet ===
=== Interface: Conexão Local* 1 ===
=== Interface: Conexão Local* 1 ===
  IP: 169.254.212.42
  Netmask: 255.255.0.0
  Broadcast IP: None
=== Interface: Conexão Local* 1 ===
=== Interface: Conexão Local* 2 ===
=== Interface: Conexão Local* 2 ===
  IP: 169.254.145.194
  Netmask: 255.255.0.0
  Broadcast IP: None
=== Interface: Conexão Local* 2 ===
=== Interface: Wi-Fi ===
=== Interface: Wi-Fi ===
  IP: 192.168.1.8
  Netmask: 255.255.255.0
  Broadcast IP: None
=== Interface: Wi-Fi ===
=== Interface: Loopback Pseudo-Interface 1 ===
  IP: 127.0.0.1
  Netmask: 255.0.0.0
  Broadcast IP: None
=== Interface: Loopback Pseudo-Interface 1 ===
Total de Bytes enviados: 1.74GB
Total de Bytes recebidos: 140.45MB
======================================== Uso da bateria ========================================
100 %
======================================== Detalhes da GPU ========================================
  id  nome              load    memória livre    memória usada    total de memória    temperatura    uuid
----  ----------------  ------  -------------    -------------    --------------     -------------  ----------------------------------------
   0  GeForce GTX 1050  2.0%    3976.0MB          120.0MB          4096.0MB           52.0 °C        GPU-c9b08d82-f1e2-40b6-fd20-543a4186d6ce


```

