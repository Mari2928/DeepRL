
############################################################################################################
##########################            RL2023 Assignment Answer Sheet              ##########################
############################################################################################################

# **PROVIDE YOUR ANSWERS TO THE ASSIGNMENT QUESTIONS IN THE FUNCTIONS BELOW.**

############################################################################################################
# Question 2
############################################################################################################

def question2_1() -> str:
    """
    (Multiple choice question):
    For the Q-learning algorithm, which value of gamma leads to the best average evaluation return?
    a) 0.99
    b) 0.8
    return: (str): your answer as a string. accepted strings: "a" or "b"
    """
    answer = "a" 
    return answer


def question2_2() -> str:
    """
    (Multiple choice question):
    For the First-visit Monte Carlo algorithm, which value of gamma leads to the best average evaluation return?
    a) 0.99
    b) 0.8
    return: (str): your answer as a string. accepted strings: "a" or "b"
    """
    answer = "a" 
    return answer


def question2_3() -> str:
    """
    (Multiple choice question):
    Between the two algorithms (Q-Learning and First-Visit MC), whose average evaluation return is impacted by gamma in
    a greater way?
    a) Q-Learning
    b) First-Visit Monte Carlo
    return: (str): your answer as a string. accepted strings: "a" or "b"
    """
    answer = "b" 
    return answer


def question2_4() -> str:
    """
    (Short answer question):
    Provide a short explanation (<100 words) as to why the value of gamma affects more the evaluation returns achieved
    by [Q-learning / First-Visit Monte Carlo] when compared to the other algorithm.
    return: answer (str): your answer as a string (100 words max)
    """
    answer = "Compared to the other algorithm like Dynamic Programming algorithm, for example, Q-learning / First-Visit Monte Carlo algorithm learns from experience without knowing transition probabilities and reward system before hand. That experience is based on the expected discounted returns, and the algorithm learns to maximize it. Thus, the discounting-factor gamma, that controls the reward system significantly affects the learning process."  # TYPE YOUR ANSWER HERE (100 words max)
    return answer


############################################################################################################
# Question 3
############################################################################################################

def question3_1() -> str:
    """
    (Multiple choice question):
    In Reinforce, which learning rate achieves the highest mean returns at the end of training?
    a) 6e-1
    b) 6e-2
    c) 6e-3
    return: (str): your answer as a string. accepted strings: "a", "b" or "c"
    """
    answer = "c"  # TYPE YOUR ANSWER HERE "a", "b" or "c"
    return answer


def question3_2() -> str:
    """
    (Multiple choice question):
    When training DQN using a linear decay strategy for epsilon, which exploration fraction achieves the highest mean
    returns at the end of training?
    a) 0.75
    b) 0.25
    c) 0.01
    return: (str): your answer as a string. accepted strings: "a", "b" or "c"
    """
    answer = "c"  # TYPE YOUR ANSWER HERE "a", "b" or "c"
    return answer


def question3_3() -> str:
    """
    (Multiple choice question):
    When training DQN using an exponential decay strategy for epsilon, which epsilon decay achieves the highest
    mean returns at the end of training?
    a) 1.0
    b) 0.75
    c) 0.001
    return: (str): your answer as a string. accepted strings: "a", "b" or "c"
    """
    answer = "b"  # TYPE YOUR ANSWER HERE "a", "b" or "c"
    return answer


def question3_4() -> str:
    """
    (Multiple choice question):
    What would the value of epsilon be at the end of training when employing an exponential decay strategy
    with epsilon decay set to 1.0?
    a) 0.0
    b) 1.0
    c) epsilon_min
    d) approximately 0.0057
    e) it depends on the number of training timesteps
    return: (str): your answer as a string. accepted strings: "a", "b", "c", "d" or "e"
    """
    answer = "e"  # TYPE YOUR ANSWER HERE "a", "b", "c", "d" or "e"
    return answer


def question3_5() -> str:
    """
    (Multiple choice question):
    What would the value of epsilon be at the end of training when employing an exponential decay strategy
    with epsilon decay set to 0.990?
    a) 0.990
    b) 1.0
    c) epsilon_min
    d) approximately 0.0014
    e) it depends on the number of training timesteps
    return: (str): your answer as a string. accepted strings: "a", "b", "c", "d" or "e"
    """
    answer = "e"  # TYPE YOUR ANSWER HERE "a", "b", "c", "d" or "e"
    return answer


def question3_6() -> str:
    """
    (Short answer question):
    Based on your answer to question3_5(), briefly  explain why a decay strategy based on an exploration fraction
    parameter (such as in the linear decay strategy you implemented) may be more generally applicable across
    different environments  than a decay strategy based on a decay rate parameter (such as in the exponential decay
    strategy you implemented).
    return: answer (str): your answer as a string (100 words max)
    """
    answer = "Manually setting the decay rate that does not depend on the number of max timesteps may not effectively benefit from hyperparameter scheduling because the required steepness of the slope of the decay rate may differ by the environment. For example, if the number of training timesteps is 100 with a decay rate of 0.99, the learning rate (epsilon) will not reach its minimum during training, while the opposite case will drop epsilon too quickly. By making epsilon based on an exploration fraction, we could train the model with a fitted exponential decay rate."  # TYPE YOUR ANSWER HERE (100 words max)
    return answer


def question3_7() -> str:
    """
    (Short answer question):
    In DQN, explain why the loss is not behaving as in typical supervised learning approaches
    (where we usually see a fairly steady decrease of the loss throughout training)
    return: answer (str): your answer as a string (150 words max)
    """
    answer = "The value of the loss grows during training because the targets in the DQN loss function depend on the network weights, in contrast with the targets used for supervised learning, which are fixed before learning begins. Since the DQN algorithm aims to maximize Q-value through timesteps, optimizing the loss function for the weights that depens on the Q-value resulted in growing the value of loss."  # TYPE YOUR ANSWER HERE (150 words max)
    return answer


def question3_8() -> str:
    """
    (Short answer question):
    Provide an explanation for the spikes which can be observed at regular intervals throughout
    the DQN training process.
    return: answer (str): your answer as a string (100 words max)
    """
    answer = "Every C (2000 in our case) updates, the DQN algorithm clones the network Q to obtain a target network and use it to generate the Q-learning targets (yj) for the following C updates to network Q. Because it uses an older set of parameters to generate (yj), it has a larger loss immediately after the update, resulting in spikes. However, this approach adds a delay between the time an update to Q is made and the time the update affects the targets (yj), making divergence or oscillations of the policy much more unlikely and the algorithm gets more stable."    
    return answer


############################################################################################################
# Question 5
############################################################################################################

def question5_1() -> str:
    """
    (Short answer question):
    Provide a short description (200 words max) describing your hyperparameter turning and scheduling process to get
    the best performance of your agents
    return: answer (str): your answer as a string (200 words max)
    """
    answer = "As for hyperparameter turning, I selected a sensible value for each hyperparameter and iterated over the range of values around the value using manual search and tuned tau and learning rates of actor and critic networks. I referred to the paper to choose those sensible values. For instance, experiment with a list of tau values and find the best one. Then, tune the next hyperparameter, the learning rate of the actor, using the best tau, and so on. Tested values in the fine-tuning are as follows: policy_learning_rate: [0.01, 0.002, 0.001, 0.0002, 0.0001], critic_learning_rate: [0.01, 0.002, 0.001, 0.0002, 0.0001], and tau: [1.0, 0.1, 0.01, 0.005, 0.003,0.002, 0.001]. For statistical consistency, I swiped my model 10 seeds per hyperparameter. Instead of the grid search, I used multiple terminals to experiment with models with different values simultaneously to save time, e.g., terminal 1 searches for the learning rate of the actor using the best tau while terminal 2 for the learning rate of critic with the best tau. I also tested scheduling weight decay in my Adam optimizer by setting weight_decay=0.01 to set L2 weight decay. But it degraded the performance, so the best model does not use this."  # TYPE YOUR ANSWER HERE (200 words max)
    return answer
