# Travel Insurance Predictions Project


## Deadline: October 18, 2021

## Collaborators
- [Jimmy Nguyen](https://github.com/Jimmy-Nguyen-Data-Science-Portfolio)
- [Chris Robinson](https://github.com/ChrisRobinsonUSD)
- [Nima Amin Taghavi](https://github.com/nimaamintaghavi/) 

# About the Project

## Short Description of Your Project and Objectives:

A travel agency in India has engaged our group to devise a model for predicting sales of coronavirus (COVID) related travel insurance based on a set of commonly collected personal attributes.  The travel agency has seen greatly reduced sales during the pandemic and now that travel is resuming feels compelled to offer COVID related travel insurance in order to stay relevant in the post-pandemic marketplace.  The agency would like to analyze the risks associated with making any financial commitments at a time when revenues are low as any additional financial burden on the agency could be devastating.


## Background

Competitors have begun offering COVID travel insurance due to the pandemic. Not all carriers include this coverage and with the COVID situation still not under control some travel companies are deciding to revamp their insurance offerings to include COVID insurance. Because of the added cost associated with maintaining this type of insurance some companies have adopted a “wait and see” attitude hoping the pandemic will end in the near future.  As we emerge from the pandemic and travel has started to resume offering COVID insurance could be a major differentiator for clients when deciding which travel agency to select for booking travel.


## Main Research Questions

The company’s current travel insurance offering does not include coverage for COVID related trip cancellation or medical expenses.  The competitors are starting to offer this coverage and several customers have shown hesitancy to travel due to the risk of cancellation associated with the current COVID situation.           

Due to the current COVID situation it is important to be able to offer COVID insurance as an option. In order to offer this coverage, the company will have to change insurance carriers and sign into a contract in order to make the offering affordable.  Due to the cost and risk associated with the change in carriers it is imperative that the company do their due diligence in estimating the customer response to the new offering before making a decision.


# Methodology

- Problem statement and justification for the proposed approach
- EDA (graphical and non-graphical representations of relationships between the response variable and predictor variables)
- Data wrangling and pre-processing (handling of missing values, outliers, correlated features, etc.)
- Data splitting (training, validation, and test sets)
- Model strategies (describing main research questions and appropriate analytics methods)
- Validation and testing (model tuning and evaluation)
- Results and final model selection (performance measures, etc.)
- Discussion and conclusions (address the problem statement and suggestions that could go beyond the scope of the project.)

# Analytics Methods

- A supervised classification task, where the outcome variable of interest is _TravelInsurance_ that indicates whether the customer will buy the travel insurance. Performance metrics should take in consideration the positive class of buyers/purchasers. 
- Therefore, the optimal performance metric that can answer the business question is precision, recall, or F1-Score. 
- For simplicity, we focus on combining the two metrics and thus the best selection is the F1-score.

## The following models are selected:

- Decision Tree (with pruning)
- Boosted Trees (AdaBoost)
- Bagging Trees (Random Forest)
- Logistic Regression with step-wise linear regression
- Multi-layered Neural Network (Designing the number of hidden layers and nodes)
- K-Nearest Neighbors (Selecting K without overfitting and best Accuracy)
- Multinomial Naive Bayes (All variables are binary)
- Linear Discriminant Analysis 
- Ensemble Voting Classifier (Based on Top 3 models with the highest F1-Scores)


## Model Training and Evaluating Performance

Each model will be fine-tuned over the optimal hyper-parameters using a 5-k folds cross-validation to get the highest F1-scores from training then compare model performance on the validation set.

For example, we will be using a pre-specified grid search to find the best hyper-parameters for a single decision tree, cross-validating in a 5-K folds across the training set. 

Lastly, we will find the top 2 models with the highest F1-scores to be used for a voting classifier ensemble model. This ensemble model will be competing against the top 1 model in comparisons with each other's F1-scores. The final model selection will be the one with the highest F1-score.

## Technologies
- Python
- HTML, CSS, Javascript
- Microsoft Powerpoint
- Microsoft Word

# Original Data 
[Kaggle - Travel Insurance Prediction Data Set](https://www.kaggle.com/tejashvi14/travel-insurance-prediction-data)

## Data Set Dictionary

- Age- Age Of The Customer
- Employment Type- The Sector In Which Customer Is Employed
- GraduateOrNot- Whether The Customer Is College Graduate Or Not
- AnnualIncome- The Yearly Income Of The Customer In Indian Rupees[Rounded To Nearest 50 Thousand Rupees]
- FamilyMembers- Number Of Members In Customer's Family
- ChronicDisease- Whether The Customer Suffers From Any Major Disease Or Conditions Like Diabetes/High BP or Asthama,etc.
- FrequentFlyer- Derived Data Based On Customer's History Of Booking Air Tickets On Atleast 4 Different Instances In The Last 2 Years[2017-2019].
- EverTravelledAbroad- Has The Customer Ever Travelled To A Foreign Country[Not Necessarily Using The Company's Services]
- TravelInsurance- Did The Customer Buy Travel Insurance Package During Introductory Offering Held In The Year 2019.


## Presentations and Reports
* [Business Brief]()
* [Presentation Slides]()
* [Python Code](https://github.com/jimmy-nguyen-cal/Travel-Insurance-Predictions-/blob/main/Code/Python/Final%20Project%20-%20Travel%20Insurance%20Predictions%20Team%207.ipynb)


## Data Visualizations
![Age Groups](https://github.com/jimmy-nguyen-cal/Travel-Insurance-Predictions-/blob/main/Data%20Visuals/Age_Histogram.png)
![Proportions of Travel Insurance Buyers by Age](https://github.com/jimmy-nguyen-cal/Travel-Insurance-Predictions-/blob/main/Data%20Visuals/Proportions%20of%20Buyers%20by%20Age.png)


## Performance Results

![Performance  Table]()

![Gains Chart]()


## Conclusion

In an attempt to address the problem statement, A random sample of sales including 2000 individuals, was taken to create a model utilizing commonly available variables, including employment type, education, annual income, family size, health, and travel tendencies, such as travel frequency and international travel.  The models evaluated were Decision Tree (with pruning), Boosted Trees (AdaBoost), Bagging Trees (Random Forest), Logistic Regression with step-wise linear regression, Multi-layered Neural Network, K-Nearest Neighbors, Multinomial Naive Bayes, Linear Discriminant Analysis, and Ensemble Voting Classifier (Based on Top 3 models with the highest F1-Scores).  The best performing model, Ensemble Voting Classifier, was used to calculate the probability of an individual, based on the previously mentioned variables, purchasing COVID insurance.  Once the final model was trained, the agencies sales pipeline for the upcoming year was run through the model to predict the probability for each sale including COVID insurance.  Sales with a predicted probability greater than 50% were selected and the estimated sale amounts for each of these purchases was then totaled to get an estimated annual revenue for COVID insurance sales.   

The total revenue predicted by the model was ₹ 45,719.70.  The estimated annual cost to offer the insurance was ₹ 40,000.00, plus a ₹ 4,000.00 safety margin.  The total profit from offering the new insurance is ₹ 1,719.70.  Remember, the goal was simply to make sure the agency could offer the insurance without affecting revenue.  The determination is that offering the new insurance will not affect the upcoming years annual revenue.  The final recommendation is that the company move forward with contracting to offer the new insurance in order to offer COVID travel coverage to their customers.

It is suggested that after the first year of offering COVID insurance the actual sales figures be compared to the model results to determine if the model is predicting accurately.  If desired, the model can then be re-tuned to adjust for inaccuracies based on the new historical dataset.  This could be done annually if it is decided there is value in predicting COVID insurance sales after the initial phase.  Additionally, the agency could offer these prediction capabilities to other companies as a form of additional revenue or in exchange for other services.  These predictions could also be used to better tailor the services offered by the agency to their clients changing needs.


## References

- _In Progress_



