# coding: utf-8
try:
    import urllib.request
except ImportError:
    raise ImportError('You should use Python 3.x')
import os.path
import gzip
import tarfile
import pickle
import os
import numpy as np

url_base = 'https://www.cs.toronto.edu/~kriz/'
key_file = 'cifar-10-python.tar.gz'


dataset_dir = os.path.dirname(os.path.abspath(__file__))
print(dataset_dir)
save_file = dataset_dir + "/cifar10.pkl"

train_num = 50000
test_num = 10000
img_dim = (3, 32, 32)
img_size = 3072


def _download(file_name):
    file_path = dataset_dir + "/" + file_name

    if os.path.exists(file_path):
        return

    print("Downloading " + file_name + " ... ")
    urllib.request.urlretrieve(url_base + file_name, file_path)
    print("Done")

def download_cifar10():
    _download(key_file)
    global dataset_dir
    file_path = dataset_dir + "/" + key_file
    dataset_dir += '\cifar-10-batches-py'

def _load_batch(file_name):
    file_path = dataset_dir + "/" + file_name
    if not os.path.exists(file_path):
        file = tarfile.open(key_file)
        file.extractall()
    print("Loading " + file_name + " to dict file ...")
    data = unpickle(file_path)
    print("Done")

    return data

def _convert_numpy():

    dataset_batch_1 = _load_batch('data_batch_1')
    dataset_batch_2 = _load_batch('data_batch_2')
    dataset_batch_3 = _load_batch('data_batch_3')
    dataset_batch_4 = _load_batch('data_batch_4')
    dataset_batch_5 = _load_batch('data_batch_5')
    dataset_batch_test = _load_batch('test_batch')

    print("Converting to NumPy Array ...")
    dataset = {}
    dataset['train_img'] = np.vstack([dataset_batch_1[b'data'], dataset_batch_2[b'data'],
                                      dataset_batch_3[b'data'], dataset_batch_4[b'data'],
                                      dataset_batch_5[b'data']])
    dataset['train_label'] = []
    dataset['train_label'].extend(dataset_batch_1[b'labels'])
    dataset['train_label'].extend(dataset_batch_2[b'labels'])
    dataset['train_label'].extend(dataset_batch_3[b'labels'])
    dataset['train_label'].extend(dataset_batch_4[b'labels'])
    dataset['train_label'].extend(dataset_batch_5[b'labels'])
    dataset['train_label'] = np.array(dataset['train_label'])
    dataset['test_img'] = dataset_batch_test[b'data']
    dataset['test_label'] = np.array(dataset_batch_test[b'labels'])
    print("Done")
    return dataset

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict

def init_cifar10():
    download_cifar10()
    dataset = _convert_numpy()
    print("Creating pickle file ...")
    with open(save_file, 'wb') as f:
        pickle.dump(dataset, f, -1)
    print("Done!")


def _change_one_hot_label(X):
    T = np.zeros((X.size, 10))
    for idx, row in enumerate(T):
        row[X[idx]] = 1

    return T


def load_cifar10(normalize=True, flatten=True, one_hot_label=False, grayscale=False):
    if not os.path.exists(save_file):
        init_cifar10()

    with open(save_file, 'rb') as f:
        dataset = pickle.load(f)

    if normalize:
        for key in ('train_img', 'test_img'):
            dataset[key] = dataset[key].astype(np.float32)
            dataset[key] /= 255.0

    if one_hot_label:
        dataset['train_label'] = _change_one_hot_label(dataset['train_label'])
        dataset['test_label'] = _change_one_hot_label(dataset['test_label'])

    if grayscale:
        dataset['train_img'][:, :1024] *= 0.3
        dataset['train_img'][:, 1024:2048] *= 0.59
        dataset['train_img'][:, 2048:3072] *= 0.11
        dataset['train_img'] = dataset['train_img'][:, :1024] +\
                               dataset['train_img'][:, 1024:2048] +\
                               dataset['train_img'][:, 2048:3072]

        dataset['test_img'][:, :1024] *= 0.3
        dataset['test_img'][:, 1024:2048] *= 0.59
        dataset['test_img'][:, 2048:3072] *= 0.11
        dataset['test_img'] = dataset['test_img'][:, :1024] +\
                              dataset['test_img'][:, 1024:2048] +\
                              dataset['test_img'][:, 2048:3072]

    if not flatten:
        for key in ('train_img', 'test_img'):
            if grayscale:
                dataset[key] = dataset[key].reshape(-1, 1, 32, 32)
            else:
                dataset[key] = dataset[key].reshape(-1, 3, 32, 32)

    return (dataset['train_img'], dataset['train_label']), (dataset['test_img'], dataset['test_label'])


if __name__ == '__main__':
    init_cifar10()