class A:
  def __init__(self, n, i):
    self.a=i
    self.b=n
    self.d=i
    self.e=n
  def B(self):
    for self.a in range(self.b):
      for self.d in range(self.e):
        print(self.a*self.d,end="\t")
      print(end="\n")

c=A(11, 1)
c.B()