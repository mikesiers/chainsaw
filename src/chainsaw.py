"""chainsaw.py : Decision Tree Splitting Functions

This module can be used to find the best split for some data based on several
splitting criteria. It is mainly intended for use in machine learning
algorithms.

"""
import wattle
import entro

def gain_ratio_split(node, minimum_records):
  """Finds and returns the best split based on gain ratio.
  
  Args:
    node (wattle.Node): The node to calculate the best split for.
    minimum_records (Number): The minimum number of child records.

  Returns:
    (wattle.Split_Test): The best split based on gain ratio.

  """

  # These values will get updated if a better split is found.
  best_gain_ratio = 0
  best_split = None

  # Get the support values for the passed node. This is used to measure the
  # original entropy.
  parent_supports = node.get_supports().values()

  # Iterate over every possible split.
  for split in node.get_possible_splits():
    temp_node = node # This temp node gets split.
    temp_node.split({return split})

    # Get the class support counts for each resulting child.
    for child in temp_node:
      child_supports.append(get_supports().values())

    # Calculate the gain ratio for this split. If it's better than the best so
    # far, update the best split to be this split.
    gain_ratio = entro.gain_ratio(child_supports, parent_supports)
    if gain_ratio > best_gain_ratio:
      best_gain_ratio = gain_ratio
      best_split = split

  return split
