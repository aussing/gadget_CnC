#!/bin/bash -l
##SBATCH --mail-type=BEGIN,END,FAIL
##SBATCH --mail-user=harry.potter@swin.edu.au
#SBATCH --time=01:30:00
#SBATCH --nodes=1
#SBATCH --ntasks=32
#SBATCH --mem-per-cpu=5000MB
#SBATCH --tmp=8G
#SBATCH --job-name DM-L50-N128


echo
echo "Running on hosts: $SLURM_NODELIST"
echo "Running on $SLURM_NNODES nodes."
echo "Running on $SLURM_NPROCS processors."
echo "Current working directory is `pwd`"
echo 

srun ./Gadget4 ./param.txt
