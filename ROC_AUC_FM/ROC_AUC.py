from sklearn.metrics import roc_curve, auc, precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt
import numpy as np
from itertools import cycle
colors = cycle(['aqua', 'darkorange', 'r', 'b', 'g', 'pink', 'gray', 'pink', 'purple', 'lightblue'])


import warnings
warnings.filterwarnings("ignore", message="No positive samples in y_true")


def ROCandAUC(y_true, y_proba, n_classes):
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    precision = dict()
    recall = dict()
    average_precision = dict()    
    for i in range(n_classes):
        fpr[i], tpr[i], _ = roc_curve(y_true[:, i], y_proba[:, i])   
        #Y_test样例真实标签，y_score学习器预测的样例的概率 
        roc_auc[i] = auc(fpr[i], tpr[i])
        
        precision[i],recall[i],_ = precision_recall_curve(y_true[:,i],y_proba[:,i])
        average_precision[i] = average_precision_score(y_true[:,i],y_proba[:,i])
    return roc_auc, fpr, tpr, precision, recall, average_precision

def DrawROC(save_path, roc_auc, n_classes, dic, fpr, tpr, NAME):
    plt.figure(1, figsize=(8,4))
    
    for i, color in zip(range(n_classes), colors):
        np.savetxt(save_path+'/'+'ROC' +'/'+ dic[i]+'_'+ NAME +'_ROC.txt', np.column_stack((fpr[i],tpr[i])),fmt='%.6f %.6f')
        plt.plot(fpr[i], tpr[i], lw=1.5,label='{0} (AUC = {1:0.3f})'''.format(dic[i], roc_auc[i]))

    bwith = 2 #边框宽度设置为2
    ax = plt.gca()#获取边框
    ax.spines['bottom'].set_linewidth(bwith)
    ax.spines['left'].set_linewidth(bwith)
    ax.spines['top'].set_linewidth(bwith)
    ax.spines['right'].set_linewidth(bwith)
    
    plt.plot([0, 1], [0, 1], 'k--', lw=1)
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])
    plt.xlabel('False Positive Rate', fontdict={'family': 'Times New Roman', 'size': 16, 'weight'  : "bold"})
    plt.ylabel('True Positive Rate', fontdict={'family': 'Times New Roman', 'size': 16, 'weight'  : "bold"})
    # plt.title('The ROC curves of the '+ NAME +' for ' + name, fontdict={'family': 'Times New Roman', 'size': 18, 'weight'  : "bold"})
    plt.rcParams['font.sans-serif']=['Times New Roman']
    plt.rc('legend', fontsize= 12)
    plt.tick_params(labelsize=14, width=1)
    
    plt.legend(loc="lower right")
    plt.savefig(save_path+'/'+NAME+'_ROC.svg',format='svg', bbox_inches='tight', transparent=True, dpi=200)
    plt.show()

def DrawPR(save_path, average_precision, n_classes, dic, recall, precision, fpr, tpr,NAME):
    plt.figure(2, figsize=(8,4))
    for i, color in zip(range(n_classes), colors):
        np.savetxt(save_path+'/'+'PR' +'/'+ dic[i]+'_'+ NAME +'_PR.txt', np.column_stack((fpr[i],tpr[i])),fmt='%.6f %.6f')
        plt.plot(recall[i],precision[i],label = "{0}(AP={1:0.3f})".format(dic[i],average_precision[i]))
    
    bwith = 2 #边框宽度设置为2
    ax = plt.gca()#获取边框
    ax.spines['bottom'].set_linewidth(bwith)
    ax.spines['left'].set_linewidth(bwith)
    ax.spines['top'].set_linewidth(bwith)
    ax.spines['right'].set_linewidth(bwith)
    
    plt.plot( [1, 0], [0, 1], 'k--', lw=1)
    plt.xlim([-0.05,1.05])
    plt.ylim([-0.05,1.05])  
    plt.xlabel('Recall', fontdict={'family': 'Times New Roman', 'size': 16, 'weight'  : "bold"})
    plt.ylabel('Precision', fontdict={'family': 'Times New Roman', 'size': 16, 'weight'  : "bold"})
    # plt.title('The PR curve of the '+ NAME +' for ' + name, fontdict={'family': 'Times New Roman', 'size': 18, 'weight'  : "bold"})
    plt.rcParams['font.sans-serif']=['Times New Roman']
    plt.rc('legend', fontsize= 12)
    plt.tick_params(labelsize=14, width=1)
    
    plt.legend(loc="lower left")
    
    plt.savefig(save_path+'/'+NAME+'_PR.svg',format='svg', bbox_inches='tight', transparent=True, dpi=200)
    plt.show()

