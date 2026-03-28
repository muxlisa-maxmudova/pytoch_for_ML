import torch
x = torch.tensor([2.0], requires_grad=True)
y = x**2 + 5  # y = 2^2 + 5 = 9

# Calculate the derivative (dy/dx)
y.backward()

# The gradient is stored in x.grad
print(x.grad) # Output: 4.0 (Because d/dx of x^2 is 2x, and 2*2=4)
