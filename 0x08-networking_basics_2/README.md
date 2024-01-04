This is ALX-SE program, 0x08-networking_basics_2 project where I:

1- Write a Bash script that configures an Ubuntu server with the below requirements.
   with these requirements:
	localhost resolves to 127.0.0.2
	facebook.com resolves to 8.8.8.8.
	Usage: ./0-change_your_home_IP

2- Write a Bash script that displays all active IPv4 IPs on the machine it’s executed on.
	Usage: ./1-show_attached_IPs

3- Write a Bash script that listens on port 98 on localhost.
	Usage: 
		execute this in one terminal be it (termainl 0)
		>"sudo ./100-port_listening_on_localhost"
		and execute this in another terminal be it (terminal 1) i
		>"telnet localhost 98
		 Trying 127.0.0.2...
		 Connected to localhost.
		 Escape character is '^]'.
		 Hello world
		 test"
		You should recieve the text on the other terminal (terimnal 0)
		>sudo ./100-port_listening_on_localhost
		 Hello world
		 test
