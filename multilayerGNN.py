from numpy import exp, array, random, dot, absolute, abs, sum, sort, reshape, delete,shape
from random import randint, choice


class Layer:
    def __init__(self,input,output):
        self.value=2 * random.random((input, output)) - 1
        self.error=0

    def mutate(self,p):
           for _ in xrange(p):#change a certain amount of items
                x = randint(0,len(self.value)-1)
                y = randint(0,len(self.value[x])-1)
                value= 2 * random.random()
                self.value[x][y] = value



class NeuralNetwork():
    def __init__(self):
        self.layers = 2
        self.error = [0, 0, 0, 0]
        w1 = Layer(3,5)
        w4 = Layer(5,1)
        self.bias = 2 * random.random()
        self.weights = [w1,w4]

    def sig(self, x):
        return 1 / (1 + exp(-x))

    def sig_der(self, x):
        return x * (1 - x)

    def mutate(self,x):
        for index in xrange(self.layers):
            self.weights[index].mutate(x)
            pass

    def think(self, input):
        output1 = self.sig(dot(input, self.weights[0].value) + self.bias) 
        output2 = self.sig(dot(output1, self.weights[1].value)  + self.bias)
         
        return [output1,output2]


class GNN():
    def __init__(self, in_, out_):
        self.layers = 2
        self.population = []
        self.maxkids=600
        self.maxTraining = 50
        self.in_ = in_
        self.out_ = out_
        self.sorted=[]
        self.acients=[]
        self.previousAverageError = 100000000000000000000000
        for net in xrange(self.maxkids):
            net = NeuralNetwork()
            self.population.append(net)  # creating a population

    def train(self):
        while self.maxTraining >=0 :
            self.evaluate()

    def print__(self):
        print(str(len(self.population))+' poplation length')
        for individual in self.population:
            print(individual)
            pass

    def mutate(self, p):
        for i in self.population:
            r = randint(1, 100)
            if r <= p:
                i.mutate(1)
         

    def best(self):
        #  self.error()
        return self.population[0]  #return the best after evelving

    def error(self):
        self.errors = []
        self.layers_weights = []

        for individual in self.population:

            output = individual.think(self.in_)
           
            error = 0
            deltaPrevious = []
            for q in xrange(self.layers):  ###loop through all the layers and get the error of each layer
                z = self.layers - 1 - q  #i wanna start from the output layer more like back propagation

                if z == self.layers - 1:  #looking for the last layer or output layer
                    error = self.out_ - output[z]
                else:
                    deltaPrevious = array(deltaPrevious)
                    error = deltaPrevious.dot(individual.weights[z + 1].value.T)
                    pass

                delta = error * individual.sig_der(output[z])
                
                deltaPrevious = delta
                
                for x in error:
                    for val in xrange(len(x)):
                        if x[val] < 0:
                            x[val] *= -1  ####check if the value is negative change it to positive
              
                finalError = sum(error)

             
                individual.weights[z].error = finalError  # append the errors to the error array
                #n self.population1 = sorted(self.population, key=lambda NeuralNetwork: NeuralNetwork.error)
            # for Layer in individual.weights:
            #     print(str(Layer.error)+'  layer error')
            self.sort()
           
            
    def sort(self):
        # now am gona arrange all the layers sepratly according to the least error
         layer=[]
         for x in xrange(self.layers):
            layekid=[]
            for individual in self.population:
                layekid.append(individual.weights[x])
                pass
            ##sort before appending
            
            layekid = sorted(layekid,key=lambda Layer:Layer.error)
            
           
            layer.append(layekid)#so now all layers are sorted time to create kids
         
         x = array(layer)
        #  print('\n'.join([''.join(['{:4}'.format(item.value) for item in row]) for row in layer]))
         
         x=x.T
        #  print('\n'.join([''.join(['{:4}'.format(item.value) for item in row]) for row in x]))
         
         self.sorted = x

         
    def evaluate(self):
        self.error()
        population = self.sorted
        self.population = [] #clear population
        # k everything till this part obviously works so lets see what i did wrong
        # print('\n'.join([''.join(['{:4}'.format(item.value) for item in row]) for row in population]))
         

        for x in xrange(int(len(population) * 0.3)):#get a percentage of the population as parents
            net = NeuralNetwork()#init a new net
            for index in xrange(self.layers):
                net.weights[index] = population[x][index]  #now i create new neaural nets by selecting the best layers as parents
                pass
            self.population.append(net)
            #ive added the best to the population
            #wanna add random paren ts to the mix they may have good genetical material 
        
        # print(str(len(self.population))+' len after first selection')
        
        # print(len(self.population))
        # print((int(len(population)*0.5)))
        while len(self.population) < (int(len(population)*0.8)):#while its not yet upto half of the lenth add random element
            x = random.randint(0,len(population))
            net = NeuralNetwork()#init a new net
            for index in xrange(self.layers):
                net.weights[index] = population[x][index]  #now i create new neaural nets by selecting the best layers as parents
                pass
            self.population.append(net)


        # print(str(len(self.population))+' len after second selection')
        
        
        #now am done selecting parent time for the hard part making kids(- _ o)
        population = self.population
        self.population=[]#clear the population
    

        for x in xrange(int(len(population) * 0.2)):#get a percentage of the population as parents
          self.population.append(population[x])


        while len(self.population) < self.maxkids:
            male = random.randint(0, len(population)-1)
            female = random.randint(0, len(population)-1)
            if male != female:
                male = population[male]
                female = population[female]
                # print(female.weight)
                # Breed them.
                babies = self.breed(male, female)

                for baby in babies:
                    self.population.append(baby)
                 
        self.maxTraining -= 1
        self.mutate(0)
        self.averageerror()
        

    def breed(self,male,female):
        children =[]
         
        # for x in xrange(self.layers):
        #     print(male.weights[x].value)

        for _ in xrange(2):
            child  = NeuralNetwork()
            # so am meant to join both of the together so first start with the layer
            for x in xrange(self.layers):
                # next go to the individual weights
                for y in xrange(len(child.weights[x].value)):
                    #  for z in xrange(len(child.weights[x].value[y])):
                    #     child.weights[x].value[y][z] = random.choice([male.weights[x].value[y][z] , female.weights[x].value[y][z] ])
                    #     child.bias = random.choice([male.bias , female.bias ])
                    #     pass



                    if _ == 0:
                        child.weights[x].value[y]=male.weights[x].value[y]
                        if len(child.weights[x].value[y]) == 1:
                            a=0
                            pass

                        else:
                            a = random.randint(0, len(child.weights[x].value[y])-1)
                            pass
                        
                        child.weights[x].value[y][a:]=female.weights[x].value[y][a:]
                        child.bias = random.choice([male.bias , female.bias ])
                        pass

                    else:
                        child.weights[x].value[y]=female.weights[x].value[y]
                        if len(child.weights[x].value[y]) == 1:
                            a=0
                            pass

                        else:
                            a = random.randint(0, len(child.weights[x].value[y])-1)
                            pass
                        
                        child.weights[x].value[y][a:]=male.weights[x].value[y][a:]
                        child.bias = random.choice([male.bias , female.bias ])
                        pass
                        pass
            children.append(child)
        return children


    def averageerror(self):
        errors = []
        for individual in self.population:

            o4 = individual.think( self.in_)
            error =  self.out_ - o4[individual.layers - 1]

            for x in error:
                if x < 0:
                    x *= -1
                    pass
                pass 

            errors.append(sum(error))
        pass
        finalerror =  sum(errors)
        if False:
            self.population =self.acients
            print('redo!!')
            # self.mutate(60)
            self.evaluate()
        
        else:
            self.previousAverageError =finalerror
            self.acients = self.population
            print(str(finalerror) +'  general error')
            pass
            pass


        

         


def main():

    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T
    # result=[]

    # with open('datasets/diabetes.txt') as f:
    #     result = [line.rstrip('\n').split(',') for line in f]

    # result=array(result,dtype=float)

    # y=[]
    # for r in result:
    #     y.append(r[len(result[0])-1])

    # y=array(y,dtype=float)
    # training_set_outputs=reshape(y,(1,len(result))).T

    # training_set_inputs=delete(result,len(result[0]) - 1,1)
    # training_set_inputs = array(training_set_inputs)

    # net.train(training_set_inputs, training_set_outputs, 10000)

    # print "New synaptic weights after training: "
    # print net.weight

    # print "Considering new situation [5.2,4.1,1.5,0.1] -> ?: "
    # o1,o2,o3,o4 = net.think(array([1,189,60,23,846,30.1,0.398,59]))
    # print o4

    gnn = GNN(training_set_inputs, training_set_outputs)
    gnn.train()


  
    print "Considering new situation [0, 0, 0] -> ?: "
    fullerror=[]
    for indicidual in gnn.population:
        val =indicidual.think(array([0, 0, 0]))
        fullerror.append(val[gnn.layers-1][0])
        pass

    print(sum(fullerror)/len(gnn.population))
 

if __name__ == '__main__':
    main()
