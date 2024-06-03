
# Javino APT package

|![javinoWithArduinoBoard](https://github.com/chon-group/dpkg-javino/assets/32855001/60041231-2a59-425e-97f1-f7cbe37f4b3b)|
|:--:|
|Meta package for Debian, Ubuntu, Mint, and derivatives that provides the [Javino](https://github.com/chon-group/Javino), a message's error check protocol for communication over a serial channel. This repository provides the Javino-CLI (Command Line Interface) for High level side.|


## Others Javino options:
|                             |High Level|Low Level|
|----------------------------:|:--------:|:-------:|
|__For programming languages__|||
|_C_|-|[javinoCLibrary](https://github.com/bptfreitas/JavinoCLibrary)|
|_Java_|[Javino](https://github.com/chon-group/Javino)|-|
|_Python_|-|[javino2Python](https://github.com/chon-group/javino2python)|
|__Libraries for IoT Boards__|-|-|
|_Arduino_|-|[javino2Arduino](https://github.com/chon-group/javino2arduino)|
|__Applications__|||
|_Linux Command Line Interface_|___This Repository___|-|

There are some libraries that use the serial port to deal with one-sided messages. However, these libraries just provide message treatment for one platform side, leaving the other side to the programmer.
The Javino aims to fill this gap because it offers a double-sided communication that provides a higher level of correctness in message exchange.

For this reason, every message is composed of a preamble, a field size and the message content. The preamble is a field composed of four hexadecimal characters that are used to identify the beginning of a message sent by an agent. The field size is composed of two hexadecimal characters that are used to calculate the message extension. Finally, the last field is the message content, up to 255 bytes. The preamble and the field size are used together to avoid errors in the event of a loss of information during the message transmission. For the sake of practice, Javino automatically mounts the message.

![Javino Message Format](https://a.fsdn.com/con/app/proj/javino/screenshots/The-Javino-message-format-ccb5d9ee.png)

When a message is sent, the Javino library starts to listen on the serial port for arriving char-to-char messages. If there is any information arriving, the Javino stores this character, analyzing if it is part of the expected preamble. So, this process is repeated until the message has been completely received. 

Once the preamble is not confirmed, the Javino discards all information received until it finds a valid preamble. Otherwise, the Javino verifies the field size value to identify the message length. 
This process avoids error insertions and defines where a message starts
and ends. 

## How to install?

In a terminal, execute the steps described below:

```console
echo "deb [trusted=yes] http://packages.chon.group/ chonos main" | sudo tee /etc/apt/sources.list.d/chonos.list
sudo apt update
sudo apt install javino
```

## COPYRIGHT
<a rel="license" href="http://creativecommons.org/licenses/by/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by/4.0/88x31.png" /></a><br />Javino is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>. The licensor cannot revoke these freedoms as long as you follow the license terms:

* __Attribution__ — You must give __appropriate credit__ like below:

N. M. Lazarin e C. E. Pantoja, “A robotic-agent platform for embedding software agents using raspberry pi and arduino boards”, _in_ __Proceedings of 9th Software Agents, Environments and Applications School (WESAAC 2015)__, Niteroi: UFF, 2015, p. 13–20. Available at: [http://www2.ic.uff.br/~wesaac2015/Proceedings-WESAAC-2015.pdf](https://www.researchgate.net/publication/277403727_A_Robotic-agent_Platform_for_Embedding_Software_Agents_Using_Raspberry_Pi_and_Arduino_Boards)

<details>
<summary> Bibtex citation format</summary>

```
@inproceedings{chonOS,
 author = {Nilson Lazarin and Carlos Pantoja and José Viterbo},
 title = { Towards a Toolkit for Teaching AI Supported by Robotic-agents: Proposal and First Impressions},
 booktitle = {Anais do XXXI Workshop sobre Educação em Computação},
 location = {João Pessoa/PB},
 year = {2023},
 keywords = {},
 issn = {2595-6175},
 pages = {20--29},
 publisher = {SBC},
 address = {Porto Alegre, RS, Brasil},
 doi = {10.5753/wei.2023.229753},
 url = {https://sol.sbc.org.br/index.php/wei/article/view/24887}
}

```
</details>
