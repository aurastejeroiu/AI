import math

import torch

import myModel

# we load the model

filepath = "myNet.pt"
ann = myModel.Net(2, 64, 1)

ann.load_state_dict(torch.load(filepath))
ann.eval()

# visualise the parameters for the ann (aka weights and biases)
for name, param in ann.named_parameters():
    if param.requires_grad:
        print(name, param.data)

x = float(input("x = "))
y = float(input("y = "))
# x = y = float(2)

x = torch.tensor([x])
y = torch.tensor([y])
predicted = ann(torch.tensor([x, y])).tolist()[0]
# real = (x + y / math.pi).item()
real = torch.sin(x + y / math.pi).item()
print("predicted: ", predicted)
print("real: ", real)
print("difference: ", abs(predicted - real))
