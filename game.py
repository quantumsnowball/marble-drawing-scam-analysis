import math
import itertools
from functools import cached_property
from collections import namedtuple, defaultdict
import pandas as pd
import numpy as np


def _tp2str(tp):
    return ''.join(map(str, tp))


class Game:
    _colors = ['r', 'y', 'g', 'b', 'p']

    def __init__(self, n_colors=3, n_balls=24, n_draws=12, rewards=None, default_reward=None, fee=None):
        assert n_balls % n_colors == 0
        assert n_draws <= n_balls
        _n_each = n_balls // n_colors
        assert _n_each <= 9
        assert rewards and isinstance(rewards, dict)
        assert default_reward >= 0
        assert fee >= 0
        self._n_colors = n_colors
        self._n_each = _n_each
        self._n_balls = n_balls
        self._n_draws = n_draws
        self._rewards = defaultdict(lambda: default_reward, rewards)
        self._fee = fee

    @property
    def fee(self):
        return self._fee

    @cached_property
    def all_cases(self):
        prods = [tuple(range(self._n_each + 1))] * int(self._n_colors)
        psbts = (x for x in itertools.product(*prods)
                 if sum(x) == self._n_draws)
        cases = set(tuple(sorted(x, reverse=True)) for x in psbts)
        return cases

    @cached_property
    def all_cases_str(self):
        cases = self.all_cases
        cases = set(map(_tp2str, cases))
        return sorted(cases, reverse=True)

    @cached_property
    def all_probs(self):
        def case_prob(case):
            n_combins = 1
            for r in case:
                n_combins *= math.comb(self._n_each, r)
            n_combins *= math.factorial(self._n_colors)
            for i in range(max(case) + 1):
                n_repeat = case.count(i)
                if n_repeat > 1:
                    n_combins /= math.factorial(n_repeat)
            n_outcomes = math.comb(self._n_balls, self._n_draws)
            probs = n_combins / n_outcomes
            return probs
        probs = pd.Series({_tp2str(case): case_prob(case)
                          for case in self.all_cases}, name='probs')
        assert np.allclose(probs.sum(), 1)
        return probs.sort_values(ascending=True)

    @cached_property
    def all_payoffs(self):
        payoffs = pd.Series({_tp2str(case): self._rewards[_tp2str(case)]
                             for case in self.all_cases}, name='payoffs')
        return payoffs

    @cached_property
    def all_expected_rewards(self):
        df = self.metrics
        return df['expR']

    @cached_property
    def metrics(self):
        payoffs = self.all_payoffs
        probs = self.all_probs
        df = pd.concat([probs, payoffs], axis=1)
        df.index.name = 'case'
        df['expR'] = df['payoffs']*df['probs']
        return df.sort_values(by='probs', ascending=False)

    @cached_property
    def client_expected_return(self):
        metrics = self.metrics
        expR = metrics['expR'].sum()
        return expR - self._fee

    @cached_property
    def offer(self):
        metrics = self.metrics
        df = metrics['payoffs']
        return df.sort_index()


def main():
    game = Game(
        n_colors=3,
        n_balls=24,
        n_draws=12,
        rewards={
            '840': +300,
            '831': +100,
            '822': +120,
            '750': +60,
            '741': +40,
            '732': +15,
            '660': +100,
            '651': +10,
            '642': +5,
            '633': +5,
            '552': +5,
            '543': -30,
            '444': +5,
        },
        default_reward=0,
        fee=2)
    print(game.metrics)
    print(game.client_expected_return)


if __name__ == '__main__':
    main()
