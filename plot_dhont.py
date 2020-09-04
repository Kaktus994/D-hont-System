from matplotlib import pyplot as plt
import numpy as np


class DhontPlot:

	colour_list = ["b", "c", "r", "g", "m", "y", "yellow", "lime", "purple", "royalblue", "indigo", "orange"]

	def __init__(self, parties_list, mandate_dict):
		self.parties_list = parties_list
		self.mandate_dict = mandate_dict
		self.x_indices = np.arange(len(self.parties_list))

	def bar_plot(self):
		keys_array = np.fromiter(self.mandate_dict.keys(), dtype=float)
		values_array = np.fromiter(self.mandate_dict.values(), dtype=float)
		new_bar = plt.bar(keys_array, values_array)

		self.set_bar_colours(new_bar)

		plt.xticks(ticks=self.x_indices, labels=self.parties_list)
		plt.yticks(np.arange(0, max(self.mandate_dict.values())+4, 3.0))

		for i, value in enumerate(self.mandate_dict.values()):
			plt.text(x=i, y=value+0.5, s=f"{value}", fontdict=dict(fontsize=18))

		plt.ylim(0, max(self.mandate_dict.values()) * 1.15)
		plt.xlabel("PARTY NAME", fontsize=18, fontweight="bold")
		plt.ylabel("No. OF MANDATES", fontsize=18, fontweight="bold")
		plt.title("D'hont System", fontsize=25, fontweight="bold")

		plt.show()

	def set_bar_colours(self, bar):
		for key in self.mandate_dict:
			bar[key].set_color(self.colour_list[key])
