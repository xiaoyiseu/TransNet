from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np

def plot_confusion_matrix(matrix, labels_name, title, cmap=plt.cm.Blues):#cmap='Blues'

    matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]    # 归一化

    plt.imshow(matrix, interpolation='nearest',cmap=cmap)    # 在特定的窗口上显示图像
#     plt.title(NAME_csv, fontdict={'family': 'Times New Roman', 'size': 20, 'weight'  : "bold"})    # 图像标题
#     plt.colorbar()

    
    bwith = 1.5 #边框宽度设置为2
    ax = plt.gca()#获取边框
#     ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
#     ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
    ax.spines['bottom'].set_linewidth(bwith)
    ax.spines['left'].set_linewidth(bwith)
    ax.spines['top'].set_linewidth(bwith)
    ax.spines['right'].set_linewidth(bwith)
    
    num_local = np.array(range(len(labels_name)))    
    plt.xticks(num_local, labels_name, rotation=0)    # 将标签印在x轴坐标上
    plt.yticks(num_local, labels_name)    # 将标签印在y轴坐标上
    
    plt.tick_params(labelsize=16, width=1)
    
    plt.rcParams['font.sans-serif']=['Times New Roman'] #['Times New Roman'] # ['SimSun']宋体；['SimHei']黑体，有很多自己都可以设置
    plt.rcParams['axes.unicode_minus'] = False
    
    plt.ylabel('True label', fontdict={'family': 'Times New Roman','weight' : "bold", 'size': 22})    
    plt.xlabel('Predicted label', fontdict={'family': 'Times New Roman', 'weight'  : "bold", 'size': 22})
    plt.tight_layout()


def DrawFusionMatrix(matrix, labels_name, name, path):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            plt.annotate(matrix[j, i], xy=(i, j), horizontalalignment='center', verticalalignment='center',
                         weight = "bold", color = "r", fontsize=12, family = "Times New Roman")
    plot_confusion_matrix(matrix, labels_name , "Confusion Matrix" )
    plt.savefig(path+ '/'+ name+'_English.svg',format='svg', bbox_inches='tight', transparent=True, dpi=200)
    plt.show()


def plot_confusion_matrix2(matrix, labels_name, title, cmap=plt.cm.Blues):  # cmap='Blues'

    matrix = matrix.astype('float') / matrix.sum(axis=1)[:, np.newaxis]  # 归一化
    from matplotlib.colors import LogNorm
    plt.imshow(matrix, interpolation='nearest', cmap=cmap)  # 在特定的窗口上显示图像
    #     plt.title(NAME_csv, fontdict={'family': 'Times New Roman', 'size': 20, 'weight'  : "bold"})    # 图像标题
    #     plt.colorbar()

    bwith = 1.5  # 边框宽度设置为2
    ax = plt.gca()  # 获取边框
    #     ax.spines['top'].set_color('red')  # 设置上‘脊梁’为红色
    #     ax.spines['right'].set_color('none')  # 设置上‘脊梁’为无色
    ax.spines['bottom'].set_linewidth(bwith)
    ax.spines['left'].set_linewidth(bwith)
    ax.spines['top'].set_linewidth(bwith)
    ax.spines['right'].set_linewidth(bwith)

    num_local = np.array(range(len(labels_name)))
    plt.xticks(num_local, labels_name, rotation=90)  # 将标签印在x轴坐标上
    plt.yticks(num_local, labels_name)  # 将标签印在y轴坐标上

    plt.tick_params(labelsize=8, width=1)

    plt.rcParams['font.sans-serif'] = ['Times New Roman']  # ['Times New Roman'] # ['SimSun']宋体；['SimHei']黑体，有很多自己都可以设置
    plt.rcParams['axes.unicode_minus'] = False

    plt.ylabel('True label', fontdict={'family': 'Times New Roman', 'weight': "bold", 'size': 10})
    plt.xlabel('Predicted label', fontdict={'family': 'Times New Roman', 'weight': "bold", 'size': 10})
    plt.tight_layout()


def DrawFusionMatrix2(matrix, labels_name, name, path):
    threshold = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i, j] >= threshold:
                plt.annotate(matrix[j, i], xy=(i, j), horizontalalignment='center', verticalalignment='center',
                             weight="bold", color="r", fontsize=4, family="Times New Roman")
            else:
                text = plt.text(j, i, "", ha="center", va="center")

    plot_confusion_matrix2(matrix, labels_name, "Confusion Matrix")
    plt.savefig(path + '/' + name + '_English.svg', format='svg', bbox_inches='tight', transparent=True, dpi=200)
    plt.show()