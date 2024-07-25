import numpy as np

from microtorch import Tensor
from microtorch import nn
from microtorch.optim import SGD, Adam
from microtorch.losses import MSELoss, BCELoss

x = Tensor([
    [0.0, 0.0],
    [1.0, 0.0],
    [0.0, 1.0],
    [1.0, 1.0]
])

y = Tensor([
    [0.0],
    [1.0],
    [1.0],
    [0.0],
])

np.random.seed(42)
model = nn.Sequential(
    nn.Linear(2, 16),
    nn.Sigmoid(),
    nn.Linear(16, 16),
    nn.Sigmoid(),
    nn.Linear(16, 1),
    nn.Sigmoid()
)

mse = MSELoss()
bce = BCELoss()

if __name__ == '__main__':
    optimizer = Adam(model.params(), lr=0.001)
    for i in range(1000):
        loss = bce(model(x), y)
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

    pred = model(x)
    print(pred)


