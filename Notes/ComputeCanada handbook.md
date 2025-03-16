# Use Slurm in computecanada

[official doc](https://docs.alliancecan.ca/wiki/Running_jobs)

`sbatch try.sh` file to set `I will put it in my github`

`$ squeue -u l78gao`

Check your job status`$ squeue -j jobid`

Check your user status `$ squeue | grep l78gao`

cancel your job `$ scancel jobid`

# Use GPU in compute Canada

Allocate GPU`srun --mem=128G --cpus-per-task=2 --time=3:00:00 --gres=gpu:v100l:1 --pty bash`

check `squeue -u l78gao`

check GPU `nvmm--version`

# Use Conda

Conda create Env `conda create --name myenv python=3.10`

Activate base env `source ~/.bashrc`

conda activate env `conda activate vllm-clean`

conda remove Env `conda env remove --prefix /scratch/l78gao/.conda/envs/vllm-cuda12`

conda deactivate Env `conda deactivate`



# Compute Canada virtual environment

remove all module `module purge`

load module `load module xxx`

check availability `module avail xxx`

check how to load this module/ pre-load module requirement `module spider xxx`

activate Env `source ~/A2/bin/activate`



# Use jupyter notebook

Allocate GPU resource`salloc --mem=16G --cpus-per-task=2 --time=3:00:00 --gres=gpu:v100l:1`

Activate Environment`source ~/A2/bin/activate`

install jupyterlab  `pip install jupyterlab`

Run four commands in your CC terminal

`echo -e '#!/bin/bash\nunset XDG_RUNTIME_DIR\njupyter notebook --ip $(hostname -f) --no-browser' >$VIRTUAL_ENV/bin/notebook.sh`
`chmod u+x $VIRTUAL_ENV/bin/notebook.sh`

`echo -e '#!/bin/bash\nunset XDG_RUNTIME_DIR\njupyter lab --ip $(hostname -f) --no-browser' > $VIRTUAL_ENV/bin/lab.sh`

`chmod u+x $VIRTUAL_ENV/bin/lab.sh`

Then you will get a output, you need to use the output node to change the `cdr2630.int.cedar.computecanada.ca:8888` below.

run in your own computer

`$VIRTUAL_ENV/bin/lab.sh`

`ssh -L 8888:cdr2630.int.cedar.computecanada.ca:8888 l78gao@cedar.computecanada.ca`

open your webpage and open the link localhost: 8888. then you can use the canada compute jupyter notebook



# Pytorch/pyserini Evaluation environment setting

module load StdEnv/2023
module load gcc/12.3
module load cuda/12.2
module load faiss/1.8.0
module load arrow
pip install datasets
module load java/21.0.1
pip install pyserini



# Vllm Env Setting(Still failed)

source ~/.bashrc
conda create -n vllm-1 python=3.12 -y
conda activate vllm-cuda12
conda install -c conda-forge numpy sentencepiece tqdm psutil protobuf
conda install -c conda-forge OpenCV
conda install -c conda-forge gcc
conda install pytorch==2.5.1 torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia
 pip install vllm 