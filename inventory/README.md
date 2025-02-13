# Inventory

This is a version tracker for PyTorch weights.

My YOLOX-compatible neural networks are named using the following system:
```
<architecture_exp_name>-<pretrained_dataset_name>-<fine_tune_dataset_name>-(<tensorrt_deployment_target>)
```

where

+ **architecture_name**: Each different configuration of a neural network will get a new name.
+ **pretrained_dataset_name**: For example, if the neural network is pre-trained using COCO object detection dataset, this will be 'COCO2017'. Otherwise, if the neural network is trained from scratch, this will be 'None'. [See upstream root README.md for how to pretrain with COCO](https://github.com/codename-gimondi/gi-YOLOX#readme)
+ **fine_tune_dataset_name**: This will show which version of my own dataset I have used to train the neural network.
+ **tensorrt_deployment_target**(optional): While PyTorch weights are universal, optimized TensorRT files cannot be shared across different device architectures / GPUs.

YOLOX stores architecture definitions as python configuration files in `exps/` folder, and all else in the respective `YOLOX_outputs` folder.

## Ready to Use Weights

Name (a composition of the below components) | Info
--- | ---
nano_foxtrot-COCO-gopro_alpha | Real time on Jetson Xavier NX
nano_juliet-COCO-gopro_alpha | Hopefully real time on Jetson Nano 

## Name Components

Relevant files to be found in: 'exps/' folder.

Name | Notes | Input Dimensions | Output Categories | Other Architecture Parameters
--- | --- | --- | --- | ---
nano_foxtrot | All the same parameters as default nano.py to enable pretrained fine tuning | (416,416) | 7 | depth=0.33, width=0.25, random_size=(10,20)
nano_india | Speed-priority. Pretrained on COCO | (256,256) | 80 (COCO) | depth=0.165, width=0.125, random_size=(5,10)
nano_juliet | transfer learning from `nano_india` | (256,256) | 7 | same as `nano_india`
small_kilo | Transfer learned from YOLOX_s(mall) for making demo videos on desktop GPU | (640,640) | 7 | same as YOLOX_s

## Pretrained Dataset Inventory

Name | Notes
--- | ---
COCO2017 | https://cocodataset.org/#download

## Fine Tune Dataset Inventory

Name | Notes | Start Date | End Date | Raw Data Size | COCO-formatted TAR archive file
--- | --- | --- | --- | --- | ---
gopro_alpha | 1920x1440 or 1920x1080 on-bike GoPro Hero Session 4. More front than rear, only a few night scenes. | 2021-09-16 | 2021-10-23 | 285GB of Video | 14.7GB

## Ground Truth Valid/Test Dataset Inventory

Name | Notes | Start Date | End Date | Raw Data Size | COCO-formatted TAR archive file
--- | --- | --- | --- | --- | ---
gt_sindorim | 1920x1440 on-bike GoPro Hero Session 4. Front only. Manual labels by Jason Sohn. Children's day, perfect weather lots of people. | 2021-05-05 | 2021-05-05 | 13.5GB of Video | 25.6MB

## TensorRT Deployment Target Inventory

Choose among

Name | Notes
--- | ---
jetson_nano | NVIDIA Jetson Nano
jetson_nx | NVIDIA Jetson Xavier NX

