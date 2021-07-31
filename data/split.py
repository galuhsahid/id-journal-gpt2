import random
from math import floor

random.seed(4)

def randomize_files(file_list):
    random.shuffle(file_list)

def get_training_and_testing_sets(file_list):
    split = 0.9
    split_index = floor(len(file_list) * split)
    training = file_list[:split_index]
    testing = file_list[split_index:]
    return training, testing

if __name__ == "__main__":
    file_name = "data/cleaned/all.txt"

    with open(file_name, 'r') as fr:
        lines = fr.readlines()

    randomize_files(lines)
    train, val = get_training_and_testing_sets(lines)

    with open("data/train.txt", "a") as f:
        for line in train:
            f.write(line.strip("\n") + "\n")

    with open("data/val.txt", "a") as f:
        for line in val:
            f.write(line.strip("\n") + "\n")
