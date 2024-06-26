#!/bin/bash

#SBATCH --job-name llmcompass-gpu                         # Job name
#SBATCH --mail-type=ALL                      # Request status by email 
#SBATCH --mail-user=mts247@cornell.edu        # Email address to send results to.
#SBATCH --get-user-env
#SBATCH --mem=100G
#SBATCH -t 99:00:00
#SBATCH --gres=gpu:a100:1
#SBATCH --partition=default_partition
#SBATCH --requeue

cd ab

rm *.csv
rm *.pdf
cd ../../..
for i in {1..2500}
    python -m ae.figure5.ab.test_matmul --gpu --roofline
    python -m ae.figure5.ab.test_matmul --gpu
done

cd ae/figure5/ab

cd ../cf

rm *.csv
rm *.pdf
cd ../../..
for i in {1..2500}
    python -m ae.figure5.cf.test_softmax --gpu --roofline
    python -m ae.figure5.cf.test_softmax --gpu
done
cd ae/figure5/cf

cd ../de

rm *.csv
rm *.pdf
cd ../../..
for i in {1..2500}
    python -m ae.figure5.de.test_layernorm --gpu --roofline
    python -m ae.figure5.de.test_layernorm --gpu
done
cd ae/figure5/de

cd ../g

rm *.csv
rm *.pdf
cd ../../..
for i in {1..2500}
    python -m ae.figure5.g.test_gelu --gpu --roofline
    python -m ae.figure5.g.test_gelu --gpu
done
cd ae/figure5/g

# cd ../h

# rm *.csv
# rm *.pdf
# cd ../../..
# python -m ae.figure5.h.test_allreduce
# cd ae/figure5/h

# cd ../ijkl

# rm *.csv
# rm *.pdf
# cd ../../..
# python -m ae.figure5.ijkl.test_transformer --gpu --roofline
# python -m ae.figure5.ijkl.test_transformer --gpu --init --roofline
# python -m ae.figure5.ijkl.test_transformer --gpu
# python -m ae.figure5.ijkl.test_transformer --gpu --init
# cd ae/figure5/ijkl
# cd ../