#!/bin/bash

#SBATCH --job-name 512-matmul                         # Job name
#SBATCH --mail-type=ALL                      # Request status by email 
#SBATCH --mail-user=mts247@cornell.edu        # Email address to send results to.
#SBATCH --get-user-env
#SBATCH --mem=100G
#SBATCH -t 99:00:00
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=default_partition
#SBATCH --nodelist=kim-compute-03
#SBATCH --requeue

source run_hardware_512.sh