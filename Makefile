.ONESHELL:
SHELL = /bin/bash

.PHONY : env
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml
	conda activate traffic-collisions
	conda install ipykernel
	python -m ipykernel install --user --name make-env --display-name "IPython - traffic-collisions"
    
.PHONY : all
all :
	jupyterbook execute main.ipynb
	jupyterbook execute day_of_month.ipynb
	jupyterbook execute time_of_day.ipynb

.PHONY : html
html :
	jupyterbook build .
