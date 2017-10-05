#!/usr/bin/env python
from pathlib import Path
from shutil import rmtree

from mosi.common import ModelStatus
from mosi.lp import Model, DecisionVariable

# noinspection PyPackageRequirements,PyUnresolvedReferences
from .init import CBC_LP_SOLVER, CBC_MPS_SOLVER, Problem

DELETE = True
DIRECTORY = None  # "../../../volume/results/lp"
OBJECTIVE = 140
SOLUTION = [-40.0, -110.0, 0.0]
TOLERANCE = 10 ** -8


# noinspection PyStatementEffect
def setup():
    rmtree(str(Path(__file__).parent.joinpath("../../volume/results/lp")), True)

    model = Model(auto=True)

    x = {
        1: DecisionVariable(model, lower_bound=-40),
        2: DecisionVariable(model, lower_bound=-float("inf")),
        3: DecisionVariable(model)
    }

    model.max(
        2 * x[1] - 2 * x[2] + x[3]
    )

    2 * x[1] - x[2] + x[3] <= 80
    3 * x[1] - 2 * x[2] + 2 * x[3] <= 100
    x[1] + x[2] + x[3] <= 40

    return Problem(model, x.values())


def test_cbc_lp():
    problem = setup()
    CBC_LP_SOLVER.solve(problem.model, directory=DIRECTORY, delete=DELETE)

    assert problem.model.get_status() == ModelStatus.OPTIMAL
    assert all(abs(var.get_value() - sol) < TOLERANCE for var, sol in zip(problem.vars, SOLUTION))
    assert [var.get_value() for var in problem.vars] == SOLUTION


def test_cbc_mps():
    problem = setup()
    CBC_MPS_SOLVER.solve(problem.model, directory=DIRECTORY, delete=DELETE)

    assert problem.model.get_status() == ModelStatus.OPTIMAL
    assert all(abs(var.get_value() - sol) < TOLERANCE for var, sol in zip(problem.vars, SOLUTION))
    assert [var.get_value() for var in problem.vars] == SOLUTION
