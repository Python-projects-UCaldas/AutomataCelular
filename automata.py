import itertools
import random

class Automata:
    def __init__(self, rule, radix, limit, phrase):
        """

        Parameters
        ----------
        rule: String
            Set of output values which tells how the automata is going to evolve.

        radix: int
            The numeral system.

        limit: int
            The limit width of the automata (max and min number of cells).

        Returns
        -------
        None.

        """
        self.transitions = {}
        self.rule = rule
        self.radix = radix
        self.limit = limit
        self.phrase = phrase
        self.init_automata()

    def init_automata(self):
        """
        Initializes the automata by assigning a transitions table using the radix, rule and limit.

        Parameters
        ----------

        Returns
        -------
        None.

        """
        iter = [i for i in range(self.radix)]
        if self.rule is None: #If the initial rule is None (it wasn't assigned by user), then assigns a random rule
            self.rule = []
            self.rule = [random.randint(0, len(iter)-1) for i in range(0, self.radix**3)]
        #print(self.rule)
        states = itertools.product(iter, repeat=3) #Does all combinations for every possible state 
        states = set(states)

        self.transitions = dict(zip(sorted(states), self.rule))
        #print(len(self.transitions), self.transitions)

    def get_next_state(self, ladj, act, radj):
        """
        Gets the following state by looking up in the transitions table where (ladj, act, radj) is
        the key in tuple form.

        Parameters
        ----------
        ladj: int
            Left adjacent of the actual state.

        act: int
            Actual state.

        radj: int
            Right adjacent of the actual state.

        Returns
        -------
        int
            The next state

        """
        if (ladj, act, radj) not in self.transitions:
            return 0
        else:
            next_state = self.transitions[(ladj, act, radj)]
        return next_state

    def get_next_phrase(self, current_phrase):
        """
        Gets the following phrase of the automata. A phrase is a list with the cells and its respective states.

        Parameters
        ----------
        current_phrase: list
            The current phrase.

        Returns
        -------
        list
            The next phrase of the automata.

        """
        next_phrase = []
        for i in range(len(current_phrase)):
            ladj = current_phrase[i-1] #left adjacent
            act = current_phrase[i] #actual state
            # If the i index is the last item of the phrase,
            # then right adjacent will be the first item of the phrase
            # otherwise the right adjacent will be the i+1 element.
            if i == len(current_phrase) - 1:
                radj = current_phrase[0]
            else:
                radj = current_phrase[i+1]

            next_state = self.get_next_state(ladj, act, radj)
            next_phrase.append(next_state)
        #print(current_phrase, next_phrase)
        return next_phrase