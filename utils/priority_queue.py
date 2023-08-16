#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch


class BinaryHeap():
    radius = 1
    spacing = 4 * radius
    color = "blue"
    hl1 = "green"
    hh2 = "red"

    def __init__(self, type=None):
        self.heap = []
        self.map = {}
        self.len = 0
        if type:
            self.type = type
        else:
            self.type = "min"

    def heap_condition(self, parent, index):
        return self.heap[parent] <= self.heap[index] \
                if self.type == "min" else\
                self.heap[parent] >= self.heap[index]

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2],\
                self.heap[index1]

    def bubble(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if index % 2 == 0:
            if not self.heap_condition(index-1, index):
                self.swap(index-1, index)
                index = index-1
        if not self.heap_condition(parent, index):
            self.swap(parent, index)
            self.bubble(parent)

    def push(self, elements):
        if type(elements) == list:
            for element in elements:
                self.heap.append(element)
                self.bubble(self.len)
                self.len += 1
        else:
            self.heap.append(elements)
            self.bubble(self.len)
            self.len += 1

    def draw(self):

        height = np.ceil(np.log2(self.len + 1)) * BinaryHeap.spacing
        offset = np.ceil(np.log2(self.len + 1)) * BinaryHeap.spacing
        # Create a figure and axis for plotting
        fig, ax = plt.subplots()
        border = 1
        level = 0
        off_table = []

        offset = 2 ** (np.ceil(np.log2(self.len + 1))) * 2 * BinaryHeap.radius
        cur_off = offset
        visited = []
        for index, node in enumerate(self.heap):
            if index in visited:
                continue
            parent = (index - 1) // 2
            if index + 1 == border:
                l_off = cur_off // 4
                border *= 2
                level += 1
                cur_off = cur_off // 2
            else:
                l_off += cur_off

            node = plt.Circle((l_off,
                               height - level * BinaryHeap.spacing),
                              BinaryHeap.radius, linewidth=2,
                              edgecolor='black',
                              facecolor=BinaryHeap.color)
            ax.add_patch(node)
            ax.text(l_off, height - level * BinaryHeap.spacing,
                    self.heap[index], fontsize=10, ha='center', color='white')
            off_table.append(np.array(
                [l_off, height - level * BinaryHeap.spacing]))
            if index != 0:
                con = ConnectionPatch(xyA=off_table[parent]
                                      + (0, -BinaryHeap.radius),
                                      xyB=off_table[index]
                                      + (0, BinaryHeap.radius),
                                      coordsA="data", coordsB="data",
                                      arrowstyle="-|>", mutation_scale=15,
                                      color="black")
                ax.add_patch(con)

            visited.append(index)
        # Set the aspect ratio and axis limits
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim(0, offset // 2)
        ax.set_ylim(-2 * BinaryHeap.radius, height)

        # Remove axis ticks and labels
        ax.axis('off')

        # Show the camera icon
        plt.title("Heap")
        plt.show()


def main():
    h = BinaryHeap()
    # h.push([2, 40, 2, 40, 1, 4, 1, 3, 4, 5])
    h.push([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    h.draw()


if __name__ == "__main__":
    main()
