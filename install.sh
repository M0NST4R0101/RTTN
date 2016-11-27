#!/bin/bash

sudo rm -rf /etc/tor/torrc
sudo mv torrc /etc/tor/torrc
sudo chmod 777 RTTN.py
sudo cp RTTN.py /usr/bin/RTTN
echo "INSTALL WITH SUCESS, USAGE: RTTN --help"
