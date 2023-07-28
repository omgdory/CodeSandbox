# Following the "sentdex" YouTube channel's tutorial
# Attempt to recreate the basic parts of a Neural Network
# To practice methodology for future Neural Network projects
# "https://www.youtube.com/watch?v=Wo5dMEP_BbI"

import numpy as np

inputs = [1,2,3, 2.5]
weights1 = [0.2,0.8,-0.5, 1.0]
weights2 = [0.5, -0.91, 0.26, -0.5]
weights3 = [-0.26, -0.27, 0.17, 0.87]

bias, bias2, bias3 = 2, 3, 0.5

output = 0
for i in range(len(inputs)):
    output += inputs[i]*weights[i]
output += bias

print(output)
