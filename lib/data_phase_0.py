import h5py 
import os 
import sys
from os import path
import numpy as np
import time 

#local modules
#from tests import input_params
#param_input =  




project_input = '/home/gbradley/lqcd_analysis_suite/tests/data/C13/C13-b_5178.ama.h5'
# for s in os.listdir(project_input):
#     name , extension = path.splitext(s)
#     if path.splitext(name)[1] == '.ama':
#         key = path.splitext(name)[0]
#         #print(key)
#         configurations = key.split('_')[1]
#         #print(configuration)
#         files_to_dict = []
#         files_to_dict.append(configurations)
#         #print(files_to_dict)

#         all_configs = list()
#         for config in files_to_dict:
#             all_configs = project_input+'/C13-b_'+config+'.ama.h5'
#             print(all_configs)

def visitor_func(name, node):
    timestr = time.strftime("%Y%m%d-%H%M")
    with open("visit_h5_"+timestr+".txt", "a") as f:
        if isinstance(node, h5py.Group):
            print(node.name, 'is a Group',file=f)
        elif isinstance(node, h5py.Dataset):
            if (node.dtype == 'object') :
                print (node.name, 'is an object Dataset',file=f)
            else:
                print(node.name, 'is a Dataset',file=f)   
        else:
            print(node.name, 'is an unknown type',file=f)  

print ('checking hdf5 file')
with h5py.File(project_input, 'r') as h5f:
    h5f.visititems(visitor_func) 
       

#####    

# from os import listdir
# from os.path import isfile, join
# onlyfiles = [f for f in listdir(project_input) if isfile(join(project_input, f))]
# print(onlyfiles)
# all_files = os.listdir(project_input)
# new = []

# filename = project_input+'/'+onlyfiles[1]
# print(filename)
# with h5py.File(filename, 'r') as data:
#     print(data.keys())
#     for group in data.keys() :
#         print (group)
#     for dset in data['2pt']:      
#         print (dset)
#         ds_data = data['2pt'][dset] # returns HDF5 dataset object
#         #print (ds_data)
#         ds_data_ = data['2pt']['pion']
#         for key in ds_data_.keys():
#             corr_data = ds_data_[key]
#             print(corr_data)
            
        # #print (ds_data.shape, ds_data.dtype)
        #     arr = corr_data['pion'] # adding [:] returns a numpy array
        #     print(arr)
        #     for key in arr:
        #         correlator = arr[key]
        #         for key in correlator:
        #             correlator_data = correlator[key][:]
        #             print(correlator_data.shape,correlator_data.dtype)
        #             print (correlator_data)

        #             for i,snk in enumerate(input_params[hadron]['sinks']):
        #                 for j,src in enumerate(input_params[hadron]['sources']):
        #                     correlators[correlator_data+'_'