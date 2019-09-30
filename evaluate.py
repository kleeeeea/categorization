import sys
from kleeeeea_helper.file import get_line_count
import numpy
import pandas as pd
from sklearn.metrics import precision_recall_curve, average_precision_score
from sklearn.metrics import classification_report

categorization_file = ''
if len(sys.argv) > 1:
    categorization_file = sys.argv[1]

label_file = ''
if len(sys.argv) > 2:
	label_file = sys.argv[2]

def get_medical_groundtruth(categorization_file):
	labels = numpy.zeros(get_line_count(categorization_file))
	# set the last num_ml_dl_documents documents labels to be 1

	medical_ml_file = '/home/klee/data/concept_medical/ml_and_anesthesia.txt'
	medical_dl_file = '/home/klee/data/concept_medical/dl_and_anesthesia.txt'
	num_ml_dl_documents = get_line_count(medical_ml_file) + get_line_count(medical_dl_file)
	labels[-num_ml_dl_documents:] = 1
	return labels


if label_file:
	# todo: add support for label_file
	pass
else:
	ground_truth_label = get_medical_groundtruth(categorization_file)

categorization_numpy = pd.read_csv(categorization_file, sep=' ', header=None).values
predicted_label = categorization_numpy.argmax(axis=1)
predicted_score = categorization_numpy[:,1] / (categorization_numpy.sum(axis=1) + numpy.finfo(float).eps)

print(precision_recall_curve(ground_truth_label, predicted_score))
print(average_precision_score(ground_truth_label, predicted_score))
print(classification_report(ground_truth_label, predicted_label))
# read

# confidence intervals, gradient, Reinforcement