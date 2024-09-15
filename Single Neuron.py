class Neuron:
  def fit(self,x,w,b):
    """
    This is the fit function of the Neuron that takes the inputs and the weights as well as the bias as a custom parameter
    """
    self.x = x
    self.w = w
    self.b = b
    if len(self.x) != len(self.w):
      print("The number of inputs and weights should be same")
    else:
      inp = [i for i in self.x]
      weights = [j for j in self.w]
      c = 0
      for l in range(len(inp)):
        c = c + (inp[l]*weights[l])
      c = c+self.b
      print(c)
n1 = Neuron()
print(n1.fit.__doc__)
n1.fit([1,2,3],[0.001,0.005,0.2],3)