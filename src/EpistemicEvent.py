from dis import dis
import numpy as np
from Formula import Formula
from AtomicFormula import AtomicFormula
from NegationFormula import NegationFormula
from ConsjunctionFormula import ConjunctionFormula
from DisjunctionFormula import DisjunctionFormula
from ModalOpFormula import ModalOpFormula

class EpistemicEvent(Formula):

    def __init__(self, event, display=False):
        """
        init of EpistemicEvent class

        :param event: Dict. The description of the Epistemic event
        :param display: bool. Whether it displays information about the Epistemic state on the terminal or not
        :return: None
        """ 
        self.screen_display = display
        self.event = event
        self.sets = list(event)
        self.action = event[self.sets[0]]
        self.Ed = event[self.sets[1]]
        self.E = event[self.sets[2]]
        self.agents = []
        for i in range(3,len(self.sets)-2):
            exec("self.%s = %s" % (self.sets[i], event[self.sets[i]]))
            self.agents += [self.sets[i]]
        self.pre = event[self.sets[-2]]
        self.post = event[self.sets[-1]]
        self.Truth = False
        if self.screen_display:
            self.display()

    def display(self):
        """
        displays information about the Epistemic event on the terminal

        :param None
        :return: None
        """ 
        print("\n---------------------------------------Epistemic Event:---------------------------------------\n",# self.event, '\n'
            "\nModel: \n", self.action,
            "\nDesignated Events: \n", self.Ed,
            "\nEvents: \n", self.E)
        for i in range(3,len(self.sets)-2):
            print(self.agents[i-3])
            exec("print(self.%s)" % (self.sets[i]))
        print("pre-conditions: \n", self.pre, "\npost-conditions: \n", self.post, "\n\n")

    def compute(self, state):
        """
        if called, computes the product update of the input epistemic state with this instance of epistemic event.

        :param state: EpistemicState instance - The epistemic state to compute with the event
        :return computed_state : dict - The dictionnary describing the newly computed epistemic state (it will be instantiated as an Epistemic State in main.py) 
        """ 
        M_prime = state.sets
        W_prime = self.rule_Wprime(state)
        self.W_copy = W_prime.copy()
        Wd_prime = self.rule_Wdprime(state, W_prime)
        #for i in range(0, len(Wd_copy), 2):
        #    Wd_prime += [self.concatenate([Wd_copy[i], Wd_copy[i+1]])]
        #print('---------------------------------------------------------------\n', Wd_prime,'\n---------------------------------------------------------------\n')
        Wd_prime = [self.concatenate(Wd_prime)]
        Wd_copy = Wd_prime.copy()
        Wd_prime = []
        for Wd in Wd_copy:
            Wd_prime += Wd
        if self.screen_display:
            print('-------------------------------Computed (new) Epistemic State:-------------------------------\n'
                '\nM_prime: (note that the names remain the same but it is a new Epistemis state instance \n', M_prime,
                '\nWd_prime: \n', Wd_prime,
                '\nW_prime: \n', self.concatenate(self.W_copy))
        self.Rm_prime_list = []
        self.rule_Rmprime(state, W_prime)
        L_prime = self.rule_Lprime(state, W_prime)
        W_prime = self.concatenate(W_prime)
        L_prime = self.concatenate2(L_prime)
        L_copy = L_prime.copy()
        L_prime = []
        for i in range(0, len(L_copy), 2):
            L_prime += [[L_copy[i], L_copy[i+1]]]

        self.computed_state = {"M":M_prime, "Wd":Wd_prime, "W":W_prime}
        for i, agent in enumerate(state.agents):
            var_name = str(agent)
            exec("self.Rm = self.%s" % (state.agents[i]))
            dict = {var_name: self.Rm}
            self.computed_state.update(dict)
        self.computed_state.update({"L_prime": L_prime})

        if self.screen_display:
            print('L_prime: \n', L_prime, '\n\n')#,'dict state: \n', self.computed_state, '\n\n')
        return self.computed_state

    def rule_Wprime(self, state, check_Ed=False):
        """
        Appllies the computationnal rules of the product update of (M, Wd) with (E, Ed)
        if check_Ed, shortcuts to return True if the conditionnal action is applicable in S

        :param state: EpistemicState instance - The epistemic state to compute with the event
        :param check_Ed: bool - A flag, if True shortcuts to check only the pre-conditions of the Ed in state
        :return W_prime : array (list of lists) - The W of the new epistemic state
        """ 
        worlds = state.Wd if check_Ed else state.W
        W_prime = []
        applicable_list = []
        for world in worlds:
            for label in state.L:
                if label[0] == world:
                    propositions = label[1]
            for assign in self.pre:
                action = assign[0]
                applicable = True
                for precondition in assign[1]:
                    if precondition.startswith('¬') or precondition.startswith('-'):
                        if precondition[1] in propositions:
                            applicable = False
                    elif not(precondition in propositions or precondition == ""):
                            applicable = False
                applicable_list.append(applicable)
                if applicable:
                    if self.concatenate([world, action]) not in worlds:
                        W_prime += [[world, action]]

            if check_Ed: #only returns if the Ed is applicable (shortcut)
                return np.asarray(applicable_list).any()
        return W_prime

    def rule_Rmprime(self, state, W_prime):
        """
        Appllies the computationnal rules of the product update of (M, Wd) with (E, Ed)

        :param state: EpistemicState instance - The epistemic state to compute with the event
        :return (by instance bridge) Rm_prime : array (list of lists) - The Rm(s) of the new epistemic state
        """ 
        #print('W_prime: ',W_prime)
        for i, agent in enumerate(state.agents):
            exec("self.%s = []" % (agent))
            exec("self.Rm = %s" % (state.state[state.sets[i+3]]))
            exec("self.Re = %s" % (self.event[self.sets[i+3]]))
            #print(agent)
            #print('Rm: ',self.Rm)
            #print('Re: ', self.Re)
            for world_i in W_prime:
                for world_j in W_prime:
                    if [world_i[0], world_j[0]] in self.Rm:
                        if [world_i[1], world_j[1]] in self.Re:
                            exec("self.%s += [[%s, %s]]" % (agent, world_i, world_j))
            exec("self.%s = self.concatenate(self.%s)" % (agent, agent))
            if self.screen_display:
                print(agent, '_prime:')
                exec("print(self.%s)" % (agent))
                exec("self.Rm_prime_list += [self.%s]" % (agent))

    def rule_Lprime(self, state, W_prime):
        """
        Appllies the computationnal rules of the product update of (M, Wd) with (E, Ed)

        :param state: EpistemicState instance - The epistemic state to compute with the event
        :return L_prime : array (list of lists) - The L of the new epistemic state
        """ 
        L = []
        for world_prime in W_prime:
            for label in state.L.copy():
                world = label[0]
                propositions = label[1].copy()
                for assign in self.post:
                    action = assign[0]
                    if world == world_prime[0]:
                        if action == world_prime[1]:
                            for post in assign[1]:
                                if post.startswith('¬') or post.startswith('-'):
                                    post = post[1:]
                                    if post in propositions:
                                        propositions.remove(post)
                                elif post != '':
                                    propositions += [post]
                            L += [world_prime, [propositions]]
        return L

    def rule_Wdprime(self, state, W_prime):
        """
        Appllies the computationnal rules of the product update of (M, Wd) with (E, Ed)

        :param state: EpistemicState instance - The epistemic state to compute with the event
        :return Wd_prime : array (list of lists) - The Wd designated world of the new epistemic state
        """
        Wd_prime = []
        W = self.W_copy.copy()
        for world in W_prime:
            for wd in state.Wd:
                if world[0] == wd:
                    if world[1] in self.Ed:
                        Wd_prime += [[world[0], world[1]]]
        if len(Wd_prime) == 0:
            return state.Wd
        """
        elif len(Wd_prime)/2 +1 < len(state.Wd):
            for world in state.Wd:
                test = True
                for wd in Wd_prime:
                    if world in wd:
                        test = False
                if test:
                    Wd_prime += [world]
        """
        return Wd_prime

    def concatenate(self, array):
        """
        - Recursive function -
        This function concatenates the new states to give a one string name to the new worlds (example ["u", "e"] is named as ["ue"])

        :param array : array - the array whose cells are to be concatenated
        :return array : array - the array concatenated
        """ 
        if len(array) > 0:
            if type(array[0]) == str:
                array = ''.join(array)
                return array
            else:
                for i, cell in enumerate(array):
                    array[i] = self.concatenate(cell)
                return array
        else:
            return ''

    def concatenate2(self, array):
        """
        -Concatenate2 is not a recursive function-
        This function concatenates the new states to give a one string name to the new worlds (example ["u", "e"] is named as ["ue"])

        :param array : array - the array whose cells are to be concatenated
        :return array : array - the array concatenated
        """ 
        if len(array) > 0:
            if type(array[0]) == str:
                array = ''.join(array)
                return array
            else:
                for i, cell in enumerate(array):
                    if i % 2 == 0:
                        array[i] = self.concatenate(cell)
                    else:
                        array[i] = cell[0]
                return array
        else:
            return ''