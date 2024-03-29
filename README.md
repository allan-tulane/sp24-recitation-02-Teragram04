# CMPS 2200  Recitation 02

**Name (Team Member 1):**_Margaret Parsons____  
**Name (Team Member 2):**_________________________

In this recitation, we will investigate recurrences. 
To complete this recitation, follow the instructions in this document. Some of your answers will go in this file, and others will require you to edit `main.py`.



## Running and testing your code
- To run tests, from the command-line shell, you can run
  + `pytest test_main.py` will run all tests
  + `pytest test_main.py::test_one` will just run `test_one`
  + We recommend running one test at a time as you are debugging.

## Turning in your work

- Once complete, click on the "Git" icon in the left pane on repl.it.
- Enter a commit message in the "what did you change?" text box
- Click "commit and push." This will push your code to your github repository.
- Although you are working as a team, please have each team member submit the same code to their repository. One person can copy the code to their repl.it and submit it from there.

## Recurrences

In class, we've started looking at recurrences and how to we can establish asymptotic bounds on their values as a function of $n$. In this lab, we'll write some code to generate recursion trees (via a recursive function) for certain kinds of recurrences. By summing up nodes in the recurrence tree (that represent contributions to the recurrence) we can compare their total cost against the corresponding asymptotic bounds. We'll focus on  recurrences of the form:

$$ W(n) = aW(n/b) + f(n) $$

where W(1) = 1.

- [x] 1. (2 point) In `main.py`, you have stub code which includes a function `simple_work_calc`. Implement this function to return the value of $W(n)$ for arbitrary values of $a$ and $b$ with $f(n)=n$.

- [x] 2. (2 point) Test that your function is correct by calling from the command-line `pytest test_main.py::test_simple_work` by completing the test cases and adding 3 additional ones.

- [x] 3. (2 point) Now implement `work_calc`, which generalizes the above so that we can now input $a$, $b$ and a *function* $f(n)$ as arguments. Test this code by completing the test cases in `test_work` and adding 3 more cases.

- [x] 4. (2 point) Now, derive the asymptotic behavior of W(n) using
       -f(n) = 1,
       -f(n) = log n
       -f(n) = n.
      Then, generate actual values for W(n) for your code and confirm that the trends match your derivations.

**Derived behavior:** 
  + f(n) = 1 : Constant (a and b cancel)
  + f(n) = log n : w(logn) + n (when a and b are the same, they cancel)
  + f(n) = n : n (if a and b are the same), otherwise it's an/b

**Actual values (using work_calc(10, 2, 2, lambda n: ...)**
  + f(n) = 1: 15
  + f(n) = logn: 16.2
  + f(n) = n: 36

- [x] 5. (4 points) Now that you have a nice way to empirically generate values of W(n), we can look at the relationship between a, b, and f(n). Suppose that f(n) = n^c. What is the asypmptotic behavior of W(n) if c < log_b a? What about c > log_b a? And if they are equal? Modify `test_compare_work` to compare empirical values for different work functions (at several different values of n) to justify your answer. 

**Case 1: c < log_b a**
Let c = 1, let b= 2, let a =10, let f(n) = n^2.

**Case 2: c > log_b a**
let c = 3, let b = 2, let a = 10, let f(n) = n^3

**Results (formatted as [(sizes,work_fn1,work_fn2)]**
[(10, 1111, 4050), (20, 11111, 48500), (50, 111111, 1040050), (100, 1111111, 11400500), (1000, 1111111111, 21633005000), (5000, 1111111111111, 6326700005000), (10000, 11111111111111, 64267000050000)]

When c < log_b a, it increases at a slower rate. 

- [x] 6. (3 points) W(n) is meant to represent the running time of some recursive algorithm. Suppose we always had a processors available to us and we wanted to compute the span of the same algorithm. Implement the function `span_calc` to compute the empirical span, where the work of the algorithm is given by W(n). Implement `test_compare_span` to create a new comparison function for comparing span functions. Derive the asymptotic expressions for the span of the recurrences you used in problem 4 above. Confirm that everything matches up as it should. 

**Derived behavior (span):** 
  + f(n) = 1 : Constant 
  + f(n) = log n : S(n/2) + O(logn)
  + f(n) = n : S(n) + O(n)

