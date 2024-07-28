# %%
import subprocess
import time

def pair_with_speaker(speaker_mac_address = '63:7C:2D:10:3C:E1'):
    try:
        

        print("Pairing with speaker...")
        # Run bluetoothctl to pair with the speaker
        subprocess.run(['bluetoothctl'], input="scan on", check=True, text=True)
        for i in ['trust','pair','connect']:
            bluetoothctl_input = f"{i} {speaker_mac_address}"
            subprocess.run(['bluetoothctl'], input=bluetoothctl_input, check=True, text=True)
            # time.sleep(10)
        print("Paired successfully.")
        time.sleep(15)

        return True
    except subprocess.CalledProcessError as e:
        print("Error:", e)
    
    print("Pairing failed.")
    return False


if __name__ == "__main__":
    speaker_mac_address = '63:7C:2D:10:3C:E1'  # Replace with your speaker's MAC address
    pair_with_speaker(speaker_mac_address)



