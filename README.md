# CSUST
本仓库包含了取名好难队所有的源代码以及训练、测试指令等。
## Preparing GCN（这里包括了TEGCN和TOP的所有环境配置）
```
conda env create -f environment.yaml
```
## Data preparation
```
mkdir data
```  
Download the data in [baidupan](https://github.com/xieyulai/UAVHuman_For_TE-GCN)  
Put downloaded data into the following directory structure:
```
—— data
    —— train_data.npy
```
Download the data in [baidupan](https://github.com/xieyulai/UAVHuman_For_TE-GCN)  
Put downloaded data into the following directory structure:

```
—— data
    —— train_data.npy
```

# Training & Testing
## [TE-GCN](https://github.com/xieyulai/TE-GCN)
### TRAIN
You can train the your model using the scripts:
```
cd TEGCN
sh scripts/TRAIN_V2.sh
```

### TEST
You can test the your model using the scripts:
```
cd TEGCN
sh scripts/EVAL_V2.sh
```
## [TOP](https://github.com/liujf69/ICMEW2024-Track10)
### TRAIN
You can train the your model using the scripts:
```

```

## Ensemble

## Contacts

