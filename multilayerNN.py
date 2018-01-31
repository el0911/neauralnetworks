from numpy import exp, array, random, dot, absolute, abs, sum, sort,reshape,delete ,shape
from random import randint,choice


class NeuralNetwork():
    def __init__(self):
        random.seed(1)
        self.weight = 2 * random.random((8, 10)) - 1
        self.weight2 = 2 * random.random((10, 4)) - 1
        self.weight3 = 2 * random.random((4,4)) - 1
        self.weight4 = 2 * random.random((4, 1)) - 1


    def sig(self,x):
        return 1/(1 + exp(-x))


    def sig_der(self,x):
        return x * ( 1 - x )


    def train(self,input,e_output,itterations):
        for itteration in xrange(itterations):
            output1,output2,output3,output4 = self.think(input)

                    # layer 4
            error_layer4 = e_output - output4
            delta4 = error_layer4 * self.sig_der(output4)  #adjustment is the error mul by the input and sigmoid derivative of the output
            
                #layer 3
            error_layer3 = delta4.dot(self.weight4.T)
            delta3=error_layer3 * self.sig_der(output3)

               #layer 2
            error_layer2 = delta3.dot(self.weight3.T)
            delta2=error_layer2 * self.sig_der(output2)

               #layer 1
            error_layer1 = delta2.dot(self.weight2.T)
            delta1=error_layer1* self.sig_der(output1)


            adjusment1 = input.T.dot(delta1)
            adjusment2 = output1.T.dot(delta2)
            adjusment3 = output2.T.dot(delta3)
            adjusment4 = output3.T.dot(delta4)
            
            
            self.weight += adjusment1
            self.weight2 += adjusment2
            self.weight3 += adjusment3
            self.weight4 += adjusment4


    def think(self, input):
        output1 = self.sig(dot(input ,self.weight))
        output2 = self.sig(dot(output1 ,self.weight2))
        output3 = self.sig(dot(output2 ,self.weight3))
        output4 = self.sig(dot(output3 ,self.weight4))
       # print(str(shape(output1))+'  shape')
        return output1,output2,output3,output4



def main():
    net = NeuralNetwork()
    print "Random starting synaptic weights: "
    print net.weight

    training_set_inputs = array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1], [0, 0, 0]])
    training_set_outputs = array([[0, 1, 1, 1, 1, 0, 0]]).T



    result=[]

    with open('datasets/diabetes.txt') as f:
        result = [line.rstrip('\n').split(',') for line in f]


    result=array(result,dtype=float)

    
    y=[]
    for r in result:
        y.append(r[len(result[0])-1])


    y=array(y,dtype=float)
    training_set_outputs=reshape(y,(1,len(result))).T

    training_set_inputs=delete(result,len(result[0]) - 1,1)
    training_set_inputs = array(training_set_inputs)

    net.train(training_set_inputs, training_set_outputs, 10000)

    print "New synaptic weights after training: "
    print net.weight

    print "Considering new situation [5.2,4.1,1.5,0.1] -> ?: "
    o1,o2,o3,o4 = net.think(array([10,139,80,0,0,27.1,1.441,57]))
    print o4

    # net.train(training_set_inputs, training_set_outputs, 1000)

    # print "New synaptic weights after training: "
    # print net.weight

    # print "Considering new situation [0, 0, 0] -> ?: "
    # o1,o2,o3,o4 = net.think(array([0, 0, 1]))

    # print o4
    

if __name__ == '__main__':
    main()




    
    

    