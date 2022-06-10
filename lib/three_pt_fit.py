import argparse as ap
import os, sys
import argcomplete
import numpy as np
import lsqfit 

# local modules 
import lib.data_phase_0 as phase0
import lib.data_phase_1 as phase1 
import c13_params as params
import two_pt_fit as tp 

class Ratio(lsqfit.MultiFitterModel):
    '''
    3 point correlation function construction. 
    Relies on the lsqfit module: https://lsqfit.readthedocs.io/en/latest/lsqfit.html#lsqfit.MultiFitter
    '''
    def __init__(self, datatag, t, params, n_states):
        super(Ratio, self).__init__(datatag)
        # variables for fit
        self.t = np.array(t)
        self.n_states = n_states

        # keys (strings) used to find the wf_overlap and energy in a parameter dictionary
        self.params = params

    def fitfcn(p=None, t=None):
        if p is None:
            p = p0
        
        if t is None:
            t = self.t

        wf = p[self.params['wf']]
        E0 = p[self.params['E0']]
        log_dE = np.append(-np.inf, p[self.params['log(dE)']])
        d = p[self.params['d']]
        g_nm = p[self.params['g_nm']]

        E = np.array([np.sum([np.exp(log_dE[j]) for j in range(n+1)]) for n in range(self.n_states)]) + E0

        output = 0
        for n in range(self.params['n_states']):
            for m in range(self.params['n_states']):
                if n == m:
                    #if m > n: g_nm[n, m] = g_nm[m, n]
                    output += ((t-1)*wf[n]*g_nm[n, m] + d[n]) * np.exp(-E[n] * t)
                else:
                    pass
                    E_n = E[n]
                    E_m = E[m]
                    dE_nm = E_n - E_m
                    dE_mn = -dE_nm

                    output += (wf[n]*g_nm[n, m]) * ((np.exp(dE_nm/2 - E_n*t) - np.exp(dE_mn/2 - E_m*t)) /
                                                    (np.exp(dE_mn/2) - np.exp(dE_nm/2)))
        return output

        # The prior determines the variables that will be fit by multifitter --
        # each entry in the prior returned by this function will be fitted
    def buildprior(self,prior, mopt=None, extend=False):
        # Extract the model's parameters from prior.

        return prior

    def builddata(self, data):
        # Extract the model's fit data from data.
        # Key of data must match model's datatag!
        return data[self.datatag]

