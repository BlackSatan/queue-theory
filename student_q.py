import scipy.stats.t


def test_conf_t_s(dist, alpha, n, num_exp=10000):
    t = abs(stats.t.ppf(alpha / 2, n - 1))  # t-статистика
    mu = dist.mean()

    result_norm = np.zeros(num_exp)

    for exp in range(num_exp):

        sample = dist.rvs(n)
        xbar = np.mean(sample)
        s = sample.std(ddof=1)  # ddof=1 для несмещенной оценки

        SE = s / math.sqrt(len(sample))  # s вместо sigma

        ci_low_norm = xbar - t * SE  # меняем z на t
        ci_hi_norm = xbar + t * SE

        if ci_low_norm <= mu <= ci_hi_norm:
            result_norm[exp] = 1

    return result_norm.mean()


def students_quantil():
    return scipy.stats.t()
