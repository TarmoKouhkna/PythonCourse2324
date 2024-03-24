# You are given two interior angles (in degrees) of a triangle.
# Write a function to return the 3rd.
# Note: only positive integers will be tested.
# https://en.wikipedia.org/wiki/Triangle
import other_angle

def test_other_angle():
  assert other_angle.other_angle(30, 60) == 90
  assert other_angle.other_angle(60, 60)== 60
  assert other_angle.other_angle(43, 78)== 59
  assert other_angle.other_angle(10, 20)== 150
