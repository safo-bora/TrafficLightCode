## TrafficLightCode
(2013 year) - Build Status from Jenkins on Traffic Light

![Alt text](/img/IMG_2866.JPG?raw=true "TL1")

## Components:

MP710 controller (16-channel load control device) 
Official page "Master Kit": http://www.masterkit.ru/main/set.php?code_id=573112

Relay MP701 (Actuator, Relay unit for 4 channels). 
Official page "Master Kit": http://www.masterkit.ru/main/set.php?code_id=573715

12V Power Supply

Cable with a regulator for 220v

Cable PVS 2х0.75mm (10 meters)

USB Extension Cable

## Command line color changing example (Windows):


Turn ON green:
{project path}\MP710.exe CMD=100 PRG=15 PORT11=128:NC PORT12=0:NC PORT13=0:NC

Turn ON yellow:
{project path}\MP710.exe CMD=100 PRG=15 PORT11=0:NC PORT12=128:NC PORT13=0:NC

Turn ON red:
{project path}\MP710.exe CMD=100 PRG=15 PORT11=0:NC PORT12=0:NC PORT13=128:NC

Turn OFF all:
{project path}\MP710.exe CMD=100 PRG=15 PORT11=0:NC PORT12=0:NC PORT13=0:NC

![Alt text](/img/IMAG5268.jpg?raw=true "TL2")
