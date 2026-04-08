SDN Packet Logger using POX and Mininet
Project Description

This project implements a simple Software Defined Networking (SDN) packet monitoring system using a POX controller and Mininet. The controller handles PacketIn events from the OpenFlow switch, logs packet information, and applies basic OpenFlow match–action rules for forwarding.

Network traffic is generated using ping and iperf, and packets are analyzed using Wireshark to observe ICMP and TCP communication.

Problem Statement

Design and implement an SDN-based packet monitoring system using Mininet and an OpenFlow controller (POX). The controller should capture packets, log relevant information, and demonstrate controller–switch interaction using match–action flow rules.

Technologies Used
Mininet
POX SDN Controller
Open vSwitch
Wireshark
iperf
Python
Network Topology

The Mininet topology used consists of:

1 OpenFlow switch (s1)
3 hosts (h1, h2, h3)
1 SDN controller (POX)
h1 ----\
        s1 ---- Controller
h2 ----/
       \
        h3
Setup and Execution Steps
1. Start the POX Controller
cd ~/sdn_project/pox
python3 pox.py ext.packet_logger
2. Start Mininet
sudo mn -c
sudo mn --topo single,3 --controller remote
3. Test Network Connectivity
pingall
4. Generate ICMP Traffic
h1 ping h2
5. Generate TCP Traffic
h1 iperf -s &
h2 iperf -c h1
6. View Flow Table
sudo ovs-ofctl dump-flows s1
7. Capture Packets with Wireshark

Start Wireshark and capture packets on interface:

s1-eth1
Expected Output
Hosts communicate successfully (0% packet loss)
Packet logs appear in the controller terminal
Wireshark captures ICMP and TCP packets
iperf shows throughput between hosts
Flow table entries are visible in the switch
Proof of Execution

Screenshots included in the repository:

Controller running
Mininet topology
Ping test results
Controller packet logs
Wireshark ICMP packets
Wireshark TCP packets
iperf throughput
Flow table entries
Conclusion

This project demonstrates controller–switch interaction in SDN using OpenFlow. The POX controller captures packet events, applies forwarding rules, and enables monitoring of network traffic through Mininet and Wireshark.
