:INPUT ACCEPT[0:0]

	:FORWARD ACCEPT [0:0]

	:OUTPUT ACCEPT [0:0]

	

	

	-I INPUT  1 -m state --state RELATED,ESTABLISHED -j ACCEPT

	-I OUTPUT 1 -m state --state RELATED,ESTABLISHED -j ACCEPT

	

	

	-A INPUT -i lo -j DROP

	-A OUTPUT -o lo -j DROP

	

	

	

	-A OUTPUT –o eth0 -p icmp -j DROP

	

	

	-A OUTPUT –o eth0 -p udp --dport 123 --sport 123 -j DROP

	

	

	-A OUTPUT -o eth0 -p tcp -m tcp --dport 80 -m state --state NEW -j DROP

	-A OUTPUT -o eth0 -p tcp -m tcp --dport 443 -m state --state NEW -j DROP

	

	iptables -A INPUT -p tcp -m time --timestart 00:01:00 --timestop 00:00:30 -j DROP

	iptables -A INPUT -p udp -m time --timestart 00:01:00 --timestop 00:00:30 -j DROP

	

	-A OUTPUT -o eth0 -p icmp -j DROP

	

	COMMIT


