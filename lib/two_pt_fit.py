import argparse as ap
import os, sys
import argcomplete
import numpy as np
import lsqfit 

# local modules 
import lib.data_phase_0 as phase0
import lib.data_phase_1 as phase1 
import c13_params as params

'''
2 point correlation function construction. Relies on the lsqfit module.
 https://lsqfit.readthedocs.io/en/latest/lsqfit.html#lsqfit.MultiFitter
'''

class Two_pt(lsqfit.MultiFitterModel):
    def __init__(self, datatag, t, param_keys, n_states):
        super(hadron_model, self).__init__(datatag)
        # variables for fit
        self.t = np.array(t)
        self.n_states = n_states
        # keys (strings) used to find the wf_overlap and energy in a parameter dictionary
        self.param_keys = param_keys

    def fitfcn(self, p, t=None):
        if t is None:
            t = self.t

        wf = p[self.param_keys['wf']]
        E0 = p[self.param_keys['E0']]
        log_dE = p[self.param_keys['log(dE)']]

        output = wf[0] * np.exp(-E0 * t)
        for j in range(1, self.n_states):
            excited_state_energy = E0 + np.sum([np.exp(log_dE[k]) for k in range(j)], axis=0)
            output = output + wf[j] * np.exp(-excited_state_energy * t)
        return output

    # The prior determines the variables that will be fit by multifitter --
    # each entry in the prior returned by this function will be fitted
    def buildprior(self, prior, mopt=None, extend=False):
        # Extract the model's parameters from prior.
        return prior

    def builddata(self, data):
        # Extract the model's fit data from data.
        # Key of data must match model's datatag!
        return data[self.datatag]

    def fcn_effective_mass(self, p, t=None):
        if t is None:
            t=self.t

        return np.log(self.fitfcn(p, t) / self.fitfcn(p, t+1))

