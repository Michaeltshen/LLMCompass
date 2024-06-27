#!/bin/bash

# Navigate to the first directory and clean up
cd ab
rm *.csv *.pdf
cd ../../..

# Run tests for the first case
for i in {1..25}; do
    python -m ae.figure5.ab.test_matmul --gpu --roofline
    python -m ae.figure5.ab.test_matmul --gpu
done

# Navigate back to the directory
cd ae/figure5/ab
cd ../cf

# Clean up for the second case
rm *.csv *.pdf
cd ../../..

# Run tests for the second case
for i in {1..25}; do
    python -m ae.figure5.cf.test_softmax --gpu --roofline
    python -m ae.figure5.cf.test_softmax --gpu
done

# Navigate back to the directory
cd ae/figure5/cf
cd ../de

# Clean up for the third case
rm *.csv *.pdf
cd ../../..

# Run tests for the third case
for i in {1..25}; do
    python -m ae.figure5.de.test_layernorm --gpu --roofline
    python -m ae.figure5.de.test_layernorm --gpu
done

# Navigate back to the directory
cd ae/figure5/de
cd ../g

# Clean up for the fourth case
rm *.csv *.pdf
cd ../../..

# Run tests for the fourth case
for i in {1..25}; do
    python -m ae.figure5.g.test_gelu --gpu --roofline
    python -m ae.figure5.g.test_gelu --gpu
done

# Navigate back to the directory
cd ae/figure5/g
