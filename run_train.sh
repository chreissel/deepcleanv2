#!/bin/bash

export DEEPCLEAN_CONTAINER_ROOT=~/images/deepclean
export DATA_DIR=~/dc-demo/data
export RESULTS_DIR=~/dc-demo/results

#export DEEPCLEAN_IFO=H1
#export DEEPCLEAN_IFO=L1
export DEEPCLEAN_IFO=K1
#export DEEPCLEAN_STRAIN_CHANNEL=CAL-CS_PROC_DARM_STRAIN_DBL_DQ
export GPU_INDEX=0
nohup poetry run law run deepclean.tasks.Train \
	--image train.sif \
	--gpus $GPU_INDEX \
	--data-fname $DATA_DIR/K-K1_lldata-1369291863-16384.hdf5 \
	--output-dir $RESULTS_DIR/test_train_K1_2 > test_train_K1_2.2.out &
