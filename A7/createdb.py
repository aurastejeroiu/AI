import math

import torch

random_input_x = torch.add(torch.rand(1000, 1), -0.5) * 20
random_input_y = torch.add(torch.rand(1000, 1), -0.5) * 20
# print(random_input_x[0] + random_input_y[0])

# result = torch.sin(random_input_x)
result = []

for i in range(1000):
    tensor = torch.sin(random_input_x[i] + random_input_y[i] / math.pi)
#     tensor = random_input_x[i] + random_input_y[i] / math.pi
    result.append([random_input_x[i].item(), random_input_y[i].item(), tensor.item()])
    # result.append(torch.tensor([random_input_x[i].item(), random_input_y[i].item(), tensor.item()]))

tensor = torch.tensor(result)
print(tensor)

torch.save(tensor, "myDataset.pt")


# def optimize_this(x, y):
#     return math.sin(x + y / math.pi)
#
#
# distribution = []
#
# for i in range(1000):
#     x = random.uniform(-10, 10)
#     y = random.uniform(-10, 10)
#     distribution.append(((x, y), optimize_this(x, y)))
#
# print(distribution)
