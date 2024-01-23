import splitfolders

input_fold_path = "/home/daniel/software/visualInspectionPopcorn/data/annotated_data"
splitfolders.ratio(input_fold_path, output="/home/daniel/software/visualInspectionPopcorn/data/split_data",
    seed=1337, ratio=(.8, .2, .0), group_prefix=None, move=False)