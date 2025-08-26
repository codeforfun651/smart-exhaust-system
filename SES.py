from machine import Pin, ADC
import time

mq_pin = ADC(Pin(34))  
mq_pin.atten(ADC.ATTN_11DB) 

relay_pin = Pin(13, Pin.OUT)
GAS_THRESHOLD = 2000


while True:
    gas_level = mq_pin.read() 
    print("Gas Level:", gas_level)  

    # Check if the gas level exceeds the threshold
    if gas_level > GAS_THRESHOLD:
        print("Gas Detected! Turning on the relay.")
        relay_pin.off()  # Activate the relay
    else:
        print("No Gas Detected. Turning off the relay.")
        relay_pin.on()  # Deactivate the relay

    time.sleep(1)  