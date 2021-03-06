# PageTest

A Python implementation of Page’s test (Page, 1963)


## Description

Page’s test evaluates the hypothesis that *X*<sub>1</sub> &ge; *X*<sub>2</sub> &ge; *X*<sub>3</sub> &ge; ... &ge; *X*<sub>n</sub> (descending trend) or *X*<sub>1</sub> &le; *X*<sub>2</sub> &le; *X*<sub>3</sub> &le; ... &le; *X*<sub>n</sub> (ascending trend) against the null hypothesis that *X*<sub>1</sub> = *X*<sub>2</sub> = *X*<sub>3</sub> = ... = *X*<sub>n</sub> (no trend). The *a-priori* hypothesis for the directionality of the trend must be specified (by default the program assumes a descending trend).

The program takes a matrix, with treatments along the columns and replications along the rows, and returns Page’s (1963) *L* statistic, along with its *p*-value.

The program calculates the exact *p*-value using Equation 4 in Page (1963, p. 224). For small values of *m* and *n*, the program can optionally use the critical values of *L* given in Page (1963) to calculate the *p*-value.

Although the test is commonly referred to as a trend test, it does not strictly test for a trend across the entire dataset. Rather, the test will return a significant result if at least one data point goes up (or down in the case of a descending hypothesis) in each replication.


## Requirements

Scipy – http://scipy.org


## Parameters

- ```matrix``` *list*: Data matrix (formated as a list of lists) with treatments along the columns and replications along the rows.
- ```ascending``` *bool*, optional: Set to True if hypothesizing an ascending trend, False if hypothesizing a descending trend (default: False).
- ```use_critical_values``` *bool*, optional: Set to True to use the critical values from Page (1963) rather than compute an exact p-vaue (default: False).


## Return values

- ```L``` *float*: Page’s L statistic
- ```m``` *int*: Number of replications
- ```n``` *int*: Number of treatments
- ```p``` *float*: P-value


## Usage example

Import the module:

```python
import Page
```

Input your data in the form of a matrix (represented in Python as a list of lists). Treatments go along the columns and replications go down the rows.

```python
data = [[100,90,105,70,5], [200,150,80,50,10], [121,130,75,20,25], [90,75,76,54,32]]
```

Run Page’s test on your data:

```python
Page.Test(data)
(214.0, 4, 5, 0.00033692926567685522)
```

The result is a 4-tuple (l, m, n, p), where l = Page’s *L* statistic, m = number of replications, n = number of treatments, and p is the *p*-value.

If you hypothesize an ascending trend (rather than descending), set the ```ascending``` argument to ```True```:

```python
Page.Test(data, ascending=True)
(146.0, 4, 5, 'n.s.')
```

If you want to use Page’s critical values (rather than calculate an exact *p*-value) set the ```use_critical_values``` argument to ```True```:

```python
Page.Test(data, use_critical_values=True)
(214.0, 4, 5, '< 0.001')
```


## References

Page, E. B. (1963). Ordered hypotheses for multiple treatments: A significance test for linear ranks. *Journal of the American Statistical Association*, *58*, 216–230. doi:[10.2307/2282965](http://dx.doi.org/10.2307%2F2282965)

Wikipedia: http://en.wikipedia.org/wiki/Page's_trend_test
