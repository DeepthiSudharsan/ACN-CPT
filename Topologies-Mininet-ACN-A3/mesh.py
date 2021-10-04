from mininet.topo import Topo
from random import randint

class Mesh( Topo ):

    def build( self ):
        Topo.build(self)

        pc1 = self.addHost('h1')
        pc2 = self.addHost('h2')
        pc3 = self.addHost('h3')
        pc4 = self.addHost('h4')
        pc5 = self.addHost('h5')
        pc6 = self.addHost('h6')

        sw1 = self.addSwitch('s1')
        sw2 = self.addSwitch('s2')
        sw3 = self.addSwitch('s3')
        sw4 = self.addSwitch('s4')
        sw5 = self.addSwitch('s5')
        sw6 = self.addSwitch('s6')

        h = [sw1,sw2,sw3,sw4,sw5,sw6]
        p = [pc1,pc2,pc3,pc4,pc5,pc6]

        for i in range(len(h)):
            self.addLink(p[i],h[i])
            for j in [randint(0,5) for r in range(4)]:
                if h[i]!=h[j]:
                    self.addLink(h[i],h[j])

topos = { 'mesh': ( lambda: Mesh() ),'test':(lambda: test()) }


