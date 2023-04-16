import matplotlib
import matplotlib.pyplot as plt
import scipy.stats
import numpy as np

# Note the Greek map uses Q and M instead of Qoppa and San because
# those letters end up being double-wide and stick out on the plots.
greek_map = {
    'alpha' : 'Α',
    'beta' : 'Β',
    'gamma' : 'Γ',
    'delta' : 'Δ',
    'epsilon' : 'Ε',
    'digamma' : 'Ϝ',
    'zeta' : 'Ζ',
    'eta' : 'Η',
    'theta' : 'Θ',
    'iota' : 'Ι',
    'kappa' : 'Κ',
    'lambda' : 'Λ',
    'mu' : 'Μ',
    'nu' : 'Ν',
    'omicron' : 'Ο',
    'pi' : 'Π',
    'san' : 'M',
    'qoppa' : 'Q',
    'rho' : 'Ρ',
    'sigma' : 'Σ',
    'tau' : 'Τ',
    'upsilon' : 'Υ',
    'phi' : 'Φ',
    'chi' : 'Χ',
    'psi' : 'Ψ',
    'omega' : 'Ω',
}

latin_map = {
    'alpha' : 'A',
    'beta' : 'B',
    'gamma' : 'C',
    'delta' : 'D',
    'epsilon' : 'E',
    'digamma' : 'F',
    'zeta' : 'Z',
    'eta' : 'H',
    'iota' : 'I',
    'kappa' : 'K',
    'lambda' : 'L',
    'mu' : 'M',
    'nu' : 'N',
    'omicron' : 'O',
    'pi' : 'P',
    'qoppa' : 'Q',
    'rho' : 'R',
    'sigma' : 'S',
    'tau' : 'T',
    'upsilon' : 'Y',
    'chi' : 'X',
}

futhark_map = {
    'alpha' : 'ᚨ',
    'beta' : 'ᛒ',
    'gamma' : 'ᚲ',
    'epsilon' : 'ᛖ',
    'digamma' : 'ᚠ',
    'zeta' : 'ᛃ',
    'eta' : 'ᚻ',
    'theta' : 'ᛜ',
    'iota' : 'ᛁ',
    'lambda' : 'ᛚ',
    'mu' : 'ᛗ',
    'nu' : 'ᚾ',
    'pi' : 'ᛈ',
    'san' : 'ᛞ',
    'qoppa' : 'ᚹ',
    'rho' : 'ᚱ',
    'sigma' : 'ᛊ',
    'tau' : 'ᛏ',
    'upsilon' : 'ᚢ',
    'phi' : 'ᚦ',
    'chi' : 'ᚷ',
    'psi' : 'ᛉ',
    'omega' : 'ᛟ',
    'ihwaz': 'ᛇ',
}

archaic_greek = {
    'name': 'Archaic Greek',
    'order': [
        'alpha',
        'beta',
        'gamma',
        'delta',
        'epsilon',
        'digamma',
        'zeta',
        'eta',
        'theta',
        'iota',
        'kappa',
        'lambda',
        'mu',
        'nu',
        'omicron',
        'pi',
        'san',
        'qoppa',
        'rho',
        'sigma',
        'tau',
        'upsilon',
        'phi',
        'chi',
        'psi',
        'omega',
    ]
}

etruscan = {
    'name': 'Etruscan Mediation',
    'order': [
        'alpha',
        'beta',
        'gamma',
        'delta',
        'epsilon',
        'digamma',
        'zeta',
        'eta',
        'theta',
        'iota',
        'kappa',
        'lambda',
        'mu',
        'nu',
        'omicron',
        'pi',
        'san',
        'qoppa',
        'rho',
        'sigma',
        'tau',
        'upsilon',
        'phi',
        'chi',
        'psi',
    ]
}

lepontic = {
    'name': 'Lepontic Mediation',
    'order': [
        'alpha',
        'beta',
        'gamma',
        'epsilon',
        'digamma',
        'zeta',
        'eta',
        'theta',
        'iota',
        'lambda',
        'mu',
        'nu',
        'pi',
        'san',
        'qoppa',
        'rho',
        'sigma',
        'tau',
        'upsilon',
        'phi',
        'chi',
        'psi',
        'omicron',
    ]
}

proto_futhark = {
    'name': 'Proto-Elder Futhark',
    'order': [
        'alpha',
        'beta',
        'gamma',
        'epsilon',
        'zeta',
        'eta',
        'theta',
        'iota',
        'lambda',
        'mu',
        'nu',
        'pi',
        'san',
        'qoppa',
        'rho',
        'sigma',
        'tau',
        'upsilon',
        'phi',
        'chi',
        'psi',
        'omega',
    ]
}

futhark = {
    'name': 'Elder Futhark',
    'order': [
        'digamma',
        'upsilon',
        'phi',
        'alpha',
        'rho',
        'gamma',
        'chi',
        'qoppa',
        'eta',
        'nu',
        'iota',
        'zeta',
        'pi',
        'ihwaz',
        'psi',
        'sigma',
        'tau',
        'beta',
        'epsilon',
        'mu',
        'lambda',
        'theta',
        'san',
        'omega',
    ]
}

roman = {
    'name': 'Roman Mediation',
    'order': [
        'alpha',
        'beta',
        'gamma',
        'delta',
        'epsilon',
        'digamma',
        'eta',
        'iota',
        'kappa',
        'lambda',
        'mu',
        'nu',
        'omicron',
        'pi',
        'qoppa',
        'rho',
        'sigma',
        'tau',
        'upsilon',
        'chi',
    ]
}

modern = {
    'name': 'Early Modern Reforms',
    'order': [
        'alpha',
        'beta',
        'gamma',
        'delta',
        'epsilon',
        'digamma',
        'gamma',
        'eta',
        'iota',
        'iota',
        'kappa',
        'lambda',
        'mu',
        'nu',
        'omicron',
        'pi',
        'qoppa',
        'rho',
        'sigma',
        'tau',
        'upsilon',
        'upsilon',
        'upsilon',
        'upsilon',
        'chi',
        'zeta',
    ]
}

# Just used for the shuffled example to show what correlation in an
# actual random sample would look like.
modern_latin = {
    'name': 'Modern Alphabet',
    'order': [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
    ]
}

# A shuffled version from the slides in the UNM talk
modern_latin_shuffled = {
    'name': 'Shuffled Modern Alphabet',
    'order': [
        'Z',
        'R',
        'U',
        'E',
        'N',
        'A',
        'L',
        'Y',
        'I',
        'X',
        'J',
        'M',
        'G',
        'D',
        'P',
        'F',
        'K',
        'T',
        'C',
        'Q',
        'V',
        'O',
        'S',
        'B',
        'W',
        'H',
    ]
}

def main():
    plot_alphabets(modern_latin, modern_latin_shuffled, filename='modern_v_modern_shuffled.png')
    plot_alphabets(futhark, proto_futhark, futhark_map, filename='futhark_v_proto_futhark.png')
    plot_alphabets(modern, archaic_greek, greek_map, filename='modern_v_archaic_greek.png')


def plot_alphabets(src, tgt, mapping=None, filename=None):
    matplotlib.rcParams['font.family'].insert(0, 'FreeMono')

    def mapchar(c):
        if mapping is None:
            return c
        return mapping[c]

    xsize, ysize = matplotlib.rcParams['figure.figsize']
    stretch = 1.3
    plt.figure(figsize=(xsize * stretch, ysize * stretch))

    plt.title(f"{src['name']} vs. {tgt['name']}", font='DejaVu Sans', fontsize=24)
    plt.xlabel(f"{src['name']} Ordering", font='DejaVu Sans', fontsize=16)
    plt.ylabel(f"{tgt['name']} Ordering", font='DejaVu Sans', fontsize=16)
    xy_pairs = match_alphabets(src['order'], tgt['order'])
    for x, y in xy_pairs:
        char = mapchar(src['order'][x-1])
        plt.text(x + .2, y + .2, char, fontsize=12)
    xs, ys = zip(*xy_pairs)
    plt.xlim(0, max(xs) + 1)
    plt.ylim(0, max(ys) + 2)
    plt.plot(xs, ys, 'o')
    plot_regression(xs, ys)
    plt.legend(loc='upper left')
    if filename:
        plt.savefig(filename)
    else:
        plt.show()


def match_alphabets(a0, a1):
    pairs = []
    for i0, c0 in enumerate(a0):
        # Ignore letters not in both alphabets
        if c0 in a1:
            pair = (i0 + 1, a1.index(c0) + 1)
            pairs.append(pair)
    return pairs


def plot_regression(src, tgt):
    line = scipy.stats.linregress(src, tgt)
    spearman = scipy.stats.spearmanr(src, tgt)
    plt.plot(src, np.asarray(src) * line.slope + line.intercept, label=f"ρ={spearman.statistic:0.02},p={spearman.pvalue:0.02}")


if __name__ == '__main__':
    main()
