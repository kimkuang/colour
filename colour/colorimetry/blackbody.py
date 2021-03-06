# -*- coding: utf-8 -*-
"""
Blackbody - Planckian Radiator
==============================

Defines objects to compute the spectral radiance of a planckian radiator and
its spectral distribution.

See Also
--------
`Blackbody Jupyter Notebook
<http://nbviewer.jupyter.org/github/colour-science/colour-notebooks/\
blob/master/notebooks/colorimetry/blackbody.ipynb>`_

References
----------
-   :cite:`CIETC1-482004i` : CIE TC 1-48. (2004). APPENDIX E. INFORMATION ON
    THE USE OF PLANCK'S EQUATION FOR STANDARD AIR. In CIE 015:2004 Colorimetry,
    3rd Edition (pp. 77-82). ISBN:978-3-901-90633-6
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import (DEFAULT_SPECTRAL_SHAPE, SpectralDistribution)
from colour.utilities import as_float_array

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2018 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = [
    'C1', 'C2', 'N', 'planck_law', 'blackbody_spectral_radiance',
    'sd_blackbody'
]

C1 = 3.741771e-16  # 2 * math.pi * PLANCK_CONSTANT * LIGHT_SPEED ** 2
C2 = 1.4388e-2  # PLANCK_CONSTANT * LIGHT_SPEED / BOLTZMANN_CONSTANT
N = 1


def planck_law(wavelength, temperature, c1=C1, c2=C2, n=N):
    """
    Returns the spectral radiance of a blackbody at thermodynamic temperature
    :math:`T[K]` in a medium having index of refraction :math:`n`.

    Parameters
    ----------
    wavelength : numeric or array_like
        Wavelength in meters.
    temperature : numeric or array_like
        Temperature :math:`T[K]` in kelvin degrees.
    c1 : numeric or array_like, optional
        The official value of :math:`c1` is provided by the Committee on Data
        for Science and Technology (CODATA) and is
        :math:`c1=3,741771x10.16\\ W/m_2` *(Mohr and Taylor, 2000)*.
    c2 : numeric or array_like, optional
        Since :math:`T` is measured on the International Temperature Scale,
        the value of :math:`c2` used in colorimetry should follow that adopted
        in the current International Temperature Scale (ITS-90)
        *(Preston-Thomas, 1990; Mielenz et aI., 1991)*, namely
        :math:`c2=1,4388x10.2\\ m/K`.
    n : numeric or array_like, optional
        Medium index of refraction. For dry air at 15C and 101 325 Pa,
        containing 0,03 percent by volume of carbon dioxide, it is
        approximately 1,00028 throughout the visible region although
        *CIE 15:2004* recommends using :math:`n=1`.

    Returns
    -------
    numeric or ndarray
        Radiance in *watts per steradian per square metre*.

    Notes
    -----
    -   The following form implementation is expressed in term of wavelength.
    -   The SI unit of radiance is *watts per steradian per square metre*.

    References
    ----------
    :cite:`CIETC1-482004i`

    Examples
    --------
    >>> # Doctests ellipsis for Python 2.x compatibility.
    >>> planck_law(500 * 1e-9, 5500)  # doctest: +ELLIPSIS
    20472701909806.5...
    """

    l = as_float_array(wavelength)  # noqa
    t = as_float_array(temperature)

    p = (((c1 * n ** -2 * l ** -5) / np.pi) * (np.exp(c2 /
                                                      (n * l * t)) - 1) ** -1)

    return p


blackbody_spectral_radiance = planck_law


def sd_blackbody(temperature, shape=DEFAULT_SPECTRAL_SHAPE, c1=C1, c2=C2, n=N):
    """
    Returns the spectral distribution of the planckian radiator for given
    temperature :math:`T[K]`.

    Parameters
    ----------
    temperature : numeric
        Temperature :math:`T[K]` in kelvin degrees.
    shape : SpectralShape, optional
        Spectral shape used to create the spectral distribution of the
        planckian radiator.
    c1 : numeric, optional
        The official value of :math:`c1` is provided by the Committee on Data
        for Science and Technology (CODATA) and is
        :math:`c1=3,741771x10.16\\ W/m_2` *(Mohr and Taylor, 2000)*.
    c2 : numeric, optional
        Since :math:`T` is measured on the International Temperature Scale,
        the value of :math:`c2` used in colorimetry should follow that adopted
        in the current International Temperature Scale (ITS-90)
        *(Preston-Thomas, 1990; Mielenz et aI., 1991)*, namely
        :math:`c2=1,4388x10.2\\ m/K`.
    n : numeric, optional
        Medium index of refraction. For dry air at 15C and 101 325 Pa,
        containing 0,03 percent by volume of carbon dioxide, it is
        approximately 1,00028 throughout the visible region although
        *CIE 15:2004* recommends using :math:`n=1`.

    Returns
    -------
    SpectralDistribution
        Blackbody spectral distribution.

    Examples
    --------
    >>> from colour import STANDARD_OBSERVERS_CMFS
    >>> from colour.utilities import numpy_print_options
    >>> cmfs = STANDARD_OBSERVERS_CMFS['CIE 1931 2 Degree Standard Observer']
    >>> with numpy_print_options(suppress=True):
    ...     sd_blackbody(5000, cmfs.shape)  # doctest: +ELLIPSIS
    SpectralDistribution([[  3.60000000e+02,   6.65427827e+12],
                          [  3.61000000e+02,   6.70960528e+12],
                          [  3.62000000e+02,   6.76482512e+12],
                          [  3.63000000e+02,   6.81993308e+12],
                          [  3.64000000e+02,   6.87492449e+12],
                          [  3.65000000e+02,   6.92979475e+12],
                          [  3.66000000e+02,   6.98453932e+12],
                          [  3.67000000e+02,   7.03915372e+12],
                          [  3.68000000e+02,   7.09363351e+12],
                          [  3.69000000e+02,   7.14797433e+12],
                          [  3.70000000e+02,   7.20217187e+12],
                          [  3.71000000e+02,   7.25622190e+12],
                          [  3.72000000e+02,   7.31012021e+12],
                          [  3.73000000e+02,   7.36386268e+12],
                          [  3.74000000e+02,   7.41744525e+12],
                          [  3.75000000e+02,   7.47086391e+12],
                          [  3.76000000e+02,   7.52411471e+12],
                          [  3.77000000e+02,   7.57719377e+12],
                          [  3.78000000e+02,   7.63009726e+12],
                          [  3.79000000e+02,   7.68282141e+12],
                          [  3.80000000e+02,   7.73536252e+12],
                          [  3.81000000e+02,   7.78771695e+12],
                          [  3.82000000e+02,   7.83988111e+12],
                          [  3.83000000e+02,   7.89185148e+12],
                          [  3.84000000e+02,   7.94362458e+12],
                          [  3.85000000e+02,   7.99519703e+12],
                          [  3.86000000e+02,   8.04656547e+12],
                          [  3.87000000e+02,   8.09772662e+12],
                          [  3.88000000e+02,   8.14867726e+12],
                          [  3.89000000e+02,   8.19941421e+12],
                          [  3.90000000e+02,   8.24993438e+12],
                          [  3.91000000e+02,   8.30023471e+12],
                          [  3.92000000e+02,   8.35031222e+12],
                          [  3.93000000e+02,   8.40016398e+12],
                          [  3.94000000e+02,   8.44978711e+12],
                          [  3.95000000e+02,   8.49917881e+12],
                          [  3.96000000e+02,   8.54833632e+12],
                          [  3.97000000e+02,   8.59725693e+12],
                          [  3.98000000e+02,   8.64593802e+12],
                          [  3.99000000e+02,   8.69437700e+12],
                          [  4.00000000e+02,   8.74257133e+12],
                          [  4.01000000e+02,   8.79051856e+12],
                          [  4.02000000e+02,   8.83821626e+12],
                          [  4.03000000e+02,   8.88566209e+12],
                          [  4.04000000e+02,   8.93285373e+12],
                          [  4.05000000e+02,   8.97978893e+12],
                          [  4.06000000e+02,   9.02646551e+12],
                          [  4.07000000e+02,   9.07288133e+12],
                          [  4.08000000e+02,   9.11903431e+12],
                          [  4.09000000e+02,   9.16492240e+12],
                          [  4.10000000e+02,   9.21054364e+12],
                          [  4.11000000e+02,   9.25589609e+12],
                          [  4.12000000e+02,   9.30097789e+12],
                          [  4.13000000e+02,   9.34578722e+12],
                          [  4.14000000e+02,   9.39032230e+12],
                          [  4.15000000e+02,   9.43458143e+12],
                          [  4.16000000e+02,   9.47856292e+12],
                          [  4.17000000e+02,   9.52226517e+12],
                          [  4.18000000e+02,   9.56568661e+12],
                          [  4.19000000e+02,   9.60882571e+12],
                          [  4.20000000e+02,   9.65168102e+12],
                          [  4.21000000e+02,   9.69425111e+12],
                          [  4.22000000e+02,   9.73653461e+12],
                          [  4.23000000e+02,   9.77853020e+12],
                          [  4.24000000e+02,   9.82023659e+12],
                          [  4.25000000e+02,   9.86165257e+12],
                          [  4.26000000e+02,   9.90277693e+12],
                          [  4.27000000e+02,   9.94360856e+12],
                          [  4.28000000e+02,   9.98414634e+12],
                          [  4.29000000e+02,   1.00243892e+13],
                          [  4.30000000e+02,   1.00643363e+13],
                          [  4.31000000e+02,   1.01039864e+13],
                          [  4.32000000e+02,   1.01433388e+13],
                          [  4.33000000e+02,   1.01823926e+13],
                          [  4.34000000e+02,   1.02211468e+13],
                          [  4.35000000e+02,   1.02596009e+13],
                          [  4.36000000e+02,   1.02977539e+13],
                          [  4.37000000e+02,   1.03356052e+13],
                          [  4.38000000e+02,   1.03731541e+13],
                          [  4.39000000e+02,   1.04104000e+13],
                          [  4.40000000e+02,   1.04473423e+13],
                          [  4.41000000e+02,   1.04839805e+13],
                          [  4.42000000e+02,   1.05203140e+13],
                          [  4.43000000e+02,   1.05563424e+13],
                          [  4.44000000e+02,   1.05920652e+13],
                          [  4.45000000e+02,   1.06274821e+13],
                          [  4.46000000e+02,   1.06625927e+13],
                          [  4.47000000e+02,   1.06973967e+13],
                          [  4.48000000e+02,   1.07318937e+13],
                          [  4.49000000e+02,   1.07660835e+13],
                          [  4.50000000e+02,   1.07999660e+13],
                          [  4.51000000e+02,   1.08335408e+13],
                          [  4.52000000e+02,   1.08668080e+13],
                          [  4.53000000e+02,   1.08997673e+13],
                          [  4.54000000e+02,   1.09324187e+13],
                          [  4.55000000e+02,   1.09647621e+13],
                          [  4.56000000e+02,   1.09967975e+13],
                          [  4.57000000e+02,   1.10285249e+13],
                          [  4.58000000e+02,   1.10599443e+13],
                          [  4.59000000e+02,   1.10910559e+13],
                          [  4.60000000e+02,   1.11218598e+13],
                          [  4.61000000e+02,   1.11523560e+13],
                          [  4.62000000e+02,   1.11825447e+13],
                          [  4.63000000e+02,   1.12124262e+13],
                          [  4.64000000e+02,   1.12420006e+13],
                          [  4.65000000e+02,   1.12712681e+13],
                          [  4.66000000e+02,   1.13002292e+13],
                          [  4.67000000e+02,   1.13288840e+13],
                          [  4.68000000e+02,   1.13572329e+13],
                          [  4.69000000e+02,   1.13852762e+13],
                          [  4.70000000e+02,   1.14130144e+13],
                          [  4.71000000e+02,   1.14404478e+13],
                          [  4.72000000e+02,   1.14675768e+13],
                          [  4.73000000e+02,   1.14944020e+13],
                          [  4.74000000e+02,   1.15209237e+13],
                          [  4.75000000e+02,   1.15471425e+13],
                          [  4.76000000e+02,   1.15730590e+13],
                          [  4.77000000e+02,   1.15986736e+13],
                          [  4.78000000e+02,   1.16239869e+13],
                          [  4.79000000e+02,   1.16489996e+13],
                          [  4.80000000e+02,   1.16737122e+13],
                          [  4.81000000e+02,   1.16981253e+13],
                          [  4.82000000e+02,   1.17222397e+13],
                          [  4.83000000e+02,   1.17460559e+13],
                          [  4.84000000e+02,   1.17695747e+13],
                          [  4.85000000e+02,   1.17927969e+13],
                          [  4.86000000e+02,   1.18157230e+13],
                          [  4.87000000e+02,   1.18383540e+13],
                          [  4.88000000e+02,   1.18606904e+13],
                          [  4.89000000e+02,   1.18827333e+13],
                          [  4.90000000e+02,   1.19044832e+13],
                          [  4.91000000e+02,   1.19259412e+13],
                          [  4.92000000e+02,   1.19471079e+13],
                          [  4.93000000e+02,   1.19679843e+13],
                          [  4.94000000e+02,   1.19885712e+13],
                          [  4.95000000e+02,   1.20088695e+13],
                          [  4.96000000e+02,   1.20288802e+13],
                          [  4.97000000e+02,   1.20486041e+13],
                          [  4.98000000e+02,   1.20680421e+13],
                          [  4.99000000e+02,   1.20871953e+13],
                          [  5.00000000e+02,   1.21060645e+13],
                          [  5.01000000e+02,   1.21246508e+13],
                          [  5.02000000e+02,   1.21429552e+13],
                          [  5.03000000e+02,   1.21609785e+13],
                          [  5.04000000e+02,   1.21787220e+13],
                          [  5.05000000e+02,   1.21961865e+13],
                          [  5.06000000e+02,   1.22133731e+13],
                          [  5.07000000e+02,   1.22302829e+13],
                          [  5.08000000e+02,   1.22469170e+13],
                          [  5.09000000e+02,   1.22632763e+13],
                          [  5.10000000e+02,   1.22793620e+13],
                          [  5.11000000e+02,   1.22951752e+13],
                          [  5.12000000e+02,   1.23107171e+13],
                          [  5.13000000e+02,   1.23259886e+13],
                          [  5.14000000e+02,   1.23409909e+13],
                          [  5.15000000e+02,   1.23557252e+13],
                          [  5.16000000e+02,   1.23701926e+13],
                          [  5.17000000e+02,   1.23843943e+13],
                          [  5.18000000e+02,   1.23983314e+13],
                          [  5.19000000e+02,   1.24120051e+13],
                          [  5.20000000e+02,   1.24254166e+13],
                          [  5.21000000e+02,   1.24385670e+13],
                          [  5.22000000e+02,   1.24514576e+13],
                          [  5.23000000e+02,   1.24640896e+13],
                          [  5.24000000e+02,   1.24764641e+13],
                          [  5.25000000e+02,   1.24885824e+13],
                          [  5.26000000e+02,   1.25004457e+13],
                          [  5.27000000e+02,   1.25120552e+13],
                          [  5.28000000e+02,   1.25234122e+13],
                          [  5.29000000e+02,   1.25345178e+13],
                          [  5.30000000e+02,   1.25453735e+13],
                          [  5.31000000e+02,   1.25559803e+13],
                          [  5.32000000e+02,   1.25663396e+13],
                          [  5.33000000e+02,   1.25764527e+13],
                          [  5.34000000e+02,   1.25863207e+13],
                          [  5.35000000e+02,   1.25959449e+13],
                          [  5.36000000e+02,   1.26053268e+13],
                          [  5.37000000e+02,   1.26144674e+13],
                          [  5.38000000e+02,   1.26233681e+13],
                          [  5.39000000e+02,   1.26320302e+13],
                          [  5.40000000e+02,   1.26404551e+13],
                          [  5.41000000e+02,   1.26486438e+13],
                          [  5.42000000e+02,   1.26565979e+13],
                          [  5.43000000e+02,   1.26643185e+13],
                          [  5.44000000e+02,   1.26718071e+13],
                          [  5.45000000e+02,   1.26790648e+13],
                          [  5.46000000e+02,   1.26860930e+13],
                          [  5.47000000e+02,   1.26928930e+13],
                          [  5.48000000e+02,   1.26994662e+13],
                          [  5.49000000e+02,   1.27058138e+13],
                          [  5.50000000e+02,   1.27119372e+13],
                          [  5.51000000e+02,   1.27178376e+13],
                          [  5.52000000e+02,   1.27235164e+13],
                          [  5.53000000e+02,   1.27289750e+13],
                          [  5.54000000e+02,   1.27342146e+13],
                          [  5.55000000e+02,   1.27392366e+13],
                          [  5.56000000e+02,   1.27440423e+13],
                          [  5.57000000e+02,   1.27486330e+13],
                          [  5.58000000e+02,   1.27530100e+13],
                          [  5.59000000e+02,   1.27571748e+13],
                          [  5.60000000e+02,   1.27611285e+13],
                          [  5.61000000e+02,   1.27648725e+13],
                          [  5.62000000e+02,   1.27684083e+13],
                          [  5.63000000e+02,   1.27717370e+13],
                          [  5.64000000e+02,   1.27748600e+13],
                          [  5.65000000e+02,   1.27777787e+13],
                          [  5.66000000e+02,   1.27804943e+13],
                          [  5.67000000e+02,   1.27830082e+13],
                          [  5.68000000e+02,   1.27853217e+13],
                          [  5.69000000e+02,   1.27874362e+13],
                          [  5.70000000e+02,   1.27893529e+13],
                          [  5.71000000e+02,   1.27910732e+13],
                          [  5.72000000e+02,   1.27925984e+13],
                          [  5.73000000e+02,   1.27939299e+13],
                          [  5.74000000e+02,   1.27950689e+13],
                          [  5.75000000e+02,   1.27960167e+13],
                          [  5.76000000e+02,   1.27967747e+13],
                          [  5.77000000e+02,   1.27973442e+13],
                          [  5.78000000e+02,   1.27977264e+13],
                          [  5.79000000e+02,   1.27979228e+13],
                          [  5.80000000e+02,   1.27979346e+13],
                          [  5.81000000e+02,   1.27977630e+13],
                          [  5.82000000e+02,   1.27974095e+13],
                          [  5.83000000e+02,   1.27968753e+13],
                          [  5.84000000e+02,   1.27961617e+13],
                          [  5.85000000e+02,   1.27952700e+13],
                          [  5.86000000e+02,   1.27942015e+13],
                          [  5.87000000e+02,   1.27929575e+13],
                          [  5.88000000e+02,   1.27915392e+13],
                          [  5.89000000e+02,   1.27899480e+13],
                          [  5.90000000e+02,   1.27881852e+13],
                          [  5.91000000e+02,   1.27862519e+13],
                          [  5.92000000e+02,   1.27841495e+13],
                          [  5.93000000e+02,   1.27818793e+13],
                          [  5.94000000e+02,   1.27794424e+13],
                          [  5.95000000e+02,   1.27768403e+13],
                          [  5.96000000e+02,   1.27740741e+13],
                          [  5.97000000e+02,   1.27711451e+13],
                          [  5.98000000e+02,   1.27680546e+13],
                          [  5.99000000e+02,   1.27648037e+13],
                          [  6.00000000e+02,   1.27613938e+13],
                          [  6.01000000e+02,   1.27578261e+13],
                          [  6.02000000e+02,   1.27541018e+13],
                          [  6.03000000e+02,   1.27502222e+13],
                          [  6.04000000e+02,   1.27461885e+13],
                          [  6.05000000e+02,   1.27420020e+13],
                          [  6.06000000e+02,   1.27376637e+13],
                          [  6.07000000e+02,   1.27331750e+13],
                          [  6.08000000e+02,   1.27285371e+13],
                          [  6.09000000e+02,   1.27237512e+13],
                          [  6.10000000e+02,   1.27188185e+13],
                          [  6.11000000e+02,   1.27137402e+13],
                          [  6.12000000e+02,   1.27085175e+13],
                          [  6.13000000e+02,   1.27031516e+13],
                          [  6.14000000e+02,   1.26976436e+13],
                          [  6.15000000e+02,   1.26919949e+13],
                          [  6.16000000e+02,   1.26862064e+13],
                          [  6.17000000e+02,   1.26802795e+13],
                          [  6.18000000e+02,   1.26742153e+13],
                          [  6.19000000e+02,   1.26680149e+13],
                          [  6.20000000e+02,   1.26616795e+13],
                          [  6.21000000e+02,   1.26552103e+13],
                          [  6.22000000e+02,   1.26486085e+13],
                          [  6.23000000e+02,   1.26418751e+13],
                          [  6.24000000e+02,   1.26350113e+13],
                          [  6.25000000e+02,   1.26280183e+13],
                          [  6.26000000e+02,   1.26208972e+13],
                          [  6.27000000e+02,   1.26136491e+13],
                          [  6.28000000e+02,   1.26062751e+13],
                          [  6.29000000e+02,   1.25987764e+13],
                          [  6.30000000e+02,   1.25911540e+13],
                          [  6.31000000e+02,   1.25834092e+13],
                          [  6.32000000e+02,   1.25755429e+13],
                          [  6.33000000e+02,   1.25675563e+13],
                          [  6.34000000e+02,   1.25594505e+13],
                          [  6.35000000e+02,   1.25512265e+13],
                          [  6.36000000e+02,   1.25428855e+13],
                          [  6.37000000e+02,   1.25344285e+13],
                          [  6.38000000e+02,   1.25258566e+13],
                          [  6.39000000e+02,   1.25171709e+13],
                          [  6.40000000e+02,   1.25083724e+13],
                          [  6.41000000e+02,   1.24994622e+13],
                          [  6.42000000e+02,   1.24904413e+13],
                          [  6.43000000e+02,   1.24813108e+13],
                          [  6.44000000e+02,   1.24720718e+13],
                          [  6.45000000e+02,   1.24627252e+13],
                          [  6.46000000e+02,   1.24532721e+13],
                          [  6.47000000e+02,   1.24437136e+13],
                          [  6.48000000e+02,   1.24340506e+13],
                          [  6.49000000e+02,   1.24242842e+13],
                          [  6.50000000e+02,   1.24144153e+13],
                          [  6.51000000e+02,   1.24044450e+13],
                          [  6.52000000e+02,   1.23943743e+13],
                          [  6.53000000e+02,   1.23842042e+13],
                          [  6.54000000e+02,   1.23739356e+13],
                          [  6.55000000e+02,   1.23635696e+13],
                          [  6.56000000e+02,   1.23531072e+13],
                          [  6.57000000e+02,   1.23425492e+13],
                          [  6.58000000e+02,   1.23318967e+13],
                          [  6.59000000e+02,   1.23211506e+13],
                          [  6.60000000e+02,   1.23103120e+13],
                          [  6.61000000e+02,   1.22993816e+13],
                          [  6.62000000e+02,   1.22883606e+13],
                          [  6.63000000e+02,   1.22772498e+13],
                          [  6.64000000e+02,   1.22660502e+13],
                          [  6.65000000e+02,   1.22547627e+13],
                          [  6.66000000e+02,   1.22433883e+13],
                          [  6.67000000e+02,   1.22319278e+13],
                          [  6.68000000e+02,   1.22203821e+13],
                          [  6.69000000e+02,   1.22087523e+13],
                          [  6.70000000e+02,   1.21970391e+13],
                          [  6.71000000e+02,   1.21852435e+13],
                          [  6.72000000e+02,   1.21733664e+13],
                          [  6.73000000e+02,   1.21614087e+13],
                          [  6.74000000e+02,   1.21493712e+13],
                          [  6.75000000e+02,   1.21372548e+13],
                          [  6.76000000e+02,   1.21250605e+13],
                          [  6.77000000e+02,   1.21127890e+13],
                          [  6.78000000e+02,   1.21004413e+13],
                          [  6.79000000e+02,   1.20880182e+13],
                          [  6.80000000e+02,   1.20755205e+13],
                          [  6.81000000e+02,   1.20629491e+13],
                          [  6.82000000e+02,   1.20503049e+13],
                          [  6.83000000e+02,   1.20375887e+13],
                          [  6.84000000e+02,   1.20248012e+13],
                          [  6.85000000e+02,   1.20119434e+13],
                          [  6.86000000e+02,   1.19990161e+13],
                          [  6.87000000e+02,   1.19860200e+13],
                          [  6.88000000e+02,   1.19729560e+13],
                          [  6.89000000e+02,   1.19598249e+13],
                          [  6.90000000e+02,   1.19466275e+13],
                          [  6.91000000e+02,   1.19333646e+13],
                          [  6.92000000e+02,   1.19200370e+13],
                          [  6.93000000e+02,   1.19066454e+13],
                          [  6.94000000e+02,   1.18931907e+13],
                          [  6.95000000e+02,   1.18796736e+13],
                          [  6.96000000e+02,   1.18660949e+13],
                          [  6.97000000e+02,   1.18524554e+13],
                          [  6.98000000e+02,   1.18387558e+13],
                          [  6.99000000e+02,   1.18249969e+13],
                          [  7.00000000e+02,   1.18111794e+13],
                          [  7.01000000e+02,   1.17973040e+13],
                          [  7.02000000e+02,   1.17833716e+13],
                          [  7.03000000e+02,   1.17693829e+13],
                          [  7.04000000e+02,   1.17553385e+13],
                          [  7.05000000e+02,   1.17412392e+13],
                          [  7.06000000e+02,   1.17270858e+13],
                          [  7.07000000e+02,   1.17128789e+13],
                          [  7.08000000e+02,   1.16986192e+13],
                          [  7.09000000e+02,   1.16843075e+13],
                          [  7.10000000e+02,   1.16699445e+13],
                          [  7.11000000e+02,   1.16555309e+13],
                          [  7.12000000e+02,   1.16410673e+13],
                          [  7.13000000e+02,   1.16265544e+13],
                          [  7.14000000e+02,   1.16119930e+13],
                          [  7.15000000e+02,   1.15973836e+13],
                          [  7.16000000e+02,   1.15827271e+13],
                          [  7.17000000e+02,   1.15680240e+13],
                          [  7.18000000e+02,   1.15532749e+13],
                          [  7.19000000e+02,   1.15384807e+13],
                          [  7.20000000e+02,   1.15236419e+13],
                          [  7.21000000e+02,   1.15087591e+13],
                          [  7.22000000e+02,   1.14938331e+13],
                          [  7.23000000e+02,   1.14788644e+13],
                          [  7.24000000e+02,   1.14638537e+13],
                          [  7.25000000e+02,   1.14488017e+13],
                          [  7.26000000e+02,   1.14337088e+13],
                          [  7.27000000e+02,   1.14185759e+13],
                          [  7.28000000e+02,   1.14034034e+13],
                          [  7.29000000e+02,   1.13881921e+13],
                          [  7.30000000e+02,   1.13729424e+13],
                          [  7.31000000e+02,   1.13576551e+13],
                          [  7.32000000e+02,   1.13423307e+13],
                          [  7.33000000e+02,   1.13269698e+13],
                          [  7.34000000e+02,   1.13115730e+13],
                          [  7.35000000e+02,   1.12961409e+13],
                          [  7.36000000e+02,   1.12806741e+13],
                          [  7.37000000e+02,   1.12651731e+13],
                          [  7.38000000e+02,   1.12496385e+13],
                          [  7.39000000e+02,   1.12340710e+13],
                          [  7.40000000e+02,   1.12184710e+13],
                          [  7.41000000e+02,   1.12028391e+13],
                          [  7.42000000e+02,   1.11871759e+13],
                          [  7.43000000e+02,   1.11714819e+13],
                          [  7.44000000e+02,   1.11557577e+13],
                          [  7.45000000e+02,   1.11400038e+13],
                          [  7.46000000e+02,   1.11242208e+13],
                          [  7.47000000e+02,   1.11084092e+13],
                          [  7.48000000e+02,   1.10925695e+13],
                          [  7.49000000e+02,   1.10767023e+13],
                          [  7.50000000e+02,   1.10608080e+13],
                          [  7.51000000e+02,   1.10448872e+13],
                          [  7.52000000e+02,   1.10289405e+13],
                          [  7.53000000e+02,   1.10129683e+13],
                          [  7.54000000e+02,   1.09969711e+13],
                          [  7.55000000e+02,   1.09809495e+13],
                          [  7.56000000e+02,   1.09649039e+13],
                          [  7.57000000e+02,   1.09488348e+13],
                          [  7.58000000e+02,   1.09327427e+13],
                          [  7.59000000e+02,   1.09166282e+13],
                          [  7.60000000e+02,   1.09004917e+13],
                          [  7.61000000e+02,   1.08843336e+13],
                          [  7.62000000e+02,   1.08681545e+13],
                          [  7.63000000e+02,   1.08519548e+13],
                          [  7.64000000e+02,   1.08357350e+13],
                          [  7.65000000e+02,   1.08194956e+13],
                          [  7.66000000e+02,   1.08032370e+13],
                          [  7.67000000e+02,   1.07869596e+13],
                          [  7.68000000e+02,   1.07706640e+13],
                          [  7.69000000e+02,   1.07543506e+13],
                          [  7.70000000e+02,   1.07380198e+13],
                          [  7.71000000e+02,   1.07216721e+13],
                          [  7.72000000e+02,   1.07053078e+13],
                          [  7.73000000e+02,   1.06889276e+13],
                          [  7.74000000e+02,   1.06725317e+13],
                          [  7.75000000e+02,   1.06561206e+13],
                          [  7.76000000e+02,   1.06396947e+13],
                          [  7.77000000e+02,   1.06232545e+13],
                          [  7.78000000e+02,   1.06068004e+13],
                          [  7.79000000e+02,   1.05903327e+13],
                          [  7.80000000e+02,   1.05738520e+13],
                          [  7.81000000e+02,   1.05573585e+13],
                          [  7.82000000e+02,   1.05408527e+13],
                          [  7.83000000e+02,   1.05243351e+13],
                          [  7.84000000e+02,   1.05078060e+13],
                          [  7.85000000e+02,   1.04912657e+13],
                          [  7.86000000e+02,   1.04747147e+13],
                          [  7.87000000e+02,   1.04581535e+13],
                          [  7.88000000e+02,   1.04415822e+13],
                          [  7.89000000e+02,   1.04250014e+13],
                          [  7.90000000e+02,   1.04084115e+13],
                          [  7.91000000e+02,   1.03918127e+13],
                          [  7.92000000e+02,   1.03752055e+13],
                          [  7.93000000e+02,   1.03585902e+13],
                          [  7.94000000e+02,   1.03419672e+13],
                          [  7.95000000e+02,   1.03253369e+13],
                          [  7.96000000e+02,   1.03086995e+13],
                          [  7.97000000e+02,   1.02920556e+13],
                          [  7.98000000e+02,   1.02754053e+13],
                          [  7.99000000e+02,   1.02587492e+13],
                          [  8.00000000e+02,   1.02420874e+13],
                          [  8.01000000e+02,   1.02254204e+13],
                          [  8.02000000e+02,   1.02087485e+13],
                          [  8.03000000e+02,   1.01920720e+13],
                          [  8.04000000e+02,   1.01753913e+13],
                          [  8.05000000e+02,   1.01587067e+13],
                          [  8.06000000e+02,   1.01420186e+13],
                          [  8.07000000e+02,   1.01253271e+13],
                          [  8.08000000e+02,   1.01086328e+13],
                          [  8.09000000e+02,   1.00919358e+13],
                          [  8.10000000e+02,   1.00752366e+13],
                          [  8.11000000e+02,   1.00585353e+13],
                          [  8.12000000e+02,   1.00418324e+13],
                          [  8.13000000e+02,   1.00251282e+13],
                          [  8.14000000e+02,   1.00084228e+13],
                          [  8.15000000e+02,   9.99171677e+12],
                          [  8.16000000e+02,   9.97501023e+12],
                          [  8.17000000e+02,   9.95830354e+12],
                          [  8.18000000e+02,   9.94159699e+12],
                          [  8.19000000e+02,   9.92489086e+12],
                          [  8.20000000e+02,   9.90818544e+12],
                          [  8.21000000e+02,   9.89148102e+12],
                          [  8.22000000e+02,   9.87477789e+12],
                          [  8.23000000e+02,   9.85807631e+12],
                          [  8.24000000e+02,   9.84137658e+12],
                          [  8.25000000e+02,   9.82467896e+12],
                          [  8.26000000e+02,   9.80798374e+12],
                          [  8.27000000e+02,   9.79129116e+12],
                          [  8.28000000e+02,   9.77460152e+12],
                          [  8.29000000e+02,   9.75791506e+12],
                          [  8.30000000e+02,   9.74123205e+12]],
                         interpolator=SpragueInterpolator,
                         interpolator_args={},
                         extrapolator=Extrapolator,
                         extrapolator_args={...})
    """

    wavelengths = shape.range()
    return SpectralDistribution(
        data=dict(
            zip(wavelengths,
                planck_law(wavelengths * 1e-9, temperature, c1, c2, n))),
        name='{0}K Blackbody'.format(temperature))
