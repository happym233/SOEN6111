from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, accuracy_score, f1_score, confusion_matrix
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import joblib

def k_fold_train(model, X, y, n_splits=5):
    skf = StratifiedKFold(n_splits=n_splits, shuffle=True, random_state=42)
    avg_acc = 0
    avg_pre = 0
    avg_rec = 0
    avg_f1 = 0
    for i, (train_index, test_index) in enumerate(skf.split(X, y)):
        # get training and testing data for this fold
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]
        # scale data
        X_train, X_test = model.normalize(X_train, X_test)
        # train SVM model
        ml_model = model.get_model()
        ml_model.fit(X_train, y_train)
        y_pred = ml_model.predict(X_test)
        precision = precision_score(y_test, y_pred, average='micro')
        recall = recall_score(y_test, y_pred, average='micro' )
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred, average='micro')
        avg_acc = avg_acc + accuracy
        avg_pre = avg_pre + precision
        avg_rec = avg_rec + recall
        avg_f1 = avg_f1 + f1
        model.save(accuracy)
        print(f'Fold {i + 1}:')
        print(f'Precision = {precision:.3f}')
        print(f'Recall = {recall:.3f}')
        print(f'Accuracy = {accuracy:.3f}')
        print(f'F1-score = {f1:.3f}')
    model.add_result({
        'acc': avg_acc / n_splits,
        'pre': avg_pre / n_splits,
        'rec': avg_rec / n_splits,
        'f1': avg_f1 / n_splits
    })




if __name__ == '__main__':
    # define features and labels
    X = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10], [10, 11]])
    y = np.array([0, 1, 0, 1, 1, 0, 0, 0, 1, 0])

    # define cross-validation object
    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)


    # iterate over folds
    for i, (train_index, test_index) in enumerate(skf.split(X, y)):
        # get training and testing data for this fold
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = y[train_index], y[test_index]

        # scale data
        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        # train SVM model
        svm = SVC(kernel='rbf', gamma='scale', random_state=42)
        svm.fit(X_train, y_train)

        # evaluate performance on test data
        y_pred = svm.predict(X_test)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)

        # save model for this fold
        # filename = f'svm_model_fold_{i}.pkl'
        # joblib.dump(svm, filename)

        # print evaluation metrics for this fold
        print(f'Fold {i + 1}:')
        print(f'Precision = {precision:.3f}')
        print(f'Recall = {recall:.3f}')
        print(f'Accuracy = {accuracy:.3f}')
        print(f'F1-score = {f1:.3f}')
        # print(f'Confusion matrix = \n{cm}\n')
