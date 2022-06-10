# lqcd_analysis_suite

lqcd_analysis_suite is an interactive analysis library that allows researchers in the field of lattice Quantum Chromodynamics(LQCD) to analyze hadronic correlation functions. 

The user will provide an input file containing parameters of interest(eg. hadron species, src_snk separation value, fit function type, fitting range, time range, etc.) then interact with the program via CLI to perform a fit to hadronic correlation functions. This suite is heavily reliant on Peter Lepage's lsqfit library: https://lsqfit.readthedocs.io/en/latest/index.html

## Prerequisites

Before you begin, ensure you have met the following requirements:
<!--- These are just example requirements. Add, duplicate or remove as required --->
* You have installed the latest version of `<lsqfit>`
* You have a `<Linux/Mac>` machine.

## Installing lqcd_analysis_suite

To install lqcd_analysis_suite, follow these steps:

Linux and macOS:
```
git clone https://github.com/gb-lanl/lqcd_analysis_suite.git
pip install -r requirements.txt
```

## Directory stucture 
   ```
   lqcd_analysis_suite
   ├── interact.py
   ├── lib
   │   ├── data_phase_0.py         
   │   ├── data_phase_1.py 
   │   └── data_display_phase_2.py
   │   └── two_pt_fit.py
   │   └── three_pt_fit.py
   │   └── fit_collect.py
   │   └── fit_analysis_.py 
   │   └── plots.py  
   ├── testing
   │   └── test.py
   │   └── input_params 
   │       └── {ens_abbreviation_}params.py
   │       └── priors.py
       ├── data
       │   └── {ens_abbreviation}
       │        └── .h5 files
   ├── .gitignore
   ├── LICENSE.txt
   ├── README.md
   ├── requirements.txt
   ├── setup.py
```

## Using lqcd_analysis_suite

To use lqcd_analysis_suite, follow these steps:

- Edit the ```.tests/{ens_abbreviation}_params.py``` dictionary to your specific case 
- ```python3 interact.py``` and follow the prompts 
-  eg. ```python3 interact.py ~/lqcd_analysis_suite/tests/data/C13/C13-b_5178.ama.h5```

## Description of required and optional input parameters: 
TODO 

## Contributing to lqcd_analysis_suite
To contribute to lqcd_analysis_suite, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively see the GitHub documentation on [creating a pull request](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

## Contributors

Thanks to the following people who have contributed to this project:

## Contact

If you want to contact me you can reach me at gbradley@lanl.gov 

## License
<!--- If you're not sure which open license to use see https://choosealicense.com/--->

This project uses the following license: [<license_name>](<link>).
