import splitfolders

input_fold_path = "/home/daniel/catkin_ws/src/josh_vision/data/all_data"
splitfolders.ratio(input_fold_path, output="/home/daniel/catkin_ws/src/josh_vision/data/split_data",
    seed=1337, ratio=(.8, .2, .0), group_prefix=None, move=False)