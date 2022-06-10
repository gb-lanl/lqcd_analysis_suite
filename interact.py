import h5py 
import os 
import sys
from os import path
import argparse as ap
import argcomplete
import h5py
import time 
import glob 
import subprocess

# local modules
import lib.data_phase_0 as phase_0 
import lib.data_phase_1 as phase_1 
import lib.data_display_phase_2 as phase_2 
#import lib.fit_collect as collect 
#import lib.fit_analysis_ as analyzer  
from tests import * 

folder_path = os.getcwd()
print(folder_path)

def main():
    parser = ap.ArgumentParser(description='Execute interactive lqcd analysis')

    parser.add_argument('input_file',
                        help='Where is the input parameter file?')
    parser.add_argument('--visit_h5', default=True,
                        help='Should I visit the h5 file and output its contents into a txt file?')
    parser.add_argument('--inspect_h5', default=True,
                        help='Should I open the txt file for you?')
    parser.add_argument('--fold_data', default=True,
                        help='Should I fold the data?')
    
    parser.add_argument('--fit_options', type=str, default=True,
                        help='Display fitting options')
    parser.add_argument('--use_priors', type=str, default=True,
                        help='Should I use a set of Bayesian priors for this fit?')
    
    args = parser.parse_args()
    # sys.stdout.write(str(calc(args)))

    argcomplete.autocomplete(parser)
    args = parser.parse_args()
    print(args)

    # get input file 
    file = args.input_file

    if args.visit_h5 == True:
        print ('checking hdf5 file..')
        with h5py.File(file, 'r') as h5f:
            h5f.visititems(phase_0.visitor_func) 
    
    files = os.listdir(folder_path)
    paths = [os.path.join(folder_path, basename) for basename in files]
    inspection_file = max(paths, key=os.path.getctime)
    print(inspection_file)

    if args.inspect_h5 == True:
        print('Opening h5 inspection file..')
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, inspection_file])

    if args.fold_data == True:
        print('Folding the data..')


    if args.fit_options == True:
        print('Displaying fit options..')

    if args.use_priors == True:
        print('Where is the dictionary of priors?')
        prior_path = input()

        
    



if __name__ == "__main__":
    main()