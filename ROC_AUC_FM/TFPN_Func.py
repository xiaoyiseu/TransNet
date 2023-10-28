import numpy as np
from sklearn.metrics import confusion_matrix, cohen_kappa_score, matthews_corrcoef

def SenSpec(Y_test_, y_predict_,  k):
    matrix4 = confusion_matrix(Y_test_[k],y_predict_ )
    accuracy = np.diag(matrix4).sum()/matrix4.sum()
#     print('ACC_TRUE：%.2f'%(accuracy*100))
    FP4, FN4, TP4, TN4 = TFPN(matrix4)
    VALUE4 = Metrics(FP4, FN4, TP4, TN4)  # ACC, TPR,TNR,G_Mean,F1_Score,PPV,NPV
#     return VALUE4
    n_list = matrix4.sum(axis=1)
    value=[]
    for index1, i in enumerate(VALUE4):
        value.append(CI(i, n_list))
    return value
#         print("{:s}: {:.2f}".format(name2[index1], value*100))
        
def Model_Name(path_weight, model, x_test, label):
    model.load_weights(path_weight,by_name=False)
    predictions = model.predict(x_test)
    y_predict_ = np.argmax(predictions[label], axis=1)
    return y_predict_

# 2-TP/TN/FP/FN的计算
def TFPN(matrix):
    FP = matrix.sum(axis=0) - np.diag(matrix)  
    FN = matrix.sum(axis=1) - np.diag(matrix)
    TP = np.diag(matrix)
    TN = matrix.sum() - (FP + FN + TP)
    return FP, FN, TP, TN
# 3-其他的性能参数的计算
def Metrics(FP, FN, TP, TN):
    ACC = (TP+TN)/(TP+TN+FP+FN) # accuracy of each class
    TPR = TP/(TP+FN) # Sensitivity/ hit rate/ recall/ true positive rate
    TNR = TN/(TN+FP) # Specificity/ true negative rate
    PPV = TP/(TP+FP) # Precision/ positive predictive value
    NPV = TN/(TN+FN) # Negative predictive value
    FPR = FP/(FP+TN) # Fall out/ false positive rate
    FNR = FN/(TP+FN) # False negative rate
    FDR = FP/(TP+FP) # False discovery rate
    G_Mean = np.sqrt(TPR*TNR)
    F1_Score = 2*(PPV*TPR)/(PPV+TPR)
    return ACC, TPR, TNR, G_Mean, F1_Score, PPV, NPV

from scipy import stats
# 计算置信区间
'''
acc_list :[0.2, 0.5, 0.1, 0.9]
n_list :[7, 21, 3, 64]
'''
def CI(acc_list, n_list):
    acc_list = np.array(acc_list)
    n_list = np.array(n_list)    
    valid_acc_list = acc_list[~np.isnan(acc_list)]
    valid_n_list = n_list[~np.isnan(acc_list)]
    avg_acc = np.average(valid_acc_list, weights=valid_n_list)
    return avg_acc
def RecogVert(model, x_test, label):
    predictions = model.predict(x_test)
    predicted = np.argmax(predictions[label], axis=1)
    return predicted
def Results(Metrics, matrix):
    average, min, max = (np.nansum(Metrics*(matrix.sum(axis=1)/matrix.sum())))*100, np.nanmin(Metrics)*100, np.nanmax(Metrics)*100
    return ("%.2f(%.2f-%.2f)" % (average, min,max))

def LevelDepat(list_name):
    Lev=[]
    Dep=[]
    for name in list_name:
        for _, i in enumerate(name):
            if i =='l':
                Lev.append(name[_+1: _+7])
                Dep.append(name[-9: -3])
    Level = [float(i) for i in Lev]
    Depart = [float(i) for i in Dep]
    return Level, Depart