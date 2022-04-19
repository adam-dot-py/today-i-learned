# Resetting SSH keygen

It is sometimes necessary to clear the SSH key on a machine, especially after reinstalling a previous Raspberry Pi setup. This is because when the machine is asked to connect to the Pi, it sees it as a different machine with a different SSH Key, which does not match the one it remembers for the IP address we are using.

To reset the keygen, use `ssh-keygen -R [raspberry pi ip address]`
