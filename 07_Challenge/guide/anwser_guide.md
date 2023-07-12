## Common Mistakes 

### Imports
* line 8 - incorrect import name

### `make_model` 
* line 9 - in_layer != input_layer 
* line 19 - model = Model(in_layer, x) -> `model = Model(in_layer, output)`

### `train_model`
* line 12 - too few validation samples 
* line 16 - validation data is set to the train data 
* line 17 - `epoch` spelled incorrectly

### `eval_model`
* line 8 - No parameter for the generator named "test"
* line 10 - wrong name for the model
* line 11 - wrong np.where order of 1/0


# Notebook 1 - 

Very low learning rate - The model will never learn. 
Incorrect loss function - swap to a binary classification loss. 

# Notebook 2 - 

Imbalanced training data - 85-95% stars. 
Correct by weighting the labels in the training loop. 

# Notebook 3 - 

There is a ton of noise in the input image. 
Cannot be stricitly corrected, must be documented. 

# Notebook 4 - 

Extra class in the training data. Write a function that removes label N=3, or weight it 0. 

# Notebook 5 - 

A pre-processing function is applied to the training data but not the validation or testing data. 