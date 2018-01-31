from numpy import exp, array, random, dot, absolute, abs, sum, sort
from random import randint,choice



class NeuralNetwork():
    def __init__(self):
        # random.seed(1)
        self.weight = 2 * random.random((3, 1)) - 1
        self.error = 0
        
        

    def sig(self, x):
        return 1 / (1 + exp(-x))

    def sig_der(self, x):
        return x * (1 - x)

    
    def mutate(self):
        x= 2 * random.random()
        r1 = x
        r2 = randint(0,3-1)
        self.weight[r2] = r1


    def train(self, input, e_output, itterations):
        for itteration in xrange(itterations):
            output = self.think(input)
            error = e_output - output
            adjust = dot(
                input.T, error * self.sig_der(output)
            )  #adjustment is the error mul by the input and sigmoid derivative of the output
            self.weight += adjust

    def think(self, input):
        return self.sig(dot(input, self.weight))


class GNN():
    def __init__(self,in_,out_):

        self.population = []
        self.in_ = in_
        self.out_ = out_

        for net in xrange(1000):
            net = NeuralNetwork()
            self.population.append(net)  # creating a population

    def error(self):

        self.errors = []

        for individual in self.population:

            output = individual.think( self.in_)
            error =  self.out_ - output

            for x in error:
                if x < 0:
                    x *= -1
                    pass
                pass 

            individual.error = sum(error)
        pass



        self.population = sorted(self.population, key=lambda NeuralNetwork: NeuralNetwork.error)

        
        # for individual in self.population:
        #     print(individual.error)
        #     pass
    pass


    def evaluate(self):
        self.error()#arranges population in terms of error 
        population=self.population
        self.population = [] #empty population  (kill  them all!!!!)


        for index in xrange(200):# add a new set of individuals to population from first 350
            self.population.append(population[index])
            pass ## now population holds the parents 
        
        population = [] #empty population
        parent = 0
    

        for index in xrange(10):# add first 100 to the population from parents
            population.append(self.population[index])
            pass

         # For those we aren't keeping, randomly keep some anyway.
        for individual in self.population:
            if 10 > random.random():
                if len(population) < 300:
                    population.append(individual)
                    pass


        while len(population)  <  1000: # keep making kids till we reach 1000
             # Get a random mom and dad.
            male = random.randint(0, len(self.population)-1)
            female = random.randint(0, len(self.population)-1)

            # Assuming they aren't the same network...
            if male != female:
                male = self.population[male]
                female = self.population[female]
                # print(female.weight)
                # Breed them.
                babies = self.breed(male, female)

                # Add the children one at a time.
                for baby in babies:
                    # Don't grow larger than desired length.
                    if len(population)  <  1000:
                        population.append(baby)
            pass

        
        self.population = population
        self.mutate(10)
        self.average_error()

       
    def train(self):
        for index in xrange(50):
            self.evaluate()


    def print__(self):
        for individual in self.population:
            print(individual.weight)
            pass


    def average_error(self):
        errors = []
        for individual in self.population:

            output = individual.think( self.in_)
            error =  self.out_ - output

            for x in error:
                if x < 0:
                    x *= -1
                    pass
                pass 

            errors.append(sum(error))
        pass
        print(sum(errors))

    def mutate(self,p):
        for i in self.population:
            r  = randint(1,100)
            if r <= p:
                i.mutate()


    def breed(self, mother, father):
      
        children = []
        for _ in xrange(2):

            child =  NeuralNetwork()
            r2 = randint(0,3-1)
            
            for x in xrange(len(child.weight)):
                 child.weight[x]=random.choice( [mother.weight[x][0], father.weight[x][0]] )
           
            children.append(child)

            

        return children


    def best(self):
        self.error
        return self.population[0] #return the best after evelving


def main():
    # net = NeuralNetwork()
    # print "Random starting synaptic weights: "
    # print net.weight

    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T


    # result=[]

    # with open('datasets/iris.txt') as f:
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

    # print "Considering new situation [1, 0, 0] -> ?: "
    # print net.think(array([1, 0, 0]))

    gnn = GNN(training_set_inputs, training_set_outputs)
    gnn.train()
    ans = gnn.best()


    print "New synaptic weights after training: "
    print ans.weight

    print "Considering new situation [1, 0, 0] -> ?: "
    print ans.think(array([0, 0,0]))

  

if __name__ == '__main__':
    main()
