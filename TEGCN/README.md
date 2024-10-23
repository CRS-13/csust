# TEGCN
Note that:
- This code is based on [TEGCN](https://github.com/xieyulai/TE-GCN)

## Data preparation
Prepare the data according to [UAVHuman-Pose processing](https://github.com/xieyulai/UAVHuman_For_TE-GCN)

Your `data/` should be like this:
```
uav
___ xsub1
    ___ test_data.npy
    ___ test_label.pkl
    ___ train_data.npy
    ___ train_label.pkl
___ xsub2
    ___ test_data.npy
    ___ test_label.pkl
    ___ train_data.npy
    ___ train_label.pkl

```

## TRAIN
You can train the your model using the scripts:
```
sh scripts/TRAIN_V2.sh
```

## TEST
You can test the your model using the scripts:
```
sh scripts/EVAL_V2.sh
```

## WEIGHTS
We have released two trained weights in [baidupan](https://pan.baidu.com/s/1kourPFzEChrjc8kPO0y6rw),passwd is `nwhu`

Your should put them into `runs/`.

- V1:TOP1-42.37%
- V2:TOP1-68.11%
