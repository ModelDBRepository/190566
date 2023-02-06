'''
Defines a class, Neuron473863578, of neurons from Allen Brain Institute's model 473863578

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473863578:
    def __init__(self, name="Neuron473863578", x=0, y=0, z=0):
        '''Instantiate Neuron473863578.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473863578_instance is used instead
        '''
               
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Scnn1a-Tg3-Cre_Ai14_IVSCC_-168093.03.02.01_402529243_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
 
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473863578_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 164.37
            sec.e_pas = -91.0012588501
        for sec in self.apic:
            sec.cm = 2.14
            sec.g_pas = 5.76426414048e-05
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000486367210659
        for sec in self.dend:
            sec.cm = 2.14
            sec.g_pas = 9.17291803525e-06
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.000672838
            sec.gbar_Ih = 0.000354419
            sec.gbar_NaTs = 0.57448
            sec.gbar_Nap = 5.94889e-05
            sec.gbar_K_P = 0.0200383
            sec.gbar_K_T = 0.000731997
            sec.gbar_SK = 0.0142485
            sec.gbar_Kv3_1 = 0.0459949
            sec.gbar_Ca_HVA = 0.000327417
            sec.gbar_Ca_LVA = 0.00684505
            sec.gamma_CaDynamics = 0.000300285
            sec.decay_CaDynamics = 421.397
            sec.g_pas = 0.000153495
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

