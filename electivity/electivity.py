import pandas as pd


def _normalize(available, consumed):
    """
    Convert lists of available and consumed items into normalized r and p series.
    """
    if len(available) != len(consumed):
        raise ValueError(
            "Available and consumed must be equal length list-like objects.")

    available = pd.Series(available)
    consumed = pd.Series(consumed)

    r = consumed.divide(consumed.sum())
    p = available.divide(available.sum())

    return r, p


def ivlev_forage_ratio(available, consumed):
    """
    Calculate Ivlev forage ratio E' (Ivlev 1961).

    :param list: available A list or list-like object of elements representing available resources.
    :param list: consumed A list of list-like object of elements representing consumed resources.
    :return list: A list of electivity values corresponding to each element of the input lists.
    """
    r, p = _normalize(available, consumed)

    E = r.divide(p)

    return E.values


def ivlev_electivity(available, consumed):
    """
    Calculate Ivlev electivity E (Ivlev 1961).

    :param list: available A list or list-like object of elements representing available resources.
    :param list: consumed A list of list-like object of elements representing consumed resources.
    :return list: A list of electivity values corresponding to each element of the input lists.
    """
    r, p = _normalize(available, consumed)

    E = r.subtract(p).divide(r.add(p))

    return E.values


def jacobs_electivity(available, consumed):
    """
    Calculate Jacobs electivity D (Jacobs 1974).

    :param list: available A list or list-like object of elements representing available resources.
    :param list: consumed A list of list-like object of elements representing consumed resources.
    :return list: A list of electivity values corresponding to each element of the input lists.
    """
    r, p = _normalize(available, consumed)

    D = r.subtract(p).divide(r.add(p).subtract(r.multiply(p.multiply(2))))

    return D.values


def jacobs_forage_ratio(available, consumed):
    """
    Calculate Jacobs modified forage ratio Q (Jacobs 1974).

    :param list: available A list or list-like object of elements representing available resources.
    :param list: consumed A list of list-like object of elements representing consumed resources.
    :return list: A list of electivity values corresponding to each element of the input lists.
    """
    r, p = _normalize(available, consumed)

    Q = r.multiply(p.multiply(-1).add(1)
                   ).divide(p.multiply(r.multiply(-1).add(1)))

    return Q.values


def strauss_linear(available, consumed):
    """
    Calculate Strauss' Linear Index L (Strauss 1979).

    :param list: available A list or list-like object of elements representing available resources.
    :param list: consumed A list of list-like object of elements representing consumed resources.
    :return list: A list of electivity values corresponding to each element of the input lists.
    """
    r, p = _normalize(available, consumed)

    L = r.subtract(p)

    return L.values


def chessons_alpha(available, consumed):
    """
    Calculate Chesson's alpha a (Chesson 1978) or Vanderploeg and Scavia's Selectivity W.

    :param list: available A list or list-like object of elements representing available resources.
    :param list: consumed A list of list-like object of elements representing consumed resources.
    :return list: A list of electivity values corresponding to each element of the input lists.
    """
    r, p = _normalize(available, consumed)

    a = r.divide(p).divide(r.divide(p).sum())

    return a.values


def relativized_electivity(available, consumed):
    """
    Calculate Vanderploeg and Scavia's Relativized Electivity E* (Vanderploeg and Scavia 1979).

    :param list: available A list or list-like object of elements representing available resources.
    :param list: consumed A list of list-like object of elements representing consumed resources.
    :return list: A list of electivity values corresponding to each element of the input lists.
    """
    r, p = _normalize(available, consumed)
    W = pd.Series(chessons_alpha(available, consumed))
    n = len(r)

    E = W.subtract(1/n).divide(W.add(1/n))

    return E.values
