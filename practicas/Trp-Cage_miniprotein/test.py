# Import PyRosetta
import pyrosetta
from pyrosetta import rosetta
import os

# Initialize PyRosetta
pyrosetta.init()

# Load the Trp-cage structure (PDB ID: 1L2Y)
pose = rosetta.core.import_pose.pose_from_file("1L2Y.pdb")

# Output initial pose information
print("Initial pose energies:")
print(pose.energies())

# Setting up the packer task to allow mutations at core residues
task_factory = rosetta.core.pack.task.TaskFactory()

# Add TaskOperations for design
restrict_to_repacking = rosetta.core.pack.task.operation.RestrictToRepacking()
task_factory.push_back(restrict_to_repacking)

# Load a resfile that specifies mutations in the core (students can modify this)
resfile = """
NATRO
start
8 A PIKAA L
9 A PIKAA L
10 A PIKAA L
11 A PIKAA L
16 A PIKAA W
18 A PIKAA W
20 A PIKAA W
"""
# Save the resfile for the TaskOperation
with open("resfile.txt", "w") as file:
    file.write(resfile)

# Create a task operation from the resfile
resfile_reader = rosetta.core.pack.task.operation.ReadResfile()
resfile_reader.filename("resfile.txt")
task_factory.push_back(resfile_reader)

# Set up the FastRelax protocol
relax = rosetta.protocols.relax.FastRelax()

# Set up the score function (standard score function for FastRelax)
scorefxn = rosetta.get_fa_scorefxn()

# Attach the score function to FastRelax
relax.set_scorefxn(scorefxn)

# Create a packer task for design with mutations
packer_task = task_factory.create_task_and_apply_taskoperations(pose)

# Apply FastRelax to the pose with the allowed mutations from the resfile
relax.apply(pose)

# Output the resulting pose information after FastRelax
print("Pose energies after FastRelax:")
print(pose.energies())

# Calculate the total score and display the energy changes
initial_score = scorefxn(pose)
print(f"Initial total score: {initial_score}")

# Saving the designed protein to a PDB file
pose.dump_pdb("stabilized_trpcage.pdb")

# Clean up (delete the resfile)
os.remove("resfile.txt")

print("Design complete. Stabilized mutant saved as stabilized_trpcage.pdb")

