# abl-charger
Example project - how to use RS485 on ABL eMH1 EV charger .

Thic code works with ABL eMH1 1W1108 wallbox and any RS485 to USB converter.  

## Hardware connection

There are two types of RS485 connectors depends on eMH version  
- RJ45 (8pins)  
- RJ12 (6pins), use pins 3,4 (A=black, B=brown)

Jumper EN1 must be wired to "enable" charging.

## Software connection
In example program `emh-functional-test.py` specify your USB device. It depends on your OS and type of USB dongle.  

I had to modify minimalmodbus library (https://github.com/pyhys/minimalmodbus), because the header of response message (preambule) it's not ":" as usual, but ">".

And keep in mind that first request on RS485 fails but it wakes up the instrument and next request will be successfull.


# abl-charger
Příklad pro první připojení protokolem RS485 na autonabíječku ABL eMH1.

Program je vyzkoušený na modelu ABL eMH1 1W1108 a více typech RS485 USB konvertoru.  

## Fyzické připojení

Nabíječek eHMx je více typů a vyskytují se dva typy RS485 konektoru
- RJ45 (8pinů)  
- RJ12 (6pinů), použijte 3,4 (A=černý, B=hnědý)

Jumper EN1 musí být propojen, aby šlo spustit nabíjení.

## Použití programu
Funkční prototypový program `emh-functional-test.py` se umí připojit k nabíječce, vyčíst stav a nastavit nabíjecí proud. V programu upravte jméno vašeho USB zařízení. To záleží na operačním systému a typu USB zařízení.  

Přikládám upravenou knihovnu minimalmodbus (https://github.com/pyhys/minimalmodbus), kde bylo nutné upravit hlavičky zpráv. Hlavička odpovědi (preambule) totiž není ":" jak je běžné ale ">".

Upozorňuji na skutečnost, že první dotaz přes RS485 skončí chybou ale tím se probudí rozhraní a následující dotaz je již zpracován úspěšně.







