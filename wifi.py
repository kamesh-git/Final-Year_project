import pywifi
from pywifi import const

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    
    profile = pywifi.Profile()
    profile.ssid = ssid
    profile.auth = const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = password
    
    iface.remove_all_network_profiles()
    tmp_profile = iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    
    for i in range(10000): 
        if iface.status() == const.IFACE_CONNECTED:
            print(f"{i} Connected")
            break
    print('disconnected')
    

# Replace 'YOUR_SSID' and 'YOUR_PASSWORD' with your actual SSID and password
connect_to_wifi('JioFiber-Ec5gb', input("Password:"))
