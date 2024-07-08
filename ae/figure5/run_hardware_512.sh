#!/bin/bash

# Navigate to the first directory and clean up
cd ab
cd ../../..

# Run tests for the first case
for i in {1..25}; do
    python -m ae.figure5.ab.test_matmul --gpu --roofline
    python -m ae.figure5.ab.test_matmul --gpu
done
