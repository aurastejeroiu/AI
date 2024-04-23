import math

import torch
from PIL import Image


from exampleCV import *

# we load the model

filepath = "cifar10model_65.model"
ann = SimpleNet(num_classes=10)

if cuda_avail:
    model.cuda()

optimizer = Adam(model.parameters(), lr=0.001,weight_decay=0.0001)
loss_fn = nn.CrossEntropyLoss()

image =  Image.open('f1.jpg')
label = 1

ann.load_state_dict(torch.load(filepath))
ann.eval()

# if cuda_avail:
#         image = Variable(image.cuda())
#         label = Variable(label.cuda())

#Predict classes using images from the test set
outputs = model(image)
_,prediction = torch.max(outputs.data, 1)





# # visualise the parameters for the ann (aka weights and biases)
# for name, param in ann.named_parameters():
#     if param.requires_grad:
#         print(name, param.data)

# x = float(input("x = "))
# y = float(input("y = "))
# x = y = float(2)

# x = torch.tensor([x])
# y = torch.tensor([y])
# real = (x + y / math.pi).item()
# predicted = ann(torch.tensor([x, y])).tolist()[0]
# real = torch.sin(x + y / math.pi).item()
print("predicted: ", prediction)
# print("real: ", real)
# print("difference: ", abs(predicted - real))
