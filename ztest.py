import statistics as stats
import pandas as pd 
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import random

df = pd.read_csv("medium_data.csv")
dataset = df["reading_time"].tolist()
sample_data = []
mean_list = []

population_mean = stats.mean(dataset)

#repeating process 100 times
for o in range(1, 100):
    #taking 30 random samples
    for i in range(1, 30):
        random_index = random.randint(0, len(dataset) - 1)
        random_value = dataset[random_index]
        sample_data.append(random_value)
        sampling_mean = stats.mean(sample_data)      
    mean_list.append(sampling_mean)

#standard deviation
standard_deviation = stats.stdev(mean_list)

#sample mean
sample_mean = stats.mean(mean_list)

#standard deviations
first_sd_start, first_sd_end = population_mean - standard_deviation, population_mean + standard_deviation
second_sd_start, second_sd_end = population_mean - (2 * standard_deviation), population_mean + (2 * standard_deviation)
third_sd_start, third_sd_end = population_mean - (3 * standard_deviation), population_mean + (3 * standard_deviation)

#graph of list of means
graph = ff.create_distplot([mean_list], ["List of means"], show_hist = False)

graph.add_trace(go.Scatter(x = [first_sd_start, first_sd_start], y = [0, 0.015], mode = "lines", name = "First sd start"))
graph.add_trace(go.Scatter(x = [first_sd_end, first_sd_end], y = [0, 0.015], mode = "lines", name = "First sd end"))

graph.add_trace(go.Scatter(x = [second_sd_start, second_sd_start], y = [0, 0.015], mode = "lines", name = "Second sd start"))
graph.add_trace(go.Scatter(x = [second_sd_end, second_sd_end], y = [0, 0.015], mode = "lines", name = "Second sd end"))

graph.add_trace(go.Scatter(x = [third_sd_start, third_sd_start], y = [0, 0.015], mode = "lines", name = "Third sd start"))
graph.add_trace(go.Scatter(x = [third_sd_end, third_sd_end], y = [0, 0.015], mode = "lines", name = "Third sd end"))

graph.show()

z_score = (sample_mean - population_mean)/standard_deviation

print("mean of sampling distribution: " + str(sampling_mean) + "\nstandard deviation of sampling distribution: " + str(standard_deviation) + "\nMean of sample1: " + str(mean_list[0]) + "\nThe z score is: " + str(z_score))