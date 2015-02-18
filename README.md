# PageTrendTest

A Python implementation of Page’s trend test (Page, 1963)


## Description

Page’s trend test evaluates the hypothesis that *X*<sub>1</sub> > *X*<sub>2</sub> > *X*<sub>3</sub> > ... > *X*<sub>n</sub> (descending trend) or *X*<sub>1</sub> < *X*<sub>2</sub> < *X*<sub>3</sub> < ... < *X*<sub>n</sub> (ascending trend) against the null hypothesis that *X*<sub>1</sub> = *X*<sub>2</sub> = *X*<sub>3</sub> = ... = *X*<sub>n</sub> (no trend). The *a-priori* hypothesis for the directionality of the trend must be specified (by default the program assumes a descending trend).

The program takes a matrix, with treatments along the columns and replications along the rows, and returns Page’s (1963) *L* statistic, along with its *p*-value.

For small *m* and *n*, the program can use the critical values from Page (1963) to calculate the *p*-value. For larger values of *m* and *n*, the program calculates the exact *p*-value using Equation 4 in Page (1963, p. 224).


## Requirements

Scipy – http://scipy.org


## Usage

Import the module:

```python
import ptt
```

Input your data in the form of a matrix (represented in Python as a list of lists). Treatments go along the columns and replications go down the rows.

```python
data = [[100,90,105,70,5], [200,150,80,50,10], [121,130,75,20,25], [90,75,76,54,32]]
```

Run Page’s trend test:

```python
ptt.PageTrendTest(data)
(214.0, 4, 5, 0.00033692926567685522)
```

The result is a 4-tuple (l, m, n, p), where l = Page’s *L* statistic, m = number of replications, n = number of treatments, and p is the *p*-value.

If you hypothesize an ascending trend (rather than descending), set the ```ascending_trend``` argument to ```True```:

```python
ptt.PageTrendTest(data, ascending_trend=True)
(146.0, 4, 5, 'n.s.')
```

If you want to use Page’s critical values (rather than calculate an exact *p*-value) set the ```exact_p_value``` argument to ```False```:

```python
ptt.PageTrendTest(data, exact_p_value=False)
(214.0, 4, 5, '< 0.001')
```


## References

Page, E. B. (1963). Ordered hypotheses for multiple treatments: A significance test for linear ranks. *Journal of the American Statistical Association*, *58*, 216–230. doi:[10.2307/2282965](http://dx.doi.org/10.2307%2F2282965)

Wikipedia: http://en.wikipedia.org/wiki/Page's_trend_test
