from imageai.Prediction.Custom import CustomImagePrediction
import os
import glob

directory = 'models'
execution_path = os.getcwd()

prediction = CustomImagePrediction()
prediction.setModelTypeAsResNet()
#for i in range (0,100):
	#prediction.setModelPath(os.path.join(execution_path, str(i)+'.h5'))  
prediction.setModelPath(os.path.join(execution_path, 'model_ex-100_acc-1.000000.h5'))       
prediction.setJsonPath(os.path.join(execution_path, "model_class.json"))
prediction.loadModel(num_objects=4)

predictions, probabilities = prediction.predictImage(os.path.join(execution_path, "img7"), result_count=4)


#for eachPrediction, eachProbability in zip(predictions1, probabilities1):
#    print(eachPrediction , " : " , eachProbability)


for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)
