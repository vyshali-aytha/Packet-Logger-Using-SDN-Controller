# SDN Packet Logger using POX Controller
# This controller logs packets received from the switch
# and forwards them using a simple OpenFlow action.

from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.packet import ethernet, ipv4

# Create logger object
log = core.getLogger()


def _handle_PacketIn(event):
    """
    Handles PacketIn events from the OpenFlow switch.
    Logs packet details and forwards the packet.
    """

    packet = event.parsed

    # Ignore incomplete packets
    if not packet.parsed:
        return

    # Log source and destination MAC addresses
    log.info("Packet received: %s -> %s", packet.src, packet.dst)

    # Detect ARP packets
    if packet.type == ethernet.ARP_TYPE:
        log.info("ARP packet detected")

    # Detect IPv4 packets
    ip = packet.find('ipv4')
    if ip:
        log.info("IP Packet: %s -> %s", ip.srcip, ip.dstip)

    # Forward packet to all ports (flood)
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=of.OFPP_FLOOD))
    event.connection.send(msg)


def launch():
    """
    Starts the controller and listens for PacketIn events.
    """
    log.info("Packet Logger Controller Started")
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
