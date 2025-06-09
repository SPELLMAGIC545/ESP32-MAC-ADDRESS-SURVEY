import network

# Create interdace about stationmode
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)

# Get MacAddress
mac = sta_if.config('mac')
print('MAC Address:', ':'.join('%02x' % b for b in mac))
