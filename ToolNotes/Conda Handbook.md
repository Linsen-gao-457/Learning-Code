[TOC]

## Create Env

activate base env `source ~/miniconda3/bin/activate base`

Conda create Env `conda create --prefix ~/conda_envs/finetune python=3.11 -y`

Conda activate `Conda conda activate /home/l78gao/conda_envs/finetune`



# Finetune

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

