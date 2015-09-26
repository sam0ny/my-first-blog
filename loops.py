## This functiion just says hi to the user when the person enters

def hi(name):
    print('Hi ' + name + '!')

girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
   hi(name)
   print('Next girl')

for i in range(len(girls)):
    print(girls[i])