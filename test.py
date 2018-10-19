import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

from voxel_data_generator import VoxelDataGenerator


def main(data, label):
    # flip
    c1 = VoxelDataGenerator(flip_axis=2)
    g1 = c1.build(data, batch_size=1)

    # shift
    c2 = VoxelDataGenerator(shift_axis=1, shift_range=0.3)
    g2 = c2.build(data, batch_size=1)

    # zoom
    c3 = VoxelDataGenerator(zoom_axis=1, zoom_range=1.5)
    g3 = c3.build(data, batch_size=1)

    # rotate
    c4 = VoxelDataGenerator(rotate_axis=1, rotate_angle=45)
    g4 = c4.build(data=data, batch_size=1)

    # visualize
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.voxels(next(g4)[0], edgecolor='k')

    plt.show()

    # take label as arugment. The generator returns data and label when it is called.
    c5 = VoxelDataGenerator(flip_axis=1)
    g5 = c5.build(data=data, label=label, batch_size=32)


if __name__ == '__main__':
    # data load : here you need to load array data
    all_data = np.load('./modelnet10.npz')
    data = all_data['X_train']
    label = all_data['y_train']

    main(data, label)
