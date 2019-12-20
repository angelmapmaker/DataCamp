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
