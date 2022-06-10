
import numpy as np 

data = './tests/data/C13/C13-b_4002.ama.h5'
# set a svdcut value 
# svdcut = 


param_dict = {
    'pion' : {
    'corr_type'     : '2pt' ,    # '3pt_tsep8', '3pt_tsep10, '3pt_tsep12' '3pt_tsep14                 
    'buffer'        : 'pion' , # 'pion_SP' , 'proton', 'proton'  ext_current, 'ext_current_SP', 'local_axial_SP'
    'src_snk_sep'   : 'src5.0_snk5.0' ,
    'channel'       : 'pion' , # 'pion_px1_py0_pz0','pion_px1_py1_pz0' ,'pion_px1_py1_pz1', 'pion_px2_py0_pz0', 'pion_px2_py1_pz0' 
                                # 'pion_px2_py1_pz1' ,'pion_px2_py2_pz0' ,'pion_px2_py2_pz1' ,'pion_px3_py0_pz0' ,'pion_px3_py1_pz0'
    'fit_range'     : np.arange(5,18),
    'fit_fcn_type'  : 'exp', #'cosh', 'sinh' 'log'
    'simultaneous'  : 'False', 
    'n_states'      :  3, 
    'JK'            :  'False',
    'bootstrap'     :  'True',
    'priors'        :  'False',


    }
}