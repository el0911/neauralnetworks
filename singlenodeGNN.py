from numpy import exp, array, random, dot


class NeuralNetwork():
    def __init__(self):
        random.seed(1)
        self.weight = 2 * random.random((3, 1)) - 1


    def sig(self,x):
        return 1/(1 + exp(-x))


    def sig_der(self,x):
        return x * ( 1 - x )


    def train(self,input,e_output,itterations):
        for itteration in xrange(itterations):
            output = self.think(input)
            error = e_output - output
            adjust = dot(input.T , error * self.sig_der(output) )   #adjustment is the error mul by the input and sigmoid derivative of the output
            self.weight += adjust


    def think(self, input):
        return self.sig(dot(input ,self.weight))



class GNN():
    def __init__(self):
        self.population = []

        for net in xrange(1000):
            net = NeuralNetwork()
            self.population.append(net) # creating a population
           
    def error(self,input,e_output):
        
        self.errors=[]

        for individual in self.population:
                
                output = individual.think(input)
                error = e_output - output
                # if error<0:
                #     error *= -1
                #     pass
                abs(error)
                self.errors.append(error)
               
        pass
        return self.errors
    pass


def main():
    # net = NeuralNetwork()
    # print "Random starting synaptic weights: "
    # print net.weight

    training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
    training_set_outputs = array([[0, 1, 1, 0]]).T

    # net.train(training_set_inputs, training_set_outputs, 10000)

    # print "New synaptic weights after training: "
    # print net.weight

    # print "Considering new situation [1, 0, 0] -> ?: "
    # print net.think(array([1, 0, 0]))

    gnn = GNN()
    print(gnn.error(training_set_inputs,training_set_outputs))


    

if __name__ == '__main__':
    main()




    
    

    