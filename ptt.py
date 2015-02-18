from scipy import stats



# PageTrendTest()
#   Run Page's trend test and return l, m, n, p,  where l = Page's L statistic,
#   m = number of replications, n = number of treatments, and p = p-value.

def PageTrendTest(matrix, ascending_trend=False, use_critical_values=False):
    ValidateInput(matrix, ascending_trend, use_critical_values)
    if ascending_trend == True:
        matrix = MirrorMatrix(matrix)
    m = len(matrix)
    n = len(matrix[0])
    l = PageL(matrix, m, n)
    p = PageP(l, m, n, matrix, use_critical_values)
    return l, m, n, p



# PageL()
#   Calculate Page's L statistic.

def PageL(matrix, m, n):
    rank_matrix = []
    for i in range(0, m):
        rank = stats.rankdata(matrix[i])
        rank_list = []
        for j in range(0, n):
            rank_list.append(rank[n-j-1])
        rank_matrix.append(rank_list)
    ranks = []
    for i in range(0, n):
        total = sum([row[i] for row in rank_matrix])
        total *= i + 1
        ranks.append(total)
    return sum(ranks)



# PageP()
#   Caluculate a p-value for L. If an exact value was requested, call PageExactP().
#   Otherwise, check that m and n are small enough to be in the critical values
#   table and call PageCriticalP() (if not, call PageExactP()).

def PageP(l, m, n, matrix, use_critical_values):
    if use_critical_values == False:
        return PageExactP(l, m, n, matrix)
    if n == 3 and m < 21:
        return PageCriticalP(l, m, n)
    if n > 3 and n < 9 and m < 13:
        return PageCriticalP(l, m, n)
    print 'Large m and n, so calculating exact p-value instead'
    return PageExactP(l, m, n, matrix)



# PageCriticalP()
#   For small m and n, the exact p-value won't always agree with the critical
#   values given in Page (1963, p. 220). If you prefer, you can use Page's critical
#   values instead. This function looks up the critical values for m and n, and
#   finds the significance level for L.

def PageCriticalP(l, m, n):
    values = critical_values[n-3][m-2]
    significance_levels = ['< 0.001', '< 0.01', '< 0.05']
    for i in range(0, 3):
        if l >= values[i] and values[i] != None:
            return significance_levels[i]
    return 'n.s.'



# PageExactP()
#   Calculate the exact p-value using Eqation 4 in Page (1963)

def PageExactP(l, m, n, matrix):
    # Calcualte L for the opposite trend
    alt_l = PageL(MirrorMatrix(matrix), m, n)
    # If L for the opposite trend > L for the hypothesized trend, then the trend
    # can't be significant ...
    if alt_l > l:
        # ... so return 'n.s.', otherwise the exact p-value could be misleading
        # if the opposite trend happens to be significant
        return 'n.s.'
    chi_squared = ((12.0*l-3.0*m*n*(n+1.0)**2.0)**2.0)/(m*n**2.0*(n**2.0-1.0)*(n+1.0))
    p_two_tailed = 1 - stats.chi2.cdf(chi_squared, 1)
    # Return one-tailed p-value, since this is a one-tailed test
    return p_two_tailed / 2.0



# MirrorMatrix()
#   Reverses the columns of a matrix

def MirrorMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    columns = []
    for i in range(0, n):
        columns.append([row[i] for row in matrix])
    mirrored_matrix = []
    for i in range(0, m):
        new_row = [row[i] for row in columns]
        new_row.reverse()
        mirrored_matrix.append(new_row)
    return mirrored_matrix



# ValidateInput()
#   Validates the input arguments to catch common problems

def ValidateInput(matrix, ascending_trend, use_critical_values):
    if type(matrix) != list:
        raise ValueError('Matrix should be represented as a Python list')
    if type(matrix[0]) != list:
        raise ValueError('Matrix should be represented as a Python list containing Python lists')
    if type(ascending_trend) != bool:
        raise ValueError('The ascending_trend argument should be set to True or False')
    if type(use_critical_values) != bool:
        raise ValueError('The use_critical_values argument should be set to True or False')
    if type(matrix[0][0]) not in (int, float):
        raise ValueError('Each row of your matrix should contain a set of scores for a replication')
    if len(matrix) < 2:
        raise ValueError('Page\'s trend test requires at least 2 replications')
    if len(matrix[0]) < 3:
        raise ValueError('Page\'s trend test requires at least 3 treatments')
    if len(set([len(row) for row in matrix])) != 1:
        raise ValueError('Each row in your matrix should be of the same length')



# Critical values from Page (1963) for small m and n

critical_values = [[[None, None, 28], [None, 42, 41], [56, 55, 54], [70, 68, 66], [83, 81, 79], [96, 93, 91], [109, 106, 104], [121, 119, 116], [134, 131, 128], [147, 144, 141], [160, 156, 153], [172, 169, 165], [185, 181, 178], [197, 194, 190], [210, 206, 202], [223, 218, 215], [235, 231, 227], [248, 243, 239], [260, 256, 251]], [[None, 60, 58], [89, 87, 84], [117, 114, 111], [145, 141, 137], [172, 167, 163], [198, 193, 189], [225, 220, 214], [252, 246, 240], [278, 272, 266], [305, 298, 292], [331, 324, 317]], [[109, 106, 103], [160, 155, 150], [210, 204, 197], [259, 251, 244], [307, 299, 291], [355, 346, 338], [403, 393, 384], [451, 441, 431], [499, 487, 477], [546, 534, 523], [593, 581, 570]], [[178, 173, 166], [260, 252, 244], [341, 331, 321], [420, 409, 397], [499, 486, 474], [577, 563, 550], [655, 640, 625], [733, 717, 701], [811, 793, 777], [888, 869, 852], [965, 946, 928]], [[269, 261, 252], [394, 382, 370], [516, 501, 487], [637, 620, 603], [757, 737, 719], [876, 855, 835], [994, 972, 950], [1113, 1088, 1065], [1230, 1205, 1180], [1348, 1321, 1295], [1465, 1437, 1410]], [[388, 376, 362], [567, 549, 532], [743, 722, 701], [917, 893, 869], [1090, 1063, 1037], [1262, 1232, 1204], [1433, 1401, 1371], [1603, 1569, 1537], [1773, 1736, 1703], [1943, 1905, 1868], [2112, 2072, 2035]]]
