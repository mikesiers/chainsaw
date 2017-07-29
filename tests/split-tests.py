import sys
sys.path.append('../')
from src.chainsaw import gain_ratio_split, cost_reduction_split
import pandas as pd

class test_split_functions(unittest.TestCase):
  def test_gain_ratio(self):
    # Test that the correct best split is found for a dataset with one
    # numerical attribute.
    dataframe = pd.read_csv('data/LOC_SDP.csv')
    test = gain_ratio_split(Node(data=dataframe), 2)
    self.assertEqual(test, Split_Test('numerical', 'LOC', 73.5)

    # Test that the correct best split is found for a dataset with one
    # categorical attribute.
    dataframe = pd.read_csv('data/Language_SDP.csv')
    test = gain_ratio_split(Node(data=dataframe), 2)
    self.assertEqual(test, Split_Test('categorical', 'Language', None))

    # Test that the correct best split is found for a dataset with a numerical
    # attribute and a categorical attribute.
    dataframe = pd.read_csv('data/Language_LOC_SDP.csv')
    test = gain_ratio_split(Node(data=dataframe), 2)
    self.assertEqual(test, Split_Test('numerical', 'LOC', 73.5)

    # Test that the correct best split is found when minimum_records is
    # changed.
    dataframe = pd.read_csv('data/LOC_SDP.csv')
    test = gain_ratio_split(Node(data=dataframe), 7)
    self.assertEqual(test, Split_Test('numerical', 'LOC', 69)

  def test_cost_reduction(self):
    # Define a cost matrix and the positive class for use in testing.
    cost_matrix = {'TP' : 1, 'TN' : 0, 'FP' : 1, 'FN' : 5}
    positive_class = '1'

    # Test that the correct best split is found for a dataset with one
    # numerical attribute.
    dataframe = pd.read_csv('data/LOC_SDP.csv')
    node = Node(data=dataframe)
    test = cost_reduction_split(node, positive_class, cost_matrix)
    self.assertEqual(test, Split_Test('numerical', 'LOC', 73.5)
                                                                                
    # Test that the correct best split is found for a dataset with one
    # categorical attribute.
    dataframe = pd.read_csv('data/Language_SDP.csv')
    node = Node(data=dataframe)
    test = cost_reduction_split(node, positive_class, cost_matrix)
    self.assertEqual(test, Split_Test('categorical', 'Language', None))
                                                                                
    # Test that the correct best split is found for a dataset with a numerical
    # attribute and a categorical attribute.
    dataframe = pd.read_csv('data/Language_LOC_SDP.csv')
    node = Node(data=dataframe)
    test = cost_reduction_split(node, positive_class, cost_matrix)
    self.assertEqual(test, Split_Test('numerical', 'LOC', 73.5)

if __name__ == '__main__':
    unittest.main(exit=False)
