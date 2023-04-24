# javino - Javino (http://javino.sf.net)

## DESCRIPTION
A library to supports a robotic-agent platform that uses Raspberry+Arduino boards and Jason Framework.

    javino [TYPE] [PORT] [MSG]

[TYPE] 

+ listen  -- wait an answer from Arduino

+ request -- send a request to Arduino, wait answer 

+ command -- send a command to Arduino, without wait answer

[PORT]

+ Set communication serial port, example: 	 
        /dev/ttyACM0

[MSG] 

+   Message for Arduino-side, example: 	 
        "Hello Arduino!"

## EXAMPLE
+ javino command /dev/ttyACMO ledOn

    Sends <ledOn> command to the ATMEGA microcontroller to run at the actuator.

+ javino request /dev/ttyACM0 getPercepts

    Sends a request <getPercept> to the ATMEGA microcontroller to gather perceptions of the sensors.

## COPYRIGHT

N. M. Lazarin e C. E. Pantoja, “A robotic-agent platform for embedding software agents using raspberry pi and arduino boards”, in Proceedings of 9th Software Agents, Environments and Applications School (WESAAC 2015), Niteroi: UFF, 2015, p. 13–20. [Online]. Available at: https://www.researchgate.net/publication/277403727_A_Robotic-agent_Platform_for_Embedding_Software_Agents_Using_Raspberry_Pi_and_Arduino_Boards

