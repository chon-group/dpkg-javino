# javino - Javino (http://javino.sf.net)

## DESCRIPTION
A double-side library to support serial communication between low-level languages and Java language. It uses Raspberry+Arduino boards and Jason Framework.

    javino [PORT]
        javino@[PORT]$ [TYPE] [MSG]

[TYPE] 

+ listen  -- waits for an answer from Arduino

+ request -- sends a request to Arduino and waits for an answer 

+ command -- sends a command to Arduino but does not wait for an answer

[PORT] - Sets the communication serial port.

[MSG] - The Message for the Arduino-side.

## EXAMPLE
Sending the <ledOn> command to the ATMEGA microcontroller to activate an actuator.
```console
user@machine:~$ javino /dev/ttyACM0 
[JAVINO] Using version stable 1.6.0 (jSerialComm)
javino@ttyACM0$ command ledOn
javino@ttyACM0$ exit
```

Sends a request <getPercept> to the ATMEGA microcontroller to gather perceptions from sensors.
```console
user@machine:~$ javino /dev/ttyACM0 
[JAVINO] Using version stable 1.6.0 (jSerialComm)
javino@ttyACM0$ request getPercepts
resourceName(myArduino);ledStatus(off);port(ttyACM0,on);
javino@ttyACM0$ exit
```

## COPYRIGHT
N. M. Lazarin e C. E. Pantoja, “A robotic-agent platform for embedding software agents using raspberry pi and arduino boards”, in Proceedings of 9th Software Agents, Environments and Applications School (WESAAC 2015), Niteroi: UFF, 2015, p. 13–20. [Online]. Available at: https://www.researchgate.net/publication/277403727_A_Robotic-agent_Platform_for_Embedding_Software_Agents_Using_Raspberry_Pi_and_Arduino_Boards

