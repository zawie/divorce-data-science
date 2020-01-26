Using SVM Models to Optimize Divorce Predictor Scales
Introduction:
	We were very intrigued by the Divorce Predictors data set (Source A), largely due to the ease with which the data could be understood and the vast social implications of the subsequent data analyses.
The data set was provided as part of a study conducted by Yontem, Adem, Ilhan, & Kilicarslan (2019), which sought to understand the features correlated with divorce incidence. Previously, psychologists had posited the “Four Horsemen” of marriage deterioration: contempt, criticism, stonewalling, and defensiveness were cited as factors most likely to cause friction in relationships. To accomplish this task, they recruited participants to fill out a Divorce Predictor Scale questionnaires, composed of 54 questions with values ranging from 0 (strongly agree) to 5 (strongly disagree). Their subsequent data analyses included efforts to classify the data using random forests, artificial networks (ANN), and RBF neural network models.
Reading the paper prompted several questions for us. First, the researchers omitted the use of support vector machines (SVM), which we thought might be effective after glancing at the data. Second, we noted the surprisingly high number of questions - 54 questions. We noted that this fact would be a barrier for future researchers wanting to expand the current set by soliciting volunteer responses for better modelling. We reasoned that if there were fewer questions, convincing couples to fill out the survey would be considerably easier. To this end, we decided to attempt to cut down the number of questions while maintaining high accuracy.

Method:
	Our attempt was based around using the Recursive Feature Elimination algorithm, which uses a linear kernel machine to extrapolate and rank the most important n features, n being the number of features we want to keep. As we sought to determine the optimal number of features to keep, or questions to ask, we developed our own framework for the removal of features.
	Our workflow is as follows. We ran the REF algorithm and selected for all but one features. For example, given 54 features, we would use n=53. The data corresponding to these 53 features would then be classified using a support vector machine (SVM) algorithm (implemented in Python), using a k-fold cross verification (fold = 5). The accuracy of this classification was recorded. 
We then utilized the REF algorithm on the remaining features, until one question remained. Therefore, after each successive iteration, the least important feature would have been removed until we ended with the single-most important feature. This process of paring down was repeated 1000 times in order to generate an average accuracy per a given number of questions.
Results:

Graph 1: Algorithmic Prediction Accuracy (%) vs Number of Questions asked in the Survey 

Our main result, as displayed in graph 1, illustrates an important and slightly unexpected result. The accuracy of our predictive classification algorithm seemingly “peaks” when the survey is composed of eight questions (an accuracy of 99.46%). Adding questions actually causes a decrease in accuracy, which plateaus. This result proves that many of the 54 initial questions are actually unnecessary or at best insignificant when it comes to predicting divorce. We posit the occasional fluctuations in the plot is explained by the fact that certain variables are connected to others; iteratively removing features least important could impact remaining features a little. 



Graph 2: The relative importance measured in rank of importance of each specific question

Knowing the relative rank of importance of the questions, we decided to create a new survey of the most important eight questions. Below is the optimized Divorce Prediction Scale we produced in this Datathon.
