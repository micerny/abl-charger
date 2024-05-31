# abl-charger
Example project - how to use RS485 on ABL eMH1 EV charger .

Thic code works with ABL eMH1 1W1108 wallbox and any RS485 to USB converter.  

## Hardware connection

There are two types of RS485 connectors depends on eMH version  
- RJ45 (8pins)  
- RJ12 (6pins), use pins 3,4 (A=black, B=brown)

Jumper EN1 must be wired, it's "enable" for charging.

## Software connection
In example program `emh-functional-test.py` specify your USB device. It depends on your OS and type of USB dongle.  

I had to modify minimalmodbus library, because the header of response message (preambule) it's not ":" as usual, but ">".

And keep in mind that first request on RS485 fails but it wakes up the instrument and next request will be successfull.








