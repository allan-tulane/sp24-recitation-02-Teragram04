from main import *


def test_simple_work():
  """ done. """
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(20, 3, 4) == 44
  assert simple_work_calc(15, 2, 2) == 49
  assert simple_work_calc(27, 3, 4) == 54


def test_work():
  assert work_calc(10, 2, 2, lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n * n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(27, 2, 2, lambda n: n * n) == 1299
  assert work_calc(5, 2, 3, lambda n: n * n) == 27
  assert work_calc(15, 2, 3, lambda n: n * n) == 279


def test_compare_work():

  # curry work_calc to create multiple work
  # functions taht can be passed to compare_work

  # create work_fn1
  # create work_fn2
  work_fn1 = lambda n: work_calc(n, 2, 2, lambda n: 1)
  work_fn2 = lambda n: work_calc(n, 2, 2, lambda n: n * n)
  res = compare_work(work_fn1, work_fn2)
  return res


print(test_compare_work())

# def test_compare_span():
# 	# TODO
