# ChargingZone - PLC Simulation Using Raspberry Pi 4

**ChargingZone** is a Raspberry Pi-based demonstration of **Powerline Communication (PLC)**, where a user connects to a custom Wi-Fi network and is redirected to a local web page hosted on the Pi. This project simulates PLC environments—showing how communication can occur over existing power lines using a local access point.


## Overview
This setup simulates a smart charging station (like a power outlet) where a user connects to the electrical socket, then they'll automatically connect to the Wi-Fi. This project showcases how PLC network works.

## Concept Behind PLC Demonstration
In real Powerline Communication (PLC), data is sent through electrical wiring. While this project doesn't implement true electrical signal modulation, it demonstrates the concept by mimicking a PLC-based system's behavior:
- A Raspberry Pi acts as the device receiving data over the "powerline."
- A Wi-Fi Access Point (ChargingZone) is the interface users connect to.
- A captive portal displays a page hosted locally, which could be thought of as "transmitted" over the power line.

##  Features
- Raspberry Pi 4 configured as a Wi-Fi Access Point
- Local web server using Python
- Automatic redirection (captive portal) upon connection
- No internet required

## Hardware Used
- Raspberry Pi 4 (8 GB)
- microSD card (16 GB+)
- Power adapter
- USB Detector

## Software & Tools
- Raspberry Pi OS 32bit
- `hostapd` – to create the Wi-Fi access point
- `dnsmasq` – to handle DNS and DHCP
- Python 3 – for the local HTTP server
- Basic HTML file `index.html` for the captive portal
