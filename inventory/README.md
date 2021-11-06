# Inventory

This is a version tracker for PyTorch weights.

My YOLOX-compatible neural networks are named using the following system:
```
<architecture_name>-<pretrained_dataset_name>-<fine_tune_dataset_name>-(<tensorrt_deployment_target>)
```
where

+ **architecture_name**: Each different configuration of a neural network will get a new name.
+ **pretrained_dataset_name**: For example, if the neural network is pre-trained using COCO object detection dataset, this will be 'COCO2017'. Otherwise, if the neural network is trained from scratch, this will be 'None'.
+ **fine_tune_dataset_name**: This will show which version of my own dataset I have used to train the neural network.
+ **tensorrt_deployment_target**(optional): While PyTorch weights are universal, optimized TensorRT files cannot be shared across different device architectures / GPUs.

YOLOX stores architecture definitions as python configuration files in `exps/` folder, and all else in the respective `YOLOX_outputs` folder.

## Architecture Name Inventory

Relevant files to be found in: 'exps/' folder.

Name | Notes | Input Dimensions | Output Categories | Other Architecture Parameters
--- | --- | --- | --- | ---


## Pretrained Dataset Inventory

## Fine Tune Dataset Inventory

## TensorRT Deployment Target Inventory


