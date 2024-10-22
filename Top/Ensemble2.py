import argparse
import pickle
import numpy as np
from tqdm import tqdm
from skopt import gp_minimize

# Global variables to track the best accuracy and predictions
best_acc = -1
best_predictions = []

def objective(weights):
    global best_acc, best_predictions
    right_num = total_num = 0
    predictions = []

    for i in tqdm(range(len(label))):
        l = label[i]
        r_values = [r[i][1] for r in [r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, r13, r14, r15]]
        # r_values = [r[i][1] for r in [r7, r8]]
        
        r = sum(r_val * weight for r_val, weight in zip(r_values, weights))
        r = np.argmax(r)
        predictions.append(r)
        right_num += int(r == int(l))
        total_num += 1
        
    acc = right_num / total_num

    # Save the predictions for the current weight configuration
    # np.save('predictions.npy', predictions)
    
    # Save the best predictions and accuracy
    if acc > best_acc:
        best_acc = acc
        best_predictions = predictions.copy()

    print(f'Current accuracy: {acc}')
    return -acc

def predict_with_weights(weights, r_values):
    return sum(r_val * weight for r_val, weight in zip(r_values, weights))
    # r = sum(r_val * weight for r_val, weight in zip(r_values, weights))
    # return np.argmax(r)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser()
    parser.add_argument('--benchmark', default = 'V1')
    parser.add_argument('--mixformer_J_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/A/skmixf__V1_J/epoch1_test_score.pkl')
    parser.add_argument('--mixformer_B_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/A/skmixf__V1_B/epoch1_test_score.pkl')
    parser.add_argument('--mixformer_JM_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/A/skmixf__V1_JM/epoch1_test_score.pkl')
    parser.add_argument('--mixformer_BM_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/A/skmixf__V1_BM/epoch1_test_score.pkl')
    parser.add_argument('--mixformer_k2_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/A/skmixf__V1_k2/epoch1_test_score.pkl')
    parser.add_argument('--mixformer_k2M_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/A/skmixf__V1_k2M/epoch1_test_score.pkl')
    parser.add_argument('--ctrgcn_J2d_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/A/ctrgcn_V1_J/epoch1_test_score.pkl')
    parser.add_argument('--ctrgcn_B2d_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/A/ctrgcn_V1_B/epoch1_test_score.pkl')
    parser.add_argument('--ctrgcn_J3d_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/A/ctrgcn_V1_J_3D/epoch1_test_score.pkl')
    parser.add_argument('--ctrgcn_B3d_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/A/ctrgcn_V1_B_3D/epoch1_test_score.pkl')
    parser.add_argument('--tdgcn_J2d_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/A/tdgcn_V1_J/epoch1_test_score.pkl')
    parser.add_argument('--tdgcn_B2d_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/A/tdgcn_V1_B/epoch1_test_score.pkl')
    parser.add_argument('--mstgcn_J2d_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/A/mstgcn_V1_J/epoch1_test_score.pkl')
    parser.add_argument('--mstgcn_B2d_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/A/mstgcn_V1_B/epoch1_test_score.pkl')
    parser.add_argument('--tegcn_J_Score', default = '/home/zjl_laoshi/xiaoke/TE-GCN/work_dir/joint_A/epoch1_test_score.pkl')
    # parser.add_argument('--tegcn_B_Score', default = './Model_inference/Mix_GCN/output/ctrgcn_V1_BM_3D/epoch1_test_score.pkl')  #还未训练

    #B
    parser.add_argument('--new_test_r1_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/test/skmixf__V1_J/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r2_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/test/skmixf__V1_B/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r3_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/test/skmixf__V1_JM/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r4_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/test/skmixf__V1_BM/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r5_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/test/skmixf__V1_k2/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r6_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_Former/output/test/skmixf__V1_k2M/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r7_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/test/ctrgcn_V1_J/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r8_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/test/ctrgcn_V1_B/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r9_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/test/ctrgcn_V1_J_3D/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r10_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/test/ctrgcn_V1_B_3D/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r11_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/test/tdgcn_V1_J/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r12_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/test/tdgcn_V1_B/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r13_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/test/mstgcn_V1_J/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r14_Score', default = '/home/zjl_laoshi/xiaoke/Top/Model_inference/Mix_GCN/output/test/mstgcn_V1_B/epoch1_test_score.pkl')
    parser.add_argument('--new_test_r15_Score', default = '/home/zjl_laoshi/xiaoke/TE-GCN/work_dir/joint_B/epoch1_test_score.pkl')
    # parser.add_argument('--tegcn_B_Score', default = './Model_inference/Mix_GCN/output/ctrgcn_V1_BM_3D/epoch1_test_score.pkl')  #还未训练
    arg = parser.parse_args()
    
    benchmark = arg.benchmark
    if benchmark == 'V1':
        npz_data = np.load('/home/zjl_laoshi/xiaoke/dataset_xiaoke/eval/test_label_A.npy')
        label = npz_data
    else:
        assert benchmark == 'V2'
        npz_data = np.load('/home/zjl_laoshi/xiaoke/dataset_xiaoke/eval/test_label_A.npy')
        label = npz_data

    # Load all scores
    with open(arg.mixformer_J_Score, 'rb') as r1:
        r1 = list(pickle.load(r1).items())

    with open(arg.mixformer_B_Score, 'rb') as r2:
        r2 = list(pickle.load(r2).items())

    with open(arg.mixformer_JM_Score, 'rb') as r3:
        r3 = list(pickle.load(r3).items())

    with open(arg.mixformer_BM_Score, 'rb') as r4:
        r4 = list(pickle.load(r4).items())

    with open(arg.mixformer_k2_Score, 'rb') as r5:
        r5 = list(pickle.load(r5).items())
        
    with open(arg.mixformer_k2M_Score, 'rb') as r6:
        r6 = list(pickle.load(r6).items())
    
    with open(arg.ctrgcn_J2d_Score, 'rb') as r7:
        r7 = list(pickle.load(r7).items())

    with open(arg.ctrgcn_B2d_Score, 'rb') as r8:
        r8 = list(pickle.load(r8).items())

    with open(arg.ctrgcn_J3d_Score, 'rb') as r9:
        r9 = list(pickle.load(r9).items())

    with open(arg.ctrgcn_B3d_Score, 'rb') as r10:
        r10 = list(pickle.load(r10).items())

    with open(arg.tdgcn_J2d_Score, 'rb') as r11:
        r11 = list(pickle.load(r11).items())
        
    with open(arg.tdgcn_B2d_Score, 'rb') as r12:
        r12 = list(pickle.load(r12).items())
    
    with open(arg.mstgcn_J2d_Score, 'rb') as r13:
        r13 = list(pickle.load(r13).items())

    with open(arg.mstgcn_B2d_Score, 'rb') as r14:
        r14 = list(pickle.load(r14).items())

    with open(arg.tegcn_J_Score, 'rb') as r15:
        r15 = list(pickle.load(r15).items())

    # space = [(0.2, 1.2) for i in range(15)]
    space = [(0, 3) for i in range(15)]
    result = gp_minimize(objective, space, n_calls=20, random_state=0)
    
    print('Maximum accuracy: {:.4f}%'.format(-result.fun * 100))
    print('Optimal weights: {}'.format(result.x))
    
    # Save the best predictions to a file
    # np.save('best_predictions.npy', best_predictions)

    # Apply weights to a new test dataset
    best_weights = result.x
    
    # Load new test data scores
    with open(arg.new_test_r1_Score, 'rb') as r1:
        r1_new = list(pickle.load(r1).items())
    
    with open(arg.new_test_r2_Score, 'rb') as r2:
        r2_new = list(pickle.load(r2).items())
    
    with open(arg.new_test_r3_Score, 'rb') as r3:
        r3_new = list(pickle.load(r3).items())
    
    with open(arg.new_test_r4_Score, 'rb') as r4:
        r4_new = list(pickle.load(r4).items())
    
    with open(arg.new_test_r5_Score, 'rb') as r5:
        r5_new = list(pickle.load(r5).items())
    
    with open(arg.new_test_r6_Score, 'rb') as r6:
        r6_new = list(pickle.load(r6).items())
    
    with open(arg.new_test_r7_Score, 'rb') as r7:
        r7_new = list(pickle.load(r7).items())
    
    with open(arg.new_test_r8_Score, 'rb') as r8:
        r8_new = list(pickle.load(r8).items())
    
    with open(arg.new_test_r9_Score, 'rb') as r9:
        r9_new = list(pickle.load(r9).items())
    
    with open(arg.new_test_r10_Score, 'rb') as r10:
        r10_new = list(pickle.load(r10).items())
    
    with open(arg.new_test_r11_Score, 'rb') as r11:
        r11_new = list(pickle.load(r11).items())
    
    with open(arg.new_test_r12_Score, 'rb') as r12:
        r12_new = list(pickle.load(r12).items())
    
    with open(arg.new_test_r13_Score, 'rb') as r13:
        r13_new = list(pickle.load(r13).items())
    
    with open(arg.new_test_r14_Score, 'rb') as r14:
        r14_new = list(pickle.load(r14).items())
    
    with open(arg.new_test_r15_Score, 'rb') as r15:
        r15_new = list(pickle.load(r15).items())
    
    # Apply weights on the new test set
    predictions_new = []
    for i in range(len(r7_new)):
        r_values_new = [r[i][1] for r in [r1_new, r2_new, r3_new, r4_new, r5_new, r6_new, r7_new, r8_new, r9_new, r10_new, r11_new, r12_new, r13_new, r14_new, r15_new]]
        # r_values_new = [r[i][1] for r in [r7_new, r8_new]]
        prediction = predict_with_weights(best_weights, r_values_new)
        predictions_new.append(prediction)
    # Save the new test set predictions
    np.save('new_test_predictions.npy', predictions_new)