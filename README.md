# python-numpy-pandas-matplotlib
Numpy, Pandas, Matplotlib

PyCharm environment setup: https://www.jetbrains.com/help/pycharm/conda-support-creating-conda-virtual-environment.html

Command Prompt Process:
1. conda create -n env_name list of packages
2. conda create -n py3 python=3 (if specific version is required)
3. conda activate my_env
4. conda env export > environment.yaml (Saving and loading environments)
5. conda env create -f environment.yaml (To create an environment from an environment file use)
6. conda env list 
7. conda env remove -n env_name
8. pip freeze | pip freeze > requirements.txt (List installed packages)


Set up Jupyter notebooks within PyCharm
https://www.jetbrains.com/help/pycharm/jupyter-notebook-support.html