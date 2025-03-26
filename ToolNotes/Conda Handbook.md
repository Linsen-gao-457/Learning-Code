[TOC]

#### Table of Conents

- [Create Env](#create-env)
- [Rename/ copy a Conda Env](#rename-copy-a-conda-env)
- [Finetune env setting](#finetune-env-setting)
- [Building everything from scratch using anaconda](#building-everything-from-scratch-using-anaconda)
  - [Step 1: unload all modules](#step-1-unload-all-modules)
  - [Step 2: install packages](#step-2-install-packages)
  - [Step 3: install your own Cuda](#step-3-install-your-own-cuda)
  - [Step 4: set up environment variables](#step-4-set-up-environment-variables)
  - [Step 5: verify CUDA Installation](#step-5-verify-cuda-installation)

# Create Env

activate base env `source ~/miniconda3/bin/activate base`

Conda create Env `conda create --prefix ~/conda_envs/finetune python=3.11 -y`

Conda activate `Conda conda activate /home/l78gao/conda_envs/finetune`

remove env `conda remove --name name_of_conda_env --all`

# Rename/ copy a Conda Env

activate the env you want to copy`conda activate /home/l78gao/conda_envs/finetune`

Export the current environment `conda env export > finetune_env.yml`

Create a new environment with the desired name `conda env create -n new_name --file finetune_env.yml`

verify the new env `conda env list`

remove the old env`conda remove --prefix /home/l78gao/conda_envs/finetune --all`

activate the renamed env `conda activate new_name`

list installed packages in the old env`conda list --prefix /home/l78gao/conda_envs/finetune`

list installed packages in the new env `conda list -n new_name`

# Finetune env setting

First you should unload all the modules `module --force purge`

pip wo CC`pip install --no-cache-dir --force-reinstall torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121`

you should uninstall all CC dependency!!!

`pip install --no-cache-dir transformers datasets peft`

use pip show to show NO CC!!

`cat /etc/os-release` check my computer type and then use to install cuda

download cuda

```
wget https://developer.download.nvidia.com/compute/cuda/12.4.0/local_installers/cuda_12.4.0_550.54.14_linux.run -O ~/cuda_12.4.0.run
```

install cuda

```
sh ~/cuda_12.4.0.run --silent --toolkit --override --installpath=$HOME/cuda-12.4
```

set path

```
export CUDA_HOME=$HOME/cuda-12.4
export PATH=$CUDA_HOME/bin:$PATH
export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
echo 'export CUDA_HOME=$HOME/cuda-12.4' >> ~/.bashrc
echo 'export PATH=$CUDA_HOME/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
```

# Building everything from scratch using anaconda

This section will introduce how to set enviroment from scratch without depending on **ComputeCanada(CC)**:

While CC encourages users to load pre-built modules. To achieve full independence from CC, we should follow this golden rule: verify every installation. Use method like `pip show` to comfirm all the denpendencies are from your virtual conda env instead of from **CC**. This ensures a clean setup, preventing unexpected conflicts in your environment.

### Step 1: unload all modules

Unload all the module first, using `module --force purge` and use `module list` to check whether you unload all modules!

### Step 2: install packages

For every package, you can use `pip install --no-cache-dir package_name` and use `pip show package_name` to check every package should be without any dependence on CC.

### Step 3: install your own Cuda

You need to install your own Cuda instead of loading from CC.
Determine the correct Cuda version first `$ navidai-smi`.

After that, you can click [here](https://developer.nvidia.com/cuda-12-4-0-download-archive?target_os=Linux) or other versions of CUDA to download CUDA.

You can use `$ cat /etc/os-release` to know your system details

Download CUDA:

```
wget https://developer.download.nvidia.com/compute/cuda/12.4.0/local_installers/cuda_12.4.0_550.54.14_linux.run -O ~/cuda_12.4.0.run
```

After downloading the installer, the next step is to install CUDA. Since you do not have `sudo` privileges(as CC does not provide user passwords), you cannot follow the standard installation instructions from the official NVDIA website. Instead, you can install CUDA using the following command.

```
sh ~/cuda_12.4.0.run --silent --toolkit --override --installpath=$HOME/cuda-12.4
```

### Step 4: set up environment variables

To ensure your system correctly detects tha installed CUDA version, update the environment variables:

```
$ export CUDA_HOME=$HOME/cuda-12.4
$ export PATH=$CUDA_HOME/bin:$PATH
$ export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH
$ echo 'export CUDA_HOME=$HOME/cuda-12.4' >> ~/.bashrc
$ echo 'export PATH=$CUDA_HOME/bin:$PATH' >> ~/.bashrc
$ echo 'export LD_LIBRARY_PATH=$CUDA_HOME/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
$ source ~/.bashrc
```

### Step 5: verify CUDA Installation

Check if Pytorch detects CUDA:

```
python -c "import torch; print(torch.cuda.is_available())"
```

Expected Output `True`

Check the detected GPU

```
python -c "import torch; print(torch.cuda.get_device_name(0))"

```

---
