from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        Topo.build(self)
        # Add hosts and switches
        top_left = self.addHost( 'h1' )
        bottom_left = self.addHost( 'h2' )
        bottom_right = self.addHost( 'h3' )
        top_right = self.addHost( 'h4' )
        top_left_swi = self.addSwitch( 's1' )
        bottom_left_swi = self.addSwitch( 's2' )
        bottom_right_swi = self.addSwitch( 's3' )
        top_right_swi = self.addSwitch( 's4' )

        # Add links
        self.addLink( top_left, top_left_swi )
        self.addLink( bottom_left, bottom_left_swi )
        self.addLink( bottom_right, bottom_right_swi )
        self.addLink( top_right, top_right_swi )
        self.addLink( top_left_swi, bottom_left_swi )
        self.addLink( bottom_left_swi, bottom_right_swi )
        self.addLink( bottom_right_swi, top_right_swi )
        self.addLink( top_right_swi, top_left_swi )


topos = { 'ring': ( lambda: MyTopo() ) }

#sudo mn --custom ring.py --topo ring