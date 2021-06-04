def relu(z):
    return max(0,z)

def feed_forward(x, Wh, Wo):
    # Hidden layer
    Zh = x * Wh
    H = relu(Zh)

    # Output layer
    Zo = H * Wo
    output = relu(Zo)
    return output

result_1 = feed_forward(1,2,3)
result_2 = feed_forward(1,0.2,3)
print(result_1)
print(result_2)