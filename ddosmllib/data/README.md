# Proyecto de título - ML Training

## Sets de Datos de Ciberseguridad

Los sets de datos disponibles se encuentran en la librería interna `ddosmllib/data`. A continuación, se detallan los archivos CSV disponibles en cada conjunto de datos, junto con una breve descripción de su contenido.

### CIC-DDoS2019

Este conjunto de datos contiene archivos CSV que representan diferentes tipos de ataques DDoS. Cada archivo corresponde a un tipo específico de ataque y contiene características extraídas del tráfico de red. Para más información, visite [CIC DDoS 2019 Dataset](https://www.unb.ca/cic/datasets/ddos-2019.html).

#### CIC-DDoS2019/01-12

Este subconjunto incluye archivos CSV con datos de ataques DDoS, proporcionando información útil para la detección de anomalías y la investigación en ciberseguridad:

| Nombre          | Descripción                                              | Listado para acceder                       |
| --------------- | -------------------------------------------------------- | ------------------------------------------ |
| `DrDos_DNS`     | Tráfico de ataques DrDoS utilizando el protocolo DNS     | `'cic-ddos2019', '01-12', 'DrDos_DNS'`     |
| `DrDos_LDAP`    | Tráfico de ataques DrDoS utilizando el protocolo LDAP    | `'cic-ddos2019', '01-12', 'DrDos_LDAP'`    |
| `DrDos_MSSQL`   | Tráfico de ataques DrDoS utilizando el protocolo MSSQL   | `'cic-ddos2019', '01-12', 'DrDos_MSSQL'`   |
| `DrDos_NetBIOS` | Tráfico de ataques DrDoS utilizando el protocolo NetBIOS | `'cic-ddos2019', '01-12', 'DrDos_NetBIOS'` |
| `DrDos_NTP`     | Tráfico de ataques DrDoS utilizando el protocolo NTP     | `'cic-ddos2019', '01-12', 'DrDos_NTP'`     |
| `DrDos_SNMP`    | Tráfico de ataques DrDoS utilizando el protocolo SNMP    | `'cic-ddos2019', '01-12', 'DrDos_SNMP'`    |
| `DrDos_SSDP`    | Tráfico de ataques DrDoS utilizando el protocolo SSDP    | `'cic-ddos2019', '01-12', 'DrDos_SSDP'`    |
| `DrDos_UDP`     | Tráfico de ataques DrDoS utilizando el protocolo UDP     | `'cic-ddos2019', '01-12', 'DrDos_UDP'`     |
| `Syn`           | Tráfico de ataques SYN Flood                             | `'cic-ddos2019', '01-12', 'Syn'`           |
| `TFTP`          | Tráfico de ataques utilizando el protocolo TFTP          | `'cic-ddos2019', '01-12', 'TFTP'`          |
| `UDPLag`        | Tráfico de ataques UDP-Lag                               | `'cic-ddos2019', '01-12', 'UDPLag'`        |

#### CIC-DDoS2019/03-11

Este subconjunto incluye archivos CSV que representan diferentes tipos de ataques DDoS:

| Nombre    | Descripción                                        | Listado para acceder                 |
| --------- | -------------------------------------------------- | ------------------------------------ |
| `LDAP`    | Tráfico de ataques utilizando el protocolo LDAP    | `'cic-ddos2019', '03-11', 'LDAP'`    |
| `MSSQL`   | Tráfico de ataques utilizando el protocolo MSSQL   | `'cic-ddos2019', '03-11', 'MSSQL'`   |
| `NetBIOS` | Tráfico de ataques utilizando el protocolo NetBIOS | `'cic-ddos2019', '03-11', 'NetBIOS'` |
| `Portmap` | Tráfico de ataques utilizando el protocolo Portmap | `'cic-ddos2019', '03-11', 'Portmap'` |
| `Syn`     | Tráfico de ataques SYN Flood                       | `'cic-ddos2019', '03-11', 'Syn'`     |
| `UDP`     | Tráfico de ataques UDP Flood                       | `'cic-ddos2019', '03-11', 'UDP'`     |
| `UDPLag`  | Tráfico de ataques UDP-Lag                         | `'cic-ddos2019', '03-11', 'UDPLag'`  |

---

### CIC-IDS2017

Este conjunto de datos incluye archivos CSV que representan tráfico de red capturado durante diferentes días y horas laborales, con etiquetas que indican si el tráfico es benigno o malicioso. Para más detalles, consulte [CIC IDS 2017 Dataset](https://www.unb.ca/cic/datasets/ids-2017.html).

#### CIC-IDS2017/MachineLearningCVE

Este subconjunto contiene archivos CSV que representan diferentes tipos de ataques y tráfico de red:

| Nombre                                          | Descripción                                                                                          | Listado para acceder                                                                             |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `Friday-WorkingHours-Afternoon-DDos`            | Tráfico capturado el viernes por la tarde, incluyendo ataques DDoS                                   | `'cic-ids2017', 'MachineLearningCVE', 'Friday-WorkingHours-Afternoon-DDos.pcap_ISCX'`            |
| `Friday-WorkingHours-Afternoon-PortScan`        | Tráfico capturado el viernes por la tarde, incluyendo ataques de escaneo de puertos                  | `'cic-ids2017', 'MachineLearningCVE', 'Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX'`        |
| `Friday-WorkingHours-Morning`                   | Tráfico capturado el viernes por la mañana, principalmente benigno                                   | `'cic-ids2017', 'MachineLearningCVE', 'Friday-WorkingHours-Morning.pcap_ISCX'`                   |
| `Monday-WorkingHours`                           | Tráfico capturado el lunes durante horas laborales, principalmente benigno                           | `'cic-ids2017', 'MachineLearningCVE', 'Monday-WorkingHours.pcap_ISCX'`                           |
| `Thursday-WorkingHours-Afternoon-Infilteration` | Tráfico capturado el jueves por la tarde, incluyendo ataques de infiltración                         | `'cic-ids2017', 'MachineLearningCVE', 'Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX'` |
| `Thursday-WorkingHours-Morning-WebAttacks`      | Tráfico capturado el jueves por la mañana, incluyendo ataques web                                    | `'cic-ids2017', 'MachineLearningCVE', 'Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX'`      |
| `Tuesday-WorkingHours`                          | Tráfico capturado el martes durante horas laborales, incluyendo ataques de fuerza bruta              | `'cic-ids2017', 'MachineLearningCVE', 'Tuesday-WorkingHours.pcap_ISCX'`                          |
| `Wednesday-WorkingHours`                        | Tráfico capturado el miércoles durante horas laborales, incluyendo ataques de denegación de servicio | `'cic-ids2017', 'MachineLearningCVE', 'Wednesday-WorkingHours.pcap_ISCX'`                        |

#### CIC-IDS2017/TrafficLabelling

Este subconjunto contiene archivos CSV que representan diferentes tipos de ataques y tráfico de red:

| Nombre                                          | Descripción                                                                                          | Listado para acceder                                                                           |
| ----------------------------------------------- | ---------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `Friday-WorkingHours-Afternoon-DDos`            | Tráfico capturado el viernes por la tarde, incluyendo ataques DDoS                                   | `'cic-ids2017', 'TrafficLabelling', 'Friday-WorkingHours-Afternoon-DDos.pcap_ISCX'`            |
| `Friday-WorkingHours-Afternoon-PortScan`        | Tráfico capturado el viernes por la tarde, incluyendo ataques de escaneo de puertos                  | `'cic-ids2017', 'TrafficLabelling', 'Friday-WorkingHours-Afternoon-PortScan.pcap_ISCX'`        |
| `Friday-WorkingHours-Morning`                   | Tráfico capturado el viernes por la mañana, principalmente benigno                                   | `'cic-ids2017', 'TrafficLabelling', 'Friday-WorkingHours-Morning.pcap_ISCX'`                   |
| `Monday-WorkingHours`                           | Tráfico capturado el lunes durante horas laborales, principalmente benigno                           | `'cic-ids2017', 'TrafficLabelling', 'Monday-WorkingHours.pcap_ISCX'`                           |
| `Thursday-WorkingHours-Afternoon-Infilteration` | Tráfico capturado el jueves por la tarde, incluyendo ataques de infiltración                         | `'cic-ids2017', 'TrafficLabelling', 'Thursday-WorkingHours-Afternoon-Infilteration.pcap_ISCX'` |
| `Thursday-WorkingHours-Morning-WebAttacks`      | Tráfico capturado el jueves por la mañana, incluyendo ataques web                                    | `'cic-ids2017', 'TrafficLabelling', 'Thursday-WorkingHours-Morning-WebAttacks.pcap_ISCX'`      |
| `Tuesday-WorkingHours`                          | Tráfico capturado el martes durante horas laborales, incluyendo ataques de fuerza bruta              | `'cic-ids2017', 'TrafficLabelling', 'Tuesday-WorkingHours.pcap_ISCX'`                          |
| `Wednesday-WorkingHours`                        | Tráfico capturado el miércoles durante horas laborales, incluyendo ataques de denegación de servicio | `'cic-ids2017', 'TrafficLabelling', 'Wednesday-WorkingHours.pcap_ISCX'`                        |

---

### N-BaIoT

Este conjunto de datos proviene del proyecto N-BaIoT, enfocado en la detección de ataques a dispositivos de Internet de las Cosas (IoT). Contiene archivos CSV que representan tráfico de red de dispositivos IoT bajo condiciones benignas y durante diferentes tipos de ataques de botnets como Mirai y BASHLITE. Para más información, visite [N-BaIoT Dataset en Kaggle](https://www.kaggle.com/datasets/mkashifn/nbaiot-dataset/data).

#### N-BaIoT/IoT DDoS Attacks

Este subconjunto contiene archivos CSV que representan diferentes tipos de ataques y tráfico de red:

| Nombre           | Descripción                                             | Listado para acceder |
| ---------------- | ------------------------------------------------------- | -------------------- |
| `benign`         | Tráfico benigno de dispositivos IoT                     | `'nbaiot', '#.benign'`           |
| `gafgyt/combo`   | Tráfico de ataques Gafgyt utilizando la técnica combo   | `'nbaiot', '#.gafgyt.combo'`     |
| `gafgyt/junk`    | Tráfico de ataques Gafgyt utilizando la técnica junk    | `'nbaiot', '#.gafgyt.junk'`      |
| `gafgyt/scan`    | Tráfico de ataques Gafgyt utilizando la técnica scan    | `'nbaiot', '#.gafgyt.scan'`      |
| `gafgyt/tcp`     | Tráfico de ataques Gafgyt utilizando el protocolo TCP   | `'nbaiot', '#.gafgyt.tcp'`       |
| `gafgyt/udp`     | Tráfico de ataques Gafgyt utilizando el protocolo UDP   | `'nbaiot', '#.gafgyt.udp'`       |
| `mirai/ack`      | Tráfico de ataques Mirai utilizando paquetes ACK        | `'nbaiot', '#.mirai.ack'`        |
| `mirai/scan`     | Tráfico de ataques Mirai utilizando técnicas de escaneo | `'nbaiot', '#.mirai.scan'`       |
| `mirai/syn`      | Tráfico de ataques Mirai utilizando paquetes SYN        | `'nbaiot', '#.mirai.syn'`        |
| `mirai/udp`      | Tráfico de ataques Mirai utilizando el protocolo UDP    | `'nbaiot', '#.mirai.udp'`        |
| `mirai/udpplain` | Tráfico de ataques Mirai utilizando paquetes UDP Plain  | `'nbaiot', '#.mirai.udpplain'`   |

#### N-BaIoT/Otros

| Nombre         | Descripción                     | Listado para acceder       |
| -------------- | ------------------------------- | -------------------------- |
| `data_summary` | Resumen de los datos            | `'nbaiot', 'data_summary'` |
| `device_info`  | Información de los dispositivos | `'nbaiot', 'device_info'`  |
| `features`     | Características de los datos    | `'nbaiot', 'features'`     |


