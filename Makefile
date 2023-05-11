.ONESHELL:
SHELL = /bin/bash

.PHONY : env
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml
	conda activate traffic-collisions
	conda install ipykernel
	python -m ipykernel install --user --name traffic-collisions --display-name "IPython - traffic-collisions"
    
.PHONY : all
all :
	jupyter execute main.ipynb --kernel_name=traffic-collisions
	jupyter execute analysis/*.ipynb --kernel_name=traffic-collisions

.PHONY : html
html :
	jupyter-book build .