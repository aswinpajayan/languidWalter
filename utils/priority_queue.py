#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch


class BinaryHeap():
    radius = 1
    spacing = 2 * radius
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
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def bubble(self, index):
        if index == 0:
            return
        parent = (index - 1) // 2
        if not self.heap_condition(parent, index):
            self.swap(parent, index)
            self.bubble(parent)

    def push(self, element):
        self.heap.append(element)
        self.bubble(self.len)
        self.len += 1
        print(self.heap, self.len)

    def draw(self):

        height = np.ceil(np.log2(self.len + 1)) * BinaryHeap.spacing
        offset = np.ceil(np.log2(self.len + 1)) * BinaryHeap.spacing
        # Create a figure and axis for plotting
        fig, ax = plt.subplots()
        border = 1
        level = 1

        cur_off = np.ceil(np.log2(self.len + 1))

        levels = np.log2(self.len + 2)
        visited = []
        for index, node in enumerate(self.heap):
            if index in visited:
                continue
            parent = index - 1 // 2
            # Draw edges 
            # if index % 2 == 1:
            #     # left node
            #     node = plt.Circle((offset - (index // 2) * BinaryHeap.spacing,
            #                        height - (index // 2) * BinaryHeap.spacing),
            #                       BinaryHeap.radius, linewidth=2,
            #                       edgecolor='black',
            #                       facecolor=BinaryHeap.color)
            #     con = ConnectionPatch(xyA=(height, offset),
            #                           xyB=(0.5, 0.75),
            #                           coordsA="data", coordsB="data",
            #                           arrowstyle="-|>", mutation_scale=15,
            #                           color="black")
            # else:
            #     if index != 0:
            #         con = ConnectionPatch(xyA=(height, offset),
            #                               xyB=(0.5, 0.75),
            #                               coordsA="data",
            #                               coordsB="data",
            #                               arrowstyle="-|>", mutation_scale=15,
            #                               color="black")
            #     node = plt.Circle((offset + (index // 2) * BinaryHeap.spacing,
            #                        height - (index // 2) * BinaryHeap.spacing),
            #                       BinaryHeap.radius, linewidth=2,
            #                       edgecolor='black',
            #                       facecolor=BinaryHeap.color)

            if index + 1 == border:
                l_off = cur_off // 2
                border *= 2
                level += 1
                cur_off = cur_off // 2
            else:
                l_off += cur_off
            print(index, l_off,  level, border, cur_off)

            node = plt.Circle((l_off,
                               (height - level) * BinaryHeap.spacing),
                              BinaryHeap.radius, linewidth=2,
                              edgecolor='black',
                              facecolor=BinaryHeap.color)
            con = ConnectionPatch(xyA=(height, offset),
                                  xyB=(0.5, 0.75),
                                  coordsA="data", coordsB="data",
                                  arrowstyle="-|>", mutation_scale=15,
                                  color="black")

            ax.add_patch(node)
            ax.text(l_off, (height - level) * BinaryHeap.spacing, self.heap[index], fontsize=10, ha='center', color='white')
            visited.append(index)
        # Set the aspect ratio and axis limits to make the icon look like a camera
        ax.set_aspect('equal', adjustable='box')
        ax.set_xlim(-20, 20)
        ax.set_ylim(-20, 20)

        # Remove axis ticks and labels
        ax.axis('off')

        # Show the camera icon
        plt.title("Heap")
        plt.show()


def main():
    h = BinaryHeap()
    h.push(10)
    h.push(3)
    h.push(20)
    h.push(2)
    h.push(40)
    h.push(1)
    h.draw()


if __name__ == "__main__":
    main()
