# 6.5930 Final Project

## Authors

## Overview

## Installation and Usage

### Model Pruing and Perplexity Evaluation

We used SparseGPT for the experiments regarding the model's perplexity. The base models we used in this project is OPT-125m. 

The instructions for perplexity evaluation can be found as below. 

```shell
cd sparsegpt

# Run dense baseline
python opt.py facebook/opt-125m c4

# Run magnitude baseline
python opt.py facebook/opt-125m c4 --sparsity .5 --gmp

# Prune to full 2:4 sparsity with SparseGPT
python opt.py facebook/opt-125m c4 --prunen 2 --prunem 4
```

### Energy and Latency Measurements with Hardware Simulation

We based our efficiency evaluation on the docker container equipped with pre-built Timeloop and Accelegy.

To reproduce the efficiency evaluation results, please first pull the docker first to update the container, and then start with `docker-compose up`. 

```
cd <your-git-repo-for-final-project>
export DOCKER_ARCH=<your arch amd64 or arm64>
docker-compose pull
docker-compose up
```

After launching the docker, please follow the instructions here for the simulation results.

```shell
cd example_designs/
python3 scripts/construct_opt.py

# run baseline dense designs w. any arch
python3 run_example_designs.py --architecture eyeriss_like --problem OPT125m

# run sparsegpt 2:4 sprase designs
python3 run_example_designs.py --clear_outputs --architecture sparse_tensor_core_like --problem MM/OPT125m_repr
```
