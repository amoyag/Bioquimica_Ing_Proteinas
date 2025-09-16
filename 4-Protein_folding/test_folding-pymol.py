from pyrosetta import *
from pyrosetta.teaching import *
init()
import os


polyA = pyrosetta.pose_from_sequence('A' * 10)
polyA.pdb_info().name("polyA")

pmm = PyMOLMover()
pmm.keep_history(True)
pmm.apply(polyA)
