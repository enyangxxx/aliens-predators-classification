# aliens-predators-classification
A binary classification task of aliens vs. predators

Source of dataset: https://www.kaggle.com/pmigdal/alien-vs-predator-images

The challenge in the dataset is the small amount of training data, it consists of 694 images for the training only, while the amount of validation data is 200. The goal is training a model, which does not overfit significantly and achieves high accuracy scores for both training and validation without applying any pre-trained model. The learning objective is playing with hyperparameter tuning: Finding out in an empirical approach, which hyperparameters have what kind of impact on the model performance. The selection of a proper model architecture is also involved and considered in the experiments.

The binary classification task is separated into two notebooks: One for the model training, another one for the model evaluation. The result consists of two trained models.

Model 1:<br>
Training loss: 0.076844<br>
Training accuracy: 0.989914<br>
Validation loss: 0.540033<br>
Validation accuracy: **0.855000**<br>

Model 2:<br>
Training loss: 0.219322<br>
Training accuracy: 0.940922<br>
Validation loss: 0.441823<br>
Validation accuracy: **0.860000**<br>
<br>
<img src="/readmeImg/alien.jpg" width="40%">
<br>
<img src="/readmeImg/predator.jpg" width="40%">

The fun part of this project is a competition between human and model performance. I invited a very intelligent Master student from Hasso Plattner Institute and asks him to classify the validation images. I offered him the oppportunity to learn from the training images but he rejected the invitation. While the best model performance is an accuracy score of 86\%, the intelligent HPI-student achieved a result of EMPTY\% accuracy. His predictions for validation image are documented in the Excel file.