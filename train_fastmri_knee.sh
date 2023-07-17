#!/bin/bash

export CUDA_VISIBLE_DEVICES=0

python main_fastmri.py \
 --config=configs/ve/fastmri_knee_320_ncsnpp_continuous.py \
 --eval_folder=eval/fastmri_multicoil_knee_320 \
 --mode='train'  \
 --workdir=workdir/fastmri_multicoil_knee_320