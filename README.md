## REPEAT: When Execution doesn’t meet Planning
RE-Planning Epistemic Actions from Trials
Accomodating Novelties in Epistemic Planning using Reinforcement Learning

# Installation
git clone and:
pip install stable-baselines3

# Comments:
The goal of this project is for an agent to adapat a plan, and replace an event by a learned policy when some event didn't produce the expected
effects.
For each problem there must be an initial epistemic representation of the problem and a new RL modification of its initial state
For each problem there must be an environment: for the agent to execute the plan in simulation and for it to learn how to handle novelties
Two examples are hereby used as demonstration of the principle

The first example consists of a birthday gift problem in which the father is supposed to get a gift that might be in two different locations PO1, PO2, but he does not know where at planning time. The novelty scenario here is that even after trying to pick up the gift at both locations (following yet a strong plan in his initial knowledge of the world), he did not get the gift. He must then refer to the environment and attempt random actions to access and wrap the gift, he will eventually discover that the gift is actually in a third location. The goal here is to demonstrate that by doing this, this method allows one to maintain a strong epistemic plan even in the face of novelty (REPEAT will change the first plan, become weak, for the new strong again plan for later similar tasks).


The second example is an extension of the Pink Panther thief problem with an additional Red Fox Policeman standing outside the vault.
If Red Fox is aware (knows) that the Pink Panther is leaving with the diamond, he will be caught red-handed! The Pink Panther must distract the Red Fox policeman by throwing a rock out of the vault when the Pink Panther leaves the vault with the diamond. If Red Fox is not distracted, he will catch the Pink Panther's thief. Throwing a Pebble is an event pattern that has two events in its event set. The one that is designated does nothing, the other states that ¬d. These two events are indistinguishable for Red Fox. 
There are two novelties here. The first is that the red fox can be inside the vault, which makes it impossible for the Pink Panther to steal the diamond without the red fox knowing. He has to try several actions to learn how to distract the red fox again to get in and steal the jewel. Spoiler alert: he will learn that cutting the electricity will bring Red Fox out of the vault to fix it. The light will no longer turn on, so he'll have to use the battery he brought with him to still turn on and know if the diamond is right or left. The second is that the Pink Panther's goal has changed and she now wants to know that she is safe, that is, she wants to know that Red Fox doesn't know she has the diamond when she goes to sleep in peace. Yet, throwing a pebble is indistinguishable from succeeding, so she must try new events.



Add -s True in addition to -v True to see both the information about the states, events and product update of the indistiguishable events and the search/RL information respectively in real computation time.

# Run

cd /src
python3 main.py -f exampleBirthdayPresent

or
python3 main.py -f examplePinkPanther


# Rules:
°Negated atoms or formulas should always remain inside parenthesis !(p), -(a&b), ¬(Op(a))...
°Operators should be input as follow "Opi(f)", Op designates the modal operator, i the agent, f the formula.


# Language: formula
    : LOWER_NAME              # atom
    | formula OP_AND formula  # conjunction
    | formula OP_OR formula   # disjunction
    | '(' formula ')'         # parens
    | '-(' formula ')'        # negation
    | '¬(' formula ')'        # negation
    | '!(' formula ')'        # negation
    | 'Op(' formula ')'       # modal_operator
    | 'Box(' formula ')'      # modal_operator
    | 'B(' formula ')'        # modal_operator
    ;
