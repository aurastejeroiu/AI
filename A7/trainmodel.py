import torch
from matplotlib import pyplot as plt

import myModel

data_set = torch.load("myDataset.pt")

print(data_set)

'''
B. in the file trainmodel.py:
1. Load the training data from the file mydataset.txt
Help function: torch.load
2. Following the example from file train_Batch.py declare and train your ANN
3. Save your trained network in file myNetwork.pt (there are several ways to
save/load a model, look at the example for the most used one)
'''

x = data_set.narrow(1, 0, 2)  # narrow(dimension, start, length) → Tensor
print(x)
y = data_set.narrow(1, 2, 1)
print(y)

# we set up the lossFunction as the mean square error
lossFunction = torch.nn.MSELoss()

# we create the ANN
ann = myModel.Net(n_feature=2, n_hidden=64, n_output=1)

print(ann)
# we use an optimizer that implements stochastic gradient descent
optimizer_batch = torch.optim.SGD(ann.parameters(), lr=0.02)

# we memorize the losses for some graphics
loss_list = []
avg_loss_list = []

# we set up the environment for training in batches
batch_size = 20
n_batches = int(len(x) / batch_size)
print(n_batches)

for epoch in range(10000):

    for batch in range(n_batches):
        # we prepare the current batch  -- please observe the slicing for tensors
        batch_x = x[batch * batch_size:(batch + 1) * batch_size]
        batch_y = y[batch * batch_size:(batch + 1) * batch_size]

        # we compute the output for this batch
        prediction = ann(batch_x)

        # we compute the loss for this batch
        loss = lossFunction(prediction, batch_y)

        # we save it for graphics
        loss_list.append(loss)

        # we set up the gradients for the weights to zero (important in pytorch)
        optimizer_batch.zero_grad()

        # we compute automatically the variation for each weight (and bias) of the network
        loss.backward()

        # we compute the new values for the weights
        optimizer_batch.step()

        # we print the loss for all the dataset for each 10th epoch
    if epoch % 100 == 99:
        y_pred = ann(x)
        loss = lossFunction(y_pred, y)
        print('\repoch: {}\tLoss =  {:.5f}'.format(epoch, loss))

    # Specify a path
filepath = "myNet.pt"

# save the model to file
torch.save(ann.state_dict(), filepath)

# make the plot
plt.plot(loss_list)
plt.savefig("loss.png")
#plt.show()

# visualise the parameters for the ann (aka weights and biases)
for name, param in ann.named_parameters():
    if param.requires_grad:
        print(name, param.data)
