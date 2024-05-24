""" 
Copyright Production 3000

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License. 
"""

import socket
import sys


# Create a new socket, define the port on which to listen
udpPort = 4211
sockListen = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockListen.bind(("0.0.0.0", udpPort))
print(f"Listening on port {udpPort}...")


while True:
    data, addr = sockListen.recvfrom(1024)
    packet_size = sys.getsizeof(data)
    message = data.decode('utf-8')

    if message == "DISERV":
        # Response
        response = "RESERV"

        # Send the response to the original sender
        sockRespond = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockRespond.sendto(response.encode('utf-8'), (addr[0], udpPort))
        # Close the response socket
        sockRespond.close()

        print(f"DISERV received, RESERV sent")

    else:
        print(f"{message}")
