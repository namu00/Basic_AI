import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision.datasets as dsets
import torchvision.transforms as transforms

from model.cnn import *

# device 설정 (cuda 사용 가능 시, cuda로 아니면 cpu로)
device = 'cuda' if torch.cuda.is_available() else 'cpu'

# random value 고정
torch.manual_seed(777)
if device == 'cuda':
    torch.cuda.manual_seed_all(777)

# MNIST dataset
mnist_test = dsets.MNIST(root='dataset/',
                        train=False,
                        transform=transforms.ToTensor(),
                        download=True)

model = CNN().to(device)

# Parameter Load
path_dir = './ckpt'
file_name = "cnn_params.pth"
model.load_state_dict(torch.load(os.path.join(path_dir, file_name)))
print("Parameter Load Complete!")

# Test
with torch.no_grad():
    X_test = mnist_test.test_data.view(len(mnist_test), 1, 28, 28).float().to(device)
    Y_test = mnist_test.test_labels.to(device)

    prediction = model(X_test)
    correct_prediction = torch.argmax(prediction, 1) == Y_test
    accuracy = correct_prediction.float().mean()
    print('Accuracy: {}%'.format(accuracy.item() * 100))