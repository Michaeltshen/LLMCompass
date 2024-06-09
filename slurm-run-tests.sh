#!/bin/bash

#SBATCH --job-name llmcompass-tests                         # Job name
#SBATCH --mail-type=ALL                      # Request status by email 
#SBATCH --mail-user=mts247@cornell.edu        # Email address to send results to.
#SBATCH --get-user-env
#SBATCH --mem=100G
#SBATCH -t 99:00:00
#SBATCH --gres=gpu:1
#SBATCH --partition=default_partition
#SBATCH --requeue

cd ae/figure11
bash run_figure11.sh 