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

# parameters
learning_rate = 0.001
training_epochs = 15
batch_size = 100

# MNIST dataset
mnist_train = dsets.MNIST(root='dataset/',
                        train=True,
                        transform=transforms.ToTensor(),
                        download=True)
mnist_test = dsets.MNIST(root='dataset/',
                        train=False,
                        transform=transforms.ToTensor(),
                        download=True)

# dataloader
data_loader = torch.utils.data.DataLoader(dataset=mnist_train,
                                        batch_size=batch_size,
                                        shuffle=True,
                                        drop_last=True)


model = CNN().to(device)

criterion = nn.CrossEntropyLoss().to(device)
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

# Training
total_batch = len(data_loader)
print('Learning Start')

for epoch in range(training_epochs):
    avg_cost = 0

    for X, Y in data_loader:
        X = X.to(device)
        Y = Y.to(device)

        optimizer.zero_grad()
        hypothesis = model(X)

        cost = criterion(hypothesis, Y)
        cost.backward()
        optimizer.step()

        avg_cost += cost / total_batch

    print('Epoch: {}, Cost: {}'.format(epoch+1, avg_cost))

print('Learning Finished!')

# 파라미터 저장
path_dir = './ckpt'
file_name = "cnn_params.pth"
if not os.path.isdir(path_dir):
    os.mkdir(path_dir)

print("Parameter Save Complete!")
torch.save(model.state_dict(), os.path.join(path_dir, file_name))

