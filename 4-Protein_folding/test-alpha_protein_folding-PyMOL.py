
# load pyRosetta
from pyrosetta import *
from pyrosetta.teaching import *
init()
import os

# rest of the setup
import math
import random

# Link PyRosetta to PyMOL
#We may want to visualize folding as it happens. Before starting with the folding protocol, instantiate a PyMOL mover and use a UNIQUE port number between 10,000 and 65,536.
# run PyMOL-RosettaServer.python3.py in the PyMOL comman line
# We will retain history in order to view the entire folding process by utilizing the .keep_history() method. Make sure it says PyMOL <---> PyRosetta link started! on its command line.

pmm = PyMOLMover()
pmm.keep_history(True)


# Generate the initial pose

polyA = pyrosetta.pose_from_sequence('A' * 10)
polyA.pdb_info().name("polyA")

pmm.apply(polyA)


### # Defino los angulos phi/psi cercanos a una helice alfa

def randTrial_alpha(your_pose):
    randNum = random.randint(2, your_pose.total_residue())
    currPhi = your_pose.phi(randNum)
    currPsi = your_pose.psi(randNum)
    newPhi = random.gauss(-60, 25)
    newPsi = random.gauss(-50, 25)
    #newPhi = random.gauss(currPhi, 25)
    #newPsi = random.gauss(currPsi, 25)
    your_pose.set_phi(randNum,newPhi) 
    your_pose.set_psi(randNum,newPsi)
    #pmm.apply(your_pose)
    return your_pose


### Scoring move

sfxn = get_fa_scorefxn()

def score(your_pose):
    return sfxn(your_pose)


### Accept/Reject Pose
def decision(before_pose, after_pose):
    E = score(after_pose) - score(before_pose)
    if E < 0:
        return after_pose
    elif random.uniform(0, 1) >= math.exp(-E/1):
        return before_pose
    else:
        return after_pose


 ### Execution

def basic_folding(your_pose, outputfile):
    """Your basic folding algorithm that completes 100 Monte-Carlo iterations on a given pose"""
    
    lowest_pose = Pose() # Create an empty pose for tracking the lowest energy pose.
    
    for i in range(100000):
        if i == 0:
            lowest_pose.assign(your_pose)
            
        before_pose = Pose()
        before_pose.assign(your_pose) # keep track of pose before random move

        after_pose = Pose()
        after_pose.assign(randTrial_alpha(your_pose)) # do random move and store the pose
        
        your_pose.assign(decision(before_pose, after_pose)) # keep the new pose or old pose
        
        if score(your_pose) < score(lowest_pose): # updating lowest pose
            lowest_pose.assign(your_pose)
        if (i % 100==0):
            pmm.apply(your_pose)
            print("Iteration # %i" %i) # output   
            print("Current pose score: %1.3f" %score(your_pose)) # output
            print("Lowest pose score: %1.3f" %score(lowest_pose)) # output
    dump_pdb(lowest_pose, outputfile)    
    return lowest_pose


basic_folding(polyA, "polyA-freefold.pdb")


