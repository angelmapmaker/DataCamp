# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())


# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))

# Numpy is imported, seed is set
import numpy as np 
# Starting step
step = 50

#Determine your next move
#In the Empire State Building bet, your next move depends on the number of eyes you throw with the dice. We can perfectly code this with an if-elif-else construct!
#The sample code assumes that you're currently at step 50. Can you fill in the missing pieces to finish the script? numpy is already imported as np and the seed has been set to 123, so you don't have to worry about that anymore.

# Roll the dice
dice=np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice>=3 and dice <=5 :
    step = step + 1
else  :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice, step )


#Make a list random_walk that contains the first step, which is the integer 0.
#Finish the for loop:
#The loop should run 100 times.
#On each iteration, set step equal to the last element in the random_walk list. You can use the index -1 for this.
#Next, let the if-elif-else construct update step for you.
#The code that appends step to random_walk is already coded.
#Print out random_walk

# Numpy is imported, seed is set
import numpy as np 
# Initialize random_walk
random_walk=[0]

# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step=random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

#How low can you go?
#Things are shaping up nicely! You already have code that calculates your location in the Empire State Building after 100 dice throws. However, there's something we haven't thought about - you can't go below 0!
#A typical way to solve problems like this is by using max(). If you pass max() two arguments, the biggest one gets returned. For example, to make sure that a variable x never goes below 10 when you decrease it, you can use:
# x = max(10, x - 1)
# Numpy is imported, seed is set
import numpy as np
# Initialize random_walk
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0,step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

print(random_walk)


#Visualize the walk
#Let's visualize this random walk! Remember how you could use matplotlib to build a line plot?
#import matplotlib.pyplot as plt
#plt.plot(x, y)
#plt.show()
#The first list you pass is mapped onto the x axis and the second list is mapped onto the y axis.
#If you pass only one argument, Python will know what to do and will use the index of the list to map onto the x axis, and the values in the list onto the y axis.

# Numpy is imported, seed is set

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)
plt.show()

# Show the plot
