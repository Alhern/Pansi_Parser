# Pansi_Parser

This program parses ANSI C, Python and Lisp files.
This helps document the code and make it more readable.

Pansi_Parser extracts the following information from the files:
* global symbols definitions
* variables
* functions
* the number of the lines where they appear

## Usage
You have to pass the path of the file you want to parse as an argument.
Only the following file extensions are supported:
* .c
* .py
* .lisp

Example with an ANSI C file:
```
$ ./pparser.py tools.c
Now parsing your C file...

        Global variables:
0001: Included file: tools.h
0004: Function: int randomInt(int min, int max)
0009: Function: float randomFloat(float min, float max)
0017: Function: int countLines(char * filename)
0036: Function: void vectorMalloc(int size, int idx[])
0064: Function: void convertLabel(char * label, char * token)
0079: Function: void dataVectorInit(char * filename, int linesNum)
0117: Function: void normCalc(int idx)
0127: Function: void normalize(int lines)
0140: Function: void mapInit()
0173: Function: void shuffle_vects(int * vector, int n)
0186: Function: float get_distance(float * weight_vector, float * input_vector)
0197: Function: void add_to_list(BMU * bmu_list, int row, int col)
0214: Function: void delete_list(BMU ** bmu_list)
0229: Function: BMU pick_winner(BMU * bmu_list)
0270: Function: BMU get_BMU(Neural_net * map, Data_vector * data)
0332: Function: void scale_neighborhood(Neural_net * map, BMU bmu, int radius, int idx, float alpha)
0352: Function: void map_training(Neural_net * map, Data_vector * data, int linesNum, float alpha, int iter, int * idxs)
0380: Function: void label_map(Neural_net * map, Data_vector * data, int linesNum)
0402: Function: void display_map(Neural_net * map)
0423: Function: void usage(char * message)
0430: Function: void showData(int lines, Data_vector * data_vector)
0443: Function: void print_map(Neural_net * map)

        Usage of global variables:
```

Example with a Python file:
```
$ ./pparser.py /mnt/c/Users/audel/Desktop/Github/TSA/model.py
Now parsing your PYTHON file...

        Global variables:
0069: Variable: TRAINING_DATASET_PATH = "data/training.1600000.processed.noemoticon.csv"
0072: Function: import_dataset()
0096: Function: preprocess(tweet)
0125: Function: postprocess(data, n=1600000)
0140: Variable: N_DIM = 300
0141: Variable: WINDOWS = 5
0142: Variable: SG = 0
0143: Variable: MIN_COUNT = 10
0148: Function: w2vmodel_builder(data)
0166: Function: save_w2vmodel(model, filename)
0173: Function: load_w2vmodel(filename)
0188: Function: build_word_vector(w2v_model, tfidf, tokens, size)
0205: Function: build_training_sets(x_set, w2v_model, tfidf)
0219: Function: build_model()
0236: Variable: EPOCHS = 30
0237: Variable: BATCH_SIZE_TRAIN = 1024
0238: Variable: VALIDATION_SPLIT = 0.1
0239: Variable: VERBOSE_TRAIN = 2
0244: Variable: BATCH_SIZE_TEST = 1024
0245: Variable: VERBOSE_TEST = 2
0248: Function: train_model(model, train_vec, y_train, test_vec, y_test)
0291: Function: engine(save_Model=False, save_W2v=False, save_Tfidf=False)
0342: Function: load_models(model_config_path, model_weights_path, w2v_path, tfidf_path)

        Global variables usage:
TRAINING_DATASET_PATH : [73]
N_DIM : [150, 206]
WINDOWS : [150]
SG : [150]
MIN_COUNT : [150]
EPOCHS : [251]
BATCH_SIZE_TRAIN : [251]
VALIDATION_SPLIT : [251]
VERBOSE_TRAIN : [251]
BATCH_SIZE_TEST : [254]
VERBOSE_TEST : [254]
```

Example with a Lisp file:
```$ ./pparser.py sysexp.lisp
Now parsing your LISP file...

        LISP functions:
0019: apply-rule (rule rules)
0033: verify-premises (prémisses)
0067: get-basic-value (prop &aux base read)
0081: put (symbole attribut valeur)
0101: conclusions (rule rules)
0125: find-rule (rule rules)
0189: update-bdf (premisses)
0203: get-premisses (rule rules)
0239: update-bdf (liste)
0244: flush-bdf (liste)
0270: apply-conclusions (conclusion)
0277: moteur (conclusion &optional rule)
0287: questions (liste)
0303: vire-conclusion (liste)
0314: get-rule (rule rules)
0321: flush-bdf (liste)
0326: flush-all (liste)


        LISP functions usage:
apply-rule : [122, 284, 285, 339, 339, 360, 360, 360, 404, 404, 404, 405, 405, 405, 423, 423, 423, 424, 424, 424, 429, 429, 429, 430, 430, 430, 464]
verify-premises : [43, 154, 165, 282, 341, 345, 345, 362, 362, 402, 402, 427, 427, 473, 473, 499, 499, 520, 520, 554, 554, 573, 573, 599, 599, 613]
get-basic-value : [118, 191, 290, 291, 381, 381, 739, 739, 740, 740, 818, 818, 819, 819, 908, 908, 908, 951, 951, 951, 952, 952, 952]
put : [394, 921, 923, 923]
conclusions : [105, 108, 110, 112, 119, 131, 133, 135, 257, 259, 270, 341, 362, 499, 503, 582, 584, 585, 613, 672, 677, 693, 695, 702, 801, 808]
find-rule : [129, 152, 154, 156, 158, 278, 315, 385, 398, 415, 419, 467, 514, 543, 562, 589, 621, 636, 641, 642, 643, 709, 714, 715, 716, 752, 757]
update-bdf : [239, 239, 242, 242, 249, 249, 281, 281, 401, 401, 422, 422, 426, 426, 472, 472, 517, 517, 551, 551, 553, 553, 570, 570, 572, 572]
get-premisses : [206, 208, 210, 213, 279, 309, 311, 399, 416, 420, 468, 515, 544, 563, 590, 622, 637, 641, 642, 710, 714, 715, 753, 757, 758]
flush-bdf : [247, 321, 321, 324, 324, 328, 328]
apply-conclusions : [341, 362, 499, 503, 503, 582, 582]
moteur : [397, 397, 414, 414, 414, 466, 466, 466, 466, 470, 470, 470, 470, 513, 513, 513, 513, 513, 519, 519, 519, 519, 519, 528, 528, 528]
questions : [290, 291, 400, 408, 410, 421, 425, 471, 516, 550, 553, 569, 572, 595, 598, 627, 641, 644, 714, 717, 736, 736, 739, 739, 740]
vire-conclusion : [306]
get-rule : [317, 402, 427, 473, 520, 554, 573, 599]
flush-all : [1108, 1284, 1304, 1323, 1343, 1378, 1411, 1447, 1481, 1522]
save-conclusion : [372, 374, 483, 483, 487, 487, 489, 489, 500, 500, 614, 614, 678, 678, 682, 682, 682, 686, 686, 686, 686]
get-all-rules : [456, 459, 470, 519, 546, 565, 593, 625, 640, 708, 743, 751, 776, 854, 936, 936, 939, 939, 955]
find-conclusion : [1161, 1211, 1223, 1223, 1231, 1231, 1241, 1241, 1255, 1255, 1255, 1262]