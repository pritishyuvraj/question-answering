from pprint import pprint 
import sys 
import re 
import matplotlib.pyplot as plt

class plot_diagrams:
	def __init__(self, fileName):
		self.fileName = fileName
		# self.extract_write_to_csv('f1', self.fileName)
		self.plot_diagrams_from_csv("f1_score.csv")

	def plot_diagrams_from_csv(self, fileName):
		read_file = open(fileName, 'r').read().split('\n')
		x_axis = []
		y_axis = []
		for index, line in enumerate(read_file):
			line = line.split(',')
			y_axis.append(float(line[1]))
			x_axis.append(float(index))
		plt.plot(y_axis)
		plt.ylabel('F1 Score')
		plt.xlabel('iterations')
		plt.show()

	def find_index(self, line, keyword):
		for index_i, word in enumerate(line):
			if keyword in word:
				return index_i

	def extract_num(self, line):
		match = re.search(r'\(?([0-9.]+)\)?', line)
		return match.group(1)

	def extract_alpha(self, alpha):
		match = re.search(r'\(?([a-zA-Z]+)\)?', alpha)
		return match.group(1)

	def extract_write_to_csv(self, keyword = None, fileName = None):
		read_file = open(fileName, "r").read().split('\r')

		for line in read_file:
			# print line
			pprint (line)
			try:
				if keyword in line:
					line = line.split(":")
					# pprint (line)
					# index = line.index(keyword)
					index = self.find_index(line, keyword)
					print index, line[index]
					value = self.extract_num(line[index+1])
					text = str(self.extract_alpha(line[index])) + ", " + str(value) + "\n"
					print "Text is ->", text
					self.append_to_file("f1_score.csv", text)
			except:
				print sys.exc_info()

	def append_to_file(self, fileName, variable):
		with open(fileName, "a") as myfile:
			myfile.write(variable)

if __name__ == '__main__':
	plot = plot_diagrams('../bidaf-pytorch-3635382.err')

