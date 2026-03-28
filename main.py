import torch
x = torch.tensor([2.0], requires_grad=True)
y = x**2
learning_rate = 0.1
y.backward()
# the update state
with torch.no_grad():
    x-=learning_rate * x.grad
print(x)










