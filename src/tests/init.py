#!/usr/bin/env python
from mosi.solver import CbcCliSolver


CBC_LP_SOLVER = CbcCliSolver(file_type="lp")
CBC_MPS_SOLVER = CbcCliSolver(file_type="mps")


# noinspection PyShadowingBuiltins
class Problem:
    def __init__(self, model, vars):
        self.model = model
        self.vars = vars

    def clear(self):
        self.model.clear()
