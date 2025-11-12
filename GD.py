# 🎯 Gradient Descent to find local minima of y = (x + 3)^2

# Function and its derivative
def f(x):
    return (x + 3)**2

def df(x):
    return 2 * (x + 3)

# Initial parameters
x = 2                 # starting point
learning_rate = 0.1   # step size
iterations = 25       # number of iterations

print("Iteration\tX value\t\tFunction Value")

for i in range(iterations):
    grad = df(x)
    x = x - learning_rate * grad   # update rule
    print(f"{i+1}\t\t{x:.6f}\t\t{f(x):.6f}")

print("\nLocal minima occurs at x =", round(x, 3))