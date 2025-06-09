import network

# Creaate interface about access point mode
ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)

# Get mac address
mac = ap_if.config('mac')
print('AP MAC Address:', ':'.join('%02x' % b for b in mac))
