# Criticality and clinical department prediction of ED patients using machine learning based on heterogeneous medical data

## 1. Abstract
![Abstract](https://github.com/xiaoyiseu/ED-triage/assets/132346882/82d674a1-1121-4bb2-b479-d5411d792d54)

This is the code for the paper:[Criticality and clinical department prediction of ED patients using machine learning based on heterogeneous medical data](https://www.sciencedirect.com/science/article/pii/S0010482523008557)

Code available: https://github.com/xiaoyiseu/ED-triage

## 2. Setups

All code was developed and tested on a single machine equiped with a NVIDIA 2080Ti GPU. The environment is as bellow:

numpy==1.18.5

pandas==1.1.5

python==3.7.15

scikit-learn==0.23.1

scipy==1.6.2

tensorflow-gpu==1.15.0

pkuseg==0.0.25

## 3. Performance

### 3.1 Ablation experiment
![Level](https://github.com/xiaoyiseu/ED-triage/assets/132346882/90871f31-635a-42cc-bd15-435d111d5dcf)
![Department](https://github.com/xiaoyiseu/ED-triage/assets/132346882/e62ebcf0-cb1f-45c3-9ba8-507c3343bbb2)

### 3.2 PR curves and ROC curves of Department & Level prediction
**PR curves**

![Department_PR](https://github.com/xiaoyiseu/ED-triage/assets/132346882/26e401a0-bdbb-4cc8-ab45-551d4c4c743e)
![Level_PR](https://github.com/xiaoyiseu/ED-triage/assets/132346882/8e530daf-1d23-40df-8538-21502d5ce7df)


**ROC curves**

![Department_ROC](https://github.com/xiaoyiseu/ED-triage/assets/132346882/bceee248-047d-4348-adbe-b0302b793ed9)
![Level_ROC](https://github.com/xiaoyiseu/ED-triage/assets/132346882/0ffad50a-137f-4cc7-811b-075eaa4de223)

### 3.3 Comparative experiment

![trian valid](https://github.com/xiaoyiseu/ED-triage/assets/132346882/acbcc906-f727-4191-9e5f-1329bde9a7fe)

