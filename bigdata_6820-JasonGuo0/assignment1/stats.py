def variance(Heights_array):
  sum_of_heights = 0.0
  for i in range(len(Heights_array)):
    sum_of_heights += Heights_array[i]
  
  mean = sum_of_heights/len(Heights_array)
  print("The mean of the heights is: ", mean)
  sum_diffsq = 0.0
  for i in range(len(Heights_array)):
    sum_diffsq += (Heights_array[i]-mean)**2

  variance = sum_diffsq/(len(Heights_array)-1)
  print("The variance of the heights is: ", variance)

  print("Whether the variance is greater than 0.01 or not:", variance > 0.01)
  
variance(Heights_array)