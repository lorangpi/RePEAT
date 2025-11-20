from Formula import Formula
from AtomicFormula import AtomicFormula
from NegationFormula import NegationFormula
from ConsjunctionFormula import ConjunctionFormula
from DisjunctionFormula import DisjunctionFormula
from ModalOpFormula import ModalOpFormula

class EpistemicState(Formula):

    def __init__(self, state, display=False):
        """
        init of EpistemicState class

        :param state: Dict. The description of the Epistemic state
        :param display: bool. Whether it displays information about the Epistemic state on the terminal or not
        :return: None
        """ 
        self.state = state
        self.sets = list(state)
        self.model = state[self.sets[0]]
        self.Wd = state[self.sets[1]]
        self.W = state[self.sets[2]]
        self.agents = []
        for i in range(3,len(self.sets)-1):
            #print('here: ', state[self.sets[i]], len(state[self.sets[i]]))
            if len(state[self.sets[i]]) == 0:
                state[self.sets[i]] = []
            exec("self.%s = %s" % (self.sets[i], state[self.sets[i]]))
            self.agents += [self.sets[i]]
        self.L = state[self.sets[-1]]
        self.Truth = False
        if display:
            self.display()

    def display(self):
        """
        displays information about the Epistemic state on the terminal

        :param None
        :return: None
        """ 
        print("\n---------------------------------------Epistemic State:---------------------------------------\n", self.state, "\n",
        "\nModel: \n", self.model,
        "\nDesignated Worlds: \n", self.Wd,
        "\nWorlds: \n", self.W)
        for i in range(3,len(self.sets)-1):
            print(self.agents[i-3])
            exec("print(self.%s)" % (self.sets[i]))
        print("L: \n", self.L, "\n")

    def browse(self, formula, Rm, negated, truth_worlds):
        """
        browses in the epistemic state description to check if a formula holds in it according to the epistemic rules. 

        :param formula: object instance - the formula to check
        :param Rm: str - the Rm of the operator's agent
        :param negated: bool - if the formula is to be negated.
        :param truth_worlds: list - worlds list in which a fornula holds - recursive tracker
        :return: the truth of the formula in this Epistemic State instance (+ for recursive reasons done & truth_worlds)
        """ 
        #print('formula browse is: ', formula, type(formula))
        if Rm == None: #if a literal proposition has to be checked
            truth_list = []
            for wd in self.Wd:
                for l in self.L:
                    if wd == l[0]:
                        if isinstance(formula, ModalOpFormula):
                            truth = indistigu[1] in truth_worlds 
                            if negated:
                                truth = not(truth) 
                        elif isinstance(formula, AtomicFormula):
                            truth = str(formula.name) in l[1]
                            if negated:
                                truth = not(truth)
                        elif isinstance(formula, DisjunctionFormula):
                            truth = (str(formula.left) in l[1] or str(formula.right) in l[1])
                        elif isinstance(formula, ConjunctionFormula):
                            truth = (str(formula.left) in l[1] and str(formula.right) in l[1])
                        truth_list += [truth]
                        if l[0] not in truth_worlds:
                            truth_worlds += [l[0]]
            truth = all(truth_list)
            done = True
        else: #if a modal operator has to be ckeckeds
            name = 'relate'
            exec("self.%s = self.%s" % (name, Rm))
            truth_list = []
            if len(self.relate) == 0:
                done = False
                truth = False
            for indistigu in self.relate:
                for wd in self.Wd:
                    if indistigu[0] == wd:
                        for l in self.L:
                            if indistigu[1] == l[0]:
                                if isinstance(formula, ModalOpFormula):
                                    truth = indistigu[1] in truth_worlds 
                                    if negated:
                                        truth = not(truth) 
                                elif isinstance(formula, AtomicFormula):
                                    truth = str(formula.name) in l[1]
                                    if negated:
                                        truth = not(truth)
                                elif isinstance(formula, DisjunctionFormula):
                                    truth = (str(formula.left) in l[1] or str(formula.right) in l[1])
                                elif isinstance(formula, ConjunctionFormula):
                                    truth = (str(formula.left) in l[1] and str(formula.right) in l[1])
                                truth_list += [truth]
                                if l[0] not in truth_worlds:
                                    truth_worlds += [l[0]]
                truth = all(truth_list)
                done = True
            #print('truth browse is: ', truth)
        return done, truth, truth_worlds

    def truth(self, formula, done=False, truth=False, Rm=None, negated=False, truth_worlds = []):
        """
        - Recursive function -
        truth checks if the formula holds in this Epistemic State instance.
        truth either calls itself if the formula is not an recursive ending condition or calls "browse" if so. 

        :param formula: object instance - the formula to check
        
        recursive parameters to keep track of:
        :param done: bool - is checking done?
        :param truth: bool - is the formmula true is this state?
        :param Rm: str - the Rm of the operator's agent
        :param negated: bool - if the instance of the formula is a negation.
        :param truth_worlds: list - worlds list in which a fornula holds - recursive tracker 
        :return: truth : bool - the truth of the formula in this Epistemic State instance (+ for recursive reasons done & truth_worlds as defined above)
        """ 

        # Formula's instance type conditions for recursive expression   
        if done:
            return done, truth, truth_worlds 
        if isinstance(formula, ModalOpFormula):
            agent = formula.agent
            Rm = "Rm" + str(formula.agent)
            form = formula.formula
            done, truth, truth_worlds = self.truth(form, done=done, truth=truth, Rm=Rm, truth_worlds=truth_worlds)
            #if the formula to be known by the operator holds in the state, else the global formula is false anyway
            if truth:
                done, truth, truth_worlds = self.browse(formula, negated=negated, Rm=Rm, truth_worlds=truth_worlds)
            if done:
                return done, truth, truth_worlds
        elif isinstance(formula, NegationFormula):
            if isinstance(formula.negation, AtomicFormula):
                done, truth, truth_worlds = self.truth(formula.negation, done=done, truth=truth, Rm=Rm, negated=True)
            else:
                done, truth, truth_worlds = self.truth(formula.negation, done=done, truth=truth, Rm=Rm)
                truth = not(truth)
        elif isinstance(formula, AtomicFormula):
            done, truth, truth_worlds = self.browse(formula, negated=negated, Rm=Rm, truth_worlds=truth_worlds)
        elif isinstance(formula, DisjunctionFormula):
            if Rm == None:
                done, truth, truth_worlds = self.truth(formula.left, done=done, truth=truth, Rm=Rm)
                # Where the OR operator appears (if left not True than try right)
                if truth:
                    done
                else:
                    done, truth, truth_worlds = self.truth(formula.right, done=done, truth=truth, Rm=Rm)
            elif not isinstance(formula.left, AtomicFormula) or not isinstance(formula.right, AtomicFormula):
                done, truth, truth_worlds = self.truth(formula.left, done=done, truth=truth, Rm=Rm)
                # Where the OR operator appears (if left not True than try right)
                if truth:
                    done
                else:
                    done, truth, truth_worlds = self.truth(formula.right, done=done, truth=truth, Rm=Rm)
            else:
                done, truth, truth_worlds = self.browse(formula, negated=negated, Rm=Rm, truth_worlds=truth_worlds)
        elif isinstance(formula, ConjunctionFormula):
            if Rm == None:
                done, truth, truth_worlds = self.truth(formula.left, done=done, truth=truth, Rm=Rm) 
                # Where the AND operator appears (if left True than still check right)
                if truth:
                    done, truth, truth_worlds = self.truth(formula.right, done=False, truth=truth, Rm=Rm)
            elif not isinstance(formula.left, AtomicFormula) or not isinstance(formula.right, AtomicFormula):
                done, truth, truth_worlds = self.truth(formula.left, done=done, truth=truth, Rm=Rm)
                # Where the AND operator appears (if left True than still check right)
                if truth:
                    done, truth, truth_worlds = self.truth(formula.right, done=False, truth=truth, Rm=Rm)
            else:
                done, truth, truth_worlds = self.browse(formula, negated=negated, Rm=Rm, truth_worlds=truth_worlds)
        else:
            print("Error msg: the Formula doesn't respect the syntax rules. Refer to Readme. \ntruth: Ignored \n",formula,'\n',type(formula))
        if done:
            return done, truth, truth_worlds