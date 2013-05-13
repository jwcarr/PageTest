PageTrendTest
=============

A Python implementation of Page's trend test (Page, 1963)
Written by Jon W. Carr

Takes a matrix, with treatments along the columns and replications along
the rows, and returns Page's (1963) L statistic, along with its p-value.

The a-priori hypothesis for directionality must be specified - either
"ascending" or "descending" - depending on the trend that is hypothesized.

Example:

data = [[100,90,105,70,5],
        [200,150,80,50,10],
        [121,130,75,20,25],
        [90,75,76,54,32]]
ptt(data, "descending")

This will return the 4-tuple: (l, m, n, p), where l = Page's L statistic,
m = number of replications, n = number of treatments, and p = the p-value.

Reference:
Page, E. (1963). Ordered hypotheses for multiple treatments: A significance
    test for linear ranks. Journal of the American Statistical Association,
    58, 216-230.
