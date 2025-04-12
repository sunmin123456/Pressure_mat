import numpy as np
import pandas as pd


def weighting_sum_ratio(my_array):
    hist, bin_edges = np.histogram(my_array, bins=range(0, 1025))

    i = 0
    weight_sum = 0
    while i < len(hist):
        weight_sum = hist[i] * i + weight_sum
        i += 1

    threshold_ratio = 0.99
    add_value = 0.01
    threshold_list = []

    while threshold_ratio > 0.89:
        weight_small = weight_sum * threshold_ratio
        j = 1023
        threshold = 0
        weight = 0

        while j > 0:
            weight = hist[j] * j + weight
            if weight >= weight_small:
                threshold = j
                break
            j = j - 1

        threshold_list.append(threshold)
        threshold_ratio = threshold_ratio - add_value
    return np.array(threshold_list)


if __name__ == "__main__":

    face_up_data_path = './20200113wholeFaceUp.csv'
    face_up_data = pd.read_csv(face_up_data_path).to_numpy()

    face_up_threshold_array = np.zeros((1800, 10))
    face_up_count = 0
    while face_up_count < len(face_up_threshold_array):
        face_up_threshold_array[face_up_count] = weighting_sum_ratio(face_up_data[face_up_count][:220])
        face_up_count = face_up_count + 1

    face_up_df = pd.DataFrame(face_up_threshold_array)
    face_up_df.to_excel('./20200114wholeFaceUpThresholdV1.1.xlsx')