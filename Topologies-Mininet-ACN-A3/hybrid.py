from mininet.topo import Topo

class MyTopos(Topo):

        def build(self):
                host_04 = self.addHost('h1')
                host_08 = self.addHost('h2')
                host_12 = self.addHost('h3')
                host_51 = self.addHost('h4')
                sw_04 = self.addSwitch('s1')
                sw_08 = self.addSwitch('s2')
                sw_12 = self.addSwitch('s3')
                sw_51 = self.addSwitch('s4')
                host_14 = self.addHost('h5')
                host_18 = self.addHost('h6')
                host_22 = self.addHost('h7')
                host_61 = self.addHost('h8')
                sw_02 = self.addSwitch('s6')

                self.addLink(host_04, sw_04)
                self.addLink(sw_04, sw_08)
                self.addLink(sw_08, host_08)
                self.addLink(sw_08, sw_12)
                self.addLink(sw_12, host_12)
                self.addLink(sw_12, sw_51)
                self.addLink(sw_51, host_51)

                self.addLink(sw_02, host_14)
                self.addLink(sw_02, host_18)
                self.addLink(sw_02, host_22)
                self.addLink(sw_02, host_61)

                self.addLink(sw_02, sw_51)

topos = {'hybrid_topo': ( lambda: MyTopos() ) }