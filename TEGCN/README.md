# TEGCN
Note that:
- This code is based on [TE-GCN](https://github.com/xieyulai/TE-GCN)

## Data preparation
```
cd TE-GCN
mkdir data
```
Download the data in [baidupan](https://github.com/xieyulai/UAVHuman_For_TE-GCN)  
Put downloaded data into the following directory structure:

```
—— data
    —— train_data.npy
```

## TRAIN
You can train the your model using the scripts:
```
cd TE-GCN
sh scripts/TRAIN_V2.sh
```

## TEST
You can test the your model using the scripts:
```
cd TE-GCN
sh scripts/EVAL_V2.sh
```
