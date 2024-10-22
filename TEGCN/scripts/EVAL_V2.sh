#!/bin/bash

RECORD=2995
WORKDIR=work_dir/$RECORD
MODELNAME=runs/$RECORD

#CONFIG=./config/uav-cross-subjectv1/test.yaml
CONFIG=./config/uav-cross-subjectv2/test.yaml

# WEIGHTS=runs/1041-52-15529.pt
WEIGHTS=/home/zjl_laoshi/yuxin/TE-GCN-main/runs/2102-49-14650.pt

BATCH_SIZE=128

python3 main.py  --config $CONFIG --work-dir $WORKDIR -model_saved_name $MODELNAME --device 5  --batch-size $BATCH_SIZE --test-batch-size $BATCH_SIZE --weights $WEIGHTS
