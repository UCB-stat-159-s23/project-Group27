.ONESHELL:
SHELL = /bin/bash

.PHONY : create_environment
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml
	conda activate notebook
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "IPython - traffic-collisions"
    
.PHONY : all
all :
	jupyterbook execute main.ipynb 

.PHONY : html
html :
	jupyterbook build .