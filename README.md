# ha_frigate_monitor
Keeps track of 2 frigate instances running HA via keepalived and triggers some LEDs to show state of device as well as the primary/ secondary nodes. Expected to be running on Seeed Odyssey X86J4105864 and ubuntu 20.04.
Runs on each individual device and displays state of that device on the elds

Notes for me personally.
LEDs are running 220ohm resistors
The GPIO addressing changes based off of the device AND OS version