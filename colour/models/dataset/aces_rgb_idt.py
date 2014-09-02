#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
ACES RGB Colourspace - Input Device Transform Dataset
=====================================================

Defines the *ACES RGB* colourspace *Input Device Transform* dataset.

See Also
--------
`RGB Colourspaces IPython Notebook
<http://nbviewer.ipython.org/github/colour-science/colour-ipython/blob/master/notebooks/models/rgb.ipynb>`_  # noqa

References
----------
.. [1]  http://www.oscars.org/science-technology/council/projects/aces.html
        (Last accessed 24 February 2014)
.. [2]  `Academy Color Encoding Specification (ACES)
        <https://www.dropbox.com/sh/nt9z9m6utzvkc5m/AACBum5OdkLPCZ3d6trfVeU8a/ACES_v1.0.1.pdf>`_  # noqa
        (Last accessed 24 February 2014)
"""

from __future__ import division, unicode_literals

from colour.colorimetry import RGB_ColourMatchingFunctions

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013 - 2014 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['ACES_RICD_DATA',
           'ACES_RICD']

ACES_RICD_DATA = {
    'r_bar': {
        360.0: 1.2e-06,
        361.0: 1.4e-06,
        362.0: 1.5e-06,
        363.0: 1.7e-06,
        364.0: 1.9e-06,
        365.0: 2.2e-06,
        366.0: 2.4e-06,
        367.0: 2.7e-06,
        368.0: 3.1e-06,
        369.0: 3.5e-06,
        370.0: 3.9e-06,
        371.0: 4.3e-06,
        372.0: 4.9e-06,
        373.0: 5.4e-06,
        374.0: 6.1e-06,
        375.0: 6.9e-06,
        376.0: 7.9e-06,
        377.0: 9e-06,
        378.0: 1.02e-05,
        379.0: 1.15e-05,
        380.0: 1.28e-05,
        381.0: 1.41e-05,
        382.0: 1.54e-05,
        383.0: 1.69e-05,
        384.0: 1.87e-05,
        385.0: 2.09e-05,
        386.0: 2.37e-05,
        387.0: 2.71e-05,
        388.0: 3.09e-05,
        389.0: 3.51e-05,
        390.0: 3.97e-05,
        391.0: 4.45e-05,
        392.0: 4.99e-05,
        393.0: 5.59e-05,
        394.0: 6.31e-05,
        395.0: 7.16e-05,
        396.0: 8.19e-05,
        397.0: 9.38e-05,
        398.0: 0.0001068,
        399.0: 0.0001204,
        400.0: 0.0001339,
        401.0: 0.0001469,
        402.0: 0.0001604,
        403.0: 0.0001757,
        404.0: 0.0001941,
        405.0: 0.0002169,
        406.0: 0.0002452,
        407.0: 0.0002786,
        408.0: 0.0003169,
        409.0: 0.0003598,
        410.0: 0.000407,
        411.0: 0.0004583,
        412.0: 0.0005147,
        413.0: 0.0005773,
        414.0: 0.0006474,
        415.0: 0.0007262,
        416.0: 0.0008134,
        417.0: 0.000909,
        418.0: 0.0010141,
        419.0: 0.0011297,
        420.0: 0.001257,
        421.0: 0.0013971,
        422.0: 0.0015472,
        423.0: 0.0017023,
        424.0: 0.0018579,
        425.0: 0.002009,
        426.0: 0.0021532,
        427.0: 0.0022907,
        428.0: 0.0024207,
        429.0: 0.0025425,
        430.0: 0.0026557,
        431.0: 0.002759,
        432.0: 0.0028521,
        433.0: 0.0029352,
        434.0: 0.0030087,
        435.0: 0.0030728,
        436.0: 0.0031276,
        437.0: 0.003173,
        438.0: 0.0032096,
        439.0: 0.0032377,
        440.0: 0.0032578,
        441.0: 0.0032702,
        442.0: 0.0032753,
        443.0: 0.003274,
        444.0: 0.0032672,
        445.0: 0.0032557,
        446.0: 0.00324,
        447.0: 0.0032202,
        448.0: 0.0031972,
        449.0: 0.0031718,
        450.0: 0.0031448,
        451.0: 0.0031167,
        452.0: 0.0030871,
        453.0: 0.0030553,
        454.0: 0.0030202,
        455.0: 0.002981,
        456.0: 0.0029373,
        457.0: 0.0028892,
        458.0: 0.0028368,
        459.0: 0.0027804,
        460.0: 0.00272,
        461.0: 0.0026561,
        462.0: 0.0025883,
        463.0: 0.0025153,
        464.0: 0.0024358,
        465.0: 0.0023486,
        466.0: 0.0022527,
        467.0: 0.0021498,
        468.0: 0.0020427,
        469.0: 0.0019343,
        470.0: 0.0018271,
        471.0: 0.0017229,
        472.0: 0.001621,
        473.0: 0.0015215,
        474.0: 0.0014242,
        475.0: 0.0013289,
        476.0: 0.0012361,
        477.0: 0.0011462,
        478.0: 0.0010593,
        479.0: 0.0009753,
        480.0: 0.0008943,
        481.0: 0.0008163,
        482.0: 0.0007416,
        483.0: 0.0006706,
        484.0: 0.0006038,
        485.0: 0.0005418,
        486.0: 0.0004848,
        487.0: 0.0004326,
        488.0: 0.0003847,
        489.0: 0.0003403,
        490.0: 0.0002992,
        491.0: 0.0002609,
        492.0: 0.0002256,
        493.0: 0.0001933,
        494.0: 0.0001638,
        495.0: 0.0001373,
        496.0: 0.0001135,
        497.0: 9.26e-05,
        498.0: 7.43e-05,
        499.0: 5.87e-05,
        500.0: 4.56e-05,
        501.0: 3.51e-05,
        502.0: 2.73e-05,
        503.0: 2.25e-05,
        504.0: 2.07e-05,
        505.0: 2.23e-05,
        506.0: 2.72e-05,
        507.0: 3.57e-05,
        508.0: 4.83e-05,
        509.0: 6.52e-05,
        510.0: 8.69e-05,
        511.0: 0.0001136,
        512.0: 0.0001453,
        513.0: 0.0001822,
        514.0: 0.0002244,
        515.0: 0.0002722,
        516.0: 0.0003257,
        517.0: 0.0003847,
        518.0: 0.000449,
        519.0: 0.0005182,
        520.0: 0.000592,
        521.0: 0.0006703,
        522.0: 0.0007529,
        523.0: 0.0008398,
        524.0: 0.0009307,
        525.0: 0.0010256,
        526.0: 0.0011245,
        527.0: 0.001227,
        528.0: 0.0013323,
        529.0: 0.0014398,
        530.0: 0.0015488,
        531.0: 0.0016588,
        532.0: 0.00177,
        533.0: 0.0018826,
        534.0: 0.0019967,
        535.0: 0.0021126,
        536.0: 0.0022303,
        537.0: 0.0023496,
        538.0: 0.0024705,
        539.0: 0.0025932,
        540.0: 0.0027177,
        541.0: 0.0028439,
        542.0: 0.002972,
        543.0: 0.0031017,
        544.0: 0.0032332,
        545.0: 0.0033662,
        546.0: 0.0035008,
        547.0: 0.003637,
        548.0: 0.003775,
        549.0: 0.0039147,
        550.0: 0.0040564,
        551.0: 0.0042,
        552.0: 0.0043454,
        553.0: 0.0044926,
        554.0: 0.0046415,
        555.0: 0.004792,
        556.0: 0.004944,
        557.0: 0.0050975,
        558.0: 0.005252,
        559.0: 0.0054075,
        560.0: 0.0055636,
        561.0: 0.0057201,
        562.0: 0.0058769,
        563.0: 0.0060339,
        564.0: 0.0061913,
        565.0: 0.0063488,
        566.0: 0.0065063,
        567.0: 0.0066637,
        568.0: 0.0068207,
        569.0: 0.0069769,
        570.0: 0.0071321,
        571.0: 0.0072859,
        572.0: 0.0074383,
        573.0: 0.007589,
        574.0: 0.0077378,
        575.0: 0.0078845,
        576.0: 0.0080289,
        577.0: 0.0081707,
        578.0: 0.0083093,
        579.0: 0.0084443,
        580.0: 0.0085751,
        581.0: 0.0087015,
        582.0: 0.0088231,
        583.0: 0.0089399,
        584.0: 0.0090516,
        585.0: 0.0091582,
        586.0: 0.0092591,
        587.0: 0.0093542,
        588.0: 0.0094435,
        589.0: 0.0095269,
        590.0: 0.0096046,
        591.0: 0.0096765,
        592.0: 0.009742,
        593.0: 0.0098,
        594.0: 0.0098494,
        595.0: 0.0098891,
        596.0: 0.009918,
        597.0: 0.0099368,
        598.0: 0.0099462,
        599.0: 0.0099472,
        600.0: 0.0099405,
        601.0: 0.0099268,
        602.0: 0.0099054,
        603.0: 0.0098752,
        604.0: 0.0098355,
        605.0: 0.0097852,
        606.0: 0.0097238,
        607.0: 0.0096519,
        608.0: 0.0095705,
        609.0: 0.0094805,
        610.0: 0.0093828,
        611.0: 0.0092776,
        612.0: 0.009165,
        613.0: 0.0090448,
        614.0: 0.0089172,
        615.0: 0.0087819,
        616.0: 0.0086396,
        617.0: 0.0084904,
        618.0: 0.0083337,
        619.0: 0.0081692,
        620.0: 0.0079963,
        621.0: 0.0078151,
        622.0: 0.0076266,
        623.0: 0.0074323,
        624.0: 0.0072336,
        625.0: 0.0070319,
        626.0: 0.0068278,
        627.0: 0.0066219,
        628.0: 0.0064162,
        629.0: 0.0062122,
        630.0: 0.0060119,
        631.0: 0.0058164,
        632.0: 0.0056255,
        633.0: 0.0054382,
        634.0: 0.0052538,
        635.0: 0.0050713,
        636.0: 0.0048907,
        637.0: 0.0047124,
        638.0: 0.0045364,
        639.0: 0.0043628,
        640.0: 0.0041916,
        641.0: 0.0040228,
        642.0: 0.0038566,
        643.0: 0.0036932,
        644.0: 0.0035331,
        645.0: 0.0033765,
        646.0: 0.0032236,
        647.0: 0.0030744,
        648.0: 0.0029294,
        649.0: 0.0027888,
        650.0: 0.0026531,
        651.0: 0.0025225,
        652.0: 0.0023969,
        653.0: 0.0022759,
        654.0: 0.0021592,
        655.0: 0.0020467,
        656.0: 0.0019381,
        657.0: 0.0018335,
        658.0: 0.0017329,
        659.0: 0.0016362,
        660.0: 0.0015432,
        661.0: 0.001454,
        662.0: 0.0013685,
        663.0: 0.0012867,
        664.0: 0.0012086,
        665.0: 0.0011342,
        666.0: 0.0010635,
        667.0: 0.0009963,
        668.0: 0.0009329,
        669.0: 0.0008734,
        670.0: 0.0008179,
        671.0: 0.0007665,
        672.0: 0.0007188,
        673.0: 0.0006745,
        674.0: 0.0006334,
        675.0: 0.0005952,
        676.0: 0.0005597,
        677.0: 0.0005267,
        678.0: 0.0004957,
        679.0: 0.0004662,
        680.0: 0.0004377,
        681.0: 0.0004097,
        682.0: 0.0003825,
        683.0: 0.0003563,
        684.0: 0.0003313,
        685.0: 0.0003079,
        686.0: 0.000286,
        687.0: 0.0002656,
        688.0: 0.0002465,
        689.0: 0.0002288,
        690.0: 0.0002124,
        691.0: 0.0001973,
        692.0: 0.0001834,
        693.0: 0.0001707,
        694.0: 0.000159,
        695.0: 0.0001482,
        696.0: 0.0001384,
        697.0: 0.0001294,
        698.0: 0.0001212,
        699.0: 0.0001135,
        700.0: 0.0001063,
        701.0: 9.95e-05,
        702.0: 9.3e-05,
        703.0: 8.69e-05,
        704.0: 8.12e-05,
        705.0: 7.59e-05,
        706.0: 7.1e-05,
        707.0: 6.63e-05,
        708.0: 6.2e-05,
        709.0: 5.8e-05,
        710.0: 5.42e-05,
        711.0: 5.06e-05,
        712.0: 4.73e-05,
        713.0: 4.41e-05,
        714.0: 4.12e-05,
        715.0: 3.85e-05,
        716.0: 3.59e-05,
        717.0: 3.35e-05,
        718.0: 3.12e-05,
        719.0: 2.91e-05,
        720.0: 2.71e-05,
        721.0: 2.53e-05,
        722.0: 2.36e-05,
        723.0: 2.2e-05,
        724.0: 2.06e-05,
        725.0: 1.92e-05,
        726.0: 1.79e-05,
        727.0: 1.67e-05,
        728.0: 1.55e-05,
        729.0: 1.45e-05,
        730.0: 1.35e-05,
        731.0: 1.25e-05,
        732.0: 1.17e-05,
        733.0: 1.08e-05,
        734.0: 1.01e-05,
        735.0: 9.4e-06,
        736.0: 8.7e-06,
        737.0: 8.1e-06,
        738.0: 7.5e-06,
        739.0: 7e-06,
        740.0: 6.5e-06,
        741.0: 6e-06,
        742.0: 5.6e-06,
        743.0: 5.2e-06,
        744.0: 4.8e-06,
        745.0: 4.5e-06,
        746.0: 4.1e-06,
        747.0: 3.9e-06,
        748.0: 3.6e-06,
        749.0: 3.3e-06,
        750.0: 3.1e-06,
        751.0: 2.9e-06,
        752.0: 2.7e-06,
        753.0: 2.5e-06,
        754.0: 2.4e-06,
        755.0: 2.2e-06,
        756.0: 2.1e-06,
        757.0: 1.9e-06,
        758.0: 1.8e-06,
        759.0: 1.7e-06,
        760.0: 1.6e-06,
        761.0: 1.5e-06,
        762.0: 1.4e-06,
        763.0: 1.3e-06,
        764.0: 1.2e-06,
        765.0: 1.1e-06,
        766.0: 1e-06,
        767.0: 1e-06,
        768.0: 9e-07,
        769.0: 8e-07,
        770.0: 8e-07,
        771.0: 7e-07,
        772.0: 7e-07,
        773.0: 6e-07,
        774.0: 6e-07,
        775.0: 5e-07,
        776.0: 5e-07,
        777.0: 5e-07,
        778.0: 4e-07,
        779.0: 4e-07,
        780.0: 4e-07,
        781.0: 4e-07,
        782.0: 3e-07,
        783.0: 3e-07,
        784.0: 3e-07,
        785.0: 3e-07,
        786.0: 3e-07,
        787.0: 2e-07,
        788.0: 2e-07,
        789.0: 2e-07,
        790.0: 2e-07,
        791.0: 2e-07,
        792.0: 2e-07,
        793.0: 2e-07,
        794.0: 1e-07,
        795.0: 1e-07,
        796.0: 1e-07,
        797.0: 1e-07,
        798.0: 1e-07,
        799.0: 1e-07,
        800.0: 1e-07,
        801.0: 1e-07,
        802.0: 1e-07,
        803.0: 1e-07,
        804.0: 1e-07,
        805.0: 1e-07,
        806.0: 1e-07,
        807.0: 1e-07,
        808.0: 1e-07,
        809.0: 1e-07,
        810.0: 0.0,
        811.0: 0.0,
        812.0: 0.0,
        813.0: 0.0,
        814.0: 0.0,
        815.0: 0.0,
        816.0: 0.0,
        817.0: 0.0,
        818.0: 0.0,
        819.0: 0.0,
        820.0: 0.0,
        821.0: 0.0,
        822.0: 0.0,
        823.0: 0.0,
        824.0: 0.0,
        825.0: 0.0,
        826.0: 0.0,
        827.0: 0.0,
        828.0: 0.0,
        829.0: 0.0,
        830.0: 0.0},
    'g_bar': {
        360.0: 0.0,
        361.0: 0.0,
        362.0: 0.0,
        363.0: 0.0,
        364.0: 0.0,
        365.0: 0.0,
        366.0: 0.0,
        367.0: 0.0,
        368.0: 0.0,
        369.0: 0.0,
        370.0: 0.0,
        371.0: 0.0,
        372.0: 0.0,
        373.0: 0.0,
        374.0: 0.0,
        375.0: 0.0,
        376.0: 1e-07,
        377.0: 1e-07,
        378.0: 1e-07,
        379.0: 1e-07,
        380.0: 1e-07,
        381.0: 1e-07,
        382.0: 1e-07,
        383.0: 1e-07,
        384.0: 1e-07,
        385.0: 1e-07,
        386.0: 2e-07,
        387.0: 2e-07,
        388.0: 2e-07,
        389.0: 3e-07,
        390.0: 3e-07,
        391.0: 3e-07,
        392.0: 4e-07,
        393.0: 5e-07,
        394.0: 5e-07,
        395.0: 6e-07,
        396.0: 7e-07,
        397.0: 8e-07,
        398.0: 9e-07,
        399.0: 1e-06,
        400.0: 1.1e-06,
        401.0: 1.2e-06,
        402.0: 1.3e-06,
        403.0: 1.5e-06,
        404.0: 1.7e-06,
        405.0: 2e-06,
        406.0: 2.3e-06,
        407.0: 2.7e-06,
        408.0: 3.2e-06,
        409.0: 3.8e-06,
        410.0: 4.4e-06,
        411.0: 5.1e-06,
        412.0: 5.9e-06,
        413.0: 6.9e-06,
        414.0: 8e-06,
        415.0: 9.3e-06,
        416.0: 1.09e-05,
        417.0: 1.28e-05,
        418.0: 1.51e-05,
        419.0: 1.81e-05,
        420.0: 2.18e-05,
        421.0: 2.65e-05,
        422.0: 3.2e-05,
        423.0: 3.84e-05,
        424.0: 4.56e-05,
        425.0: 5.37e-05,
        426.0: 6.26e-05,
        427.0: 7.25e-05,
        428.0: 8.33e-05,
        429.0: 9.51e-05,
        430.0: 0.0001081,
        431.0: 0.0001221,
        432.0: 0.0001372,
        433.0: 0.0001534,
        434.0: 0.0001705,
        435.0: 0.0001886,
        436.0: 0.0002077,
        437.0: 0.0002277,
        438.0: 0.0002486,
        439.0: 0.0002702,
        440.0: 0.0002926,
        441.0: 0.0003156,
        442.0: 0.0003394,
        443.0: 0.000364,
        444.0: 0.0003897,
        445.0: 0.0004167,
        446.0: 0.000445,
        447.0: 0.0004745,
        448.0: 0.0005054,
        449.0: 0.0005377,
        450.0: 0.0005713,
        451.0: 0.0006062,
        452.0: 0.0006426,
        453.0: 0.0006803,
        454.0: 0.0007194,
        455.0: 0.0007598,
        456.0: 0.0008017,
        457.0: 0.0008449,
        458.0: 0.0008891,
        459.0: 0.0009342,
        460.0: 0.00098,
        461.0: 0.0010264,
        462.0: 0.0010734,
        463.0: 0.0011211,
        464.0: 0.0011696,
        465.0: 0.001219,
        466.0: 0.0012693,
        467.0: 0.0013205,
        468.0: 0.0013729,
        469.0: 0.0014269,
        470.0: 0.0014826,
        471.0: 0.0015401,
        472.0: 0.0015995,
        473.0: 0.0016608,
        474.0: 0.001724,
        475.0: 0.0017891,
        476.0: 0.0018563,
        477.0: 0.0019256,
        478.0: 0.0019967,
        479.0: 0.002069,
        480.0: 0.0021424,
        481.0: 0.0022166,
        482.0: 0.0022922,
        483.0: 0.00237,
        484.0: 0.0024507,
        485.0: 0.0025351,
        486.0: 0.0026236,
        487.0: 0.0027165,
        488.0: 0.0028142,
        489.0: 0.0029173,
        490.0: 0.0030263,
        491.0: 0.0031418,
        492.0: 0.003264,
        493.0: 0.0033928,
        494.0: 0.003528,
        495.0: 0.0036695,
        496.0: 0.0038168,
        497.0: 0.0039706,
        498.0: 0.0041327,
        499.0: 0.0043045,
        500.0: 0.0044878,
        501.0: 0.0046836,
        502.0: 0.0048904,
        503.0: 0.005106,
        504.0: 0.0053279,
        505.0: 0.0055539,
        506.0: 0.0057824,
        507.0: 0.0060137,
        508.0: 0.0062484,
        509.0: 0.0064873,
        510.0: 0.0067307,
        511.0: 0.0069786,
        512.0: 0.0072292,
        513.0: 0.0074806,
        514.0: 0.007731,
        515.0: 0.0079785,
        516.0: 0.0082225,
        517.0: 0.0084618,
        518.0: 0.0086938,
        519.0: 0.0089159,
        520.0: 0.0091254,
        521.0: 0.0093204,
        522.0: 0.0095018,
        523.0: 0.0096712,
        524.0: 0.0098304,
        525.0: 0.0099812,
        526.0: 0.0101242,
        527.0: 0.0102587,
        528.0: 0.0103843,
        529.0: 0.0105006,
        530.0: 0.0106074,
        531.0: 0.0107046,
        532.0: 0.0107925,
        533.0: 0.0108717,
        534.0: 0.0109425,
        535.0: 0.0110054,
        536.0: 0.0110606,
        537.0: 0.0111082,
        538.0: 0.011148,
        539.0: 0.0111802,
        540.0: 0.0112046,
        541.0: 0.0112213,
        542.0: 0.0112306,
        543.0: 0.0112326,
        544.0: 0.0112273,
        545.0: 0.0112149,
        546.0: 0.0111954,
        547.0: 0.011169,
        548.0: 0.0111362,
        549.0: 0.0110973,
        550.0: 0.0110527,
        551.0: 0.0110022,
        552.0: 0.0109459,
        553.0: 0.0108839,
        554.0: 0.0108161,
        555.0: 0.0107425,
        556.0: 0.0106629,
        557.0: 0.0105773,
        558.0: 0.0104855,
        559.0: 0.0103873,
        560.0: 0.0102827,
        561.0: 0.0101713,
        562.0: 0.0100537,
        563.0: 0.0099302,
        564.0: 0.0098011,
        565.0: 0.0096665,
        566.0: 0.0095268,
        567.0: 0.0093819,
        568.0: 0.009232,
        569.0: 0.0090771,
        570.0: 0.0089174,
        571.0: 0.0087528,
        572.0: 0.0085837,
        573.0: 0.0084104,
        574.0: 0.0082333,
        575.0: 0.0080525,
        576.0: 0.0078685,
        577.0: 0.0076814,
        578.0: 0.0074915,
        579.0: 0.0072987,
        580.0: 0.0071033,
        581.0: 0.0069055,
        582.0: 0.0067057,
        583.0: 0.0065044,
        584.0: 0.0063021,
        585.0: 0.0060993,
        586.0: 0.0058964,
        587.0: 0.0056937,
        588.0: 0.0054917,
        589.0: 0.0052906,
        590.0: 0.005091,
        591.0: 0.0048931,
        592.0: 0.0046974,
        593.0: 0.0045043,
        594.0: 0.0043144,
        595.0: 0.0041283,
        596.0: 0.0039465,
        597.0: 0.003769,
        598.0: 0.0035956,
        599.0: 0.0034261,
        600.0: 0.0032602,
        601.0: 0.0030979,
        602.0: 0.0029397,
        603.0: 0.0027858,
        604.0: 0.0026369,
        605.0: 0.0024933,
        606.0: 0.0023553,
        607.0: 0.0022229,
        608.0: 0.0020958,
        609.0: 0.0019739,
        610.0: 0.0018572,
        611.0: 0.0017455,
        612.0: 0.0016389,
        613.0: 0.0015372,
        614.0: 0.0014404,
        615.0: 0.0013484,
        616.0: 0.001261,
        617.0: 0.0011783,
        618.0: 0.0010998,
        619.0: 0.0010253,
        620.0: 0.0009547,
        621.0: 0.0008876,
        622.0: 0.0008241,
        623.0: 0.0007641,
        624.0: 0.0007075,
        625.0: 0.0006544,
        626.0: 0.0006045,
        627.0: 0.0005578,
        628.0: 0.0005141,
        629.0: 0.0004733,
        630.0: 0.0004351,
        631.0: 0.0003996,
        632.0: 0.0003666,
        633.0: 0.0003359,
        634.0: 0.0003074,
        635.0: 0.0002809,
        636.0: 0.0002562,
        637.0: 0.0002334,
        638.0: 0.0002123,
        639.0: 0.0001928,
        640.0: 0.0001747,
        641.0: 0.0001581,
        642.0: 0.0001428,
        643.0: 0.0001287,
        644.0: 0.0001159,
        645.0: 0.0001043,
        646.0: 9.38e-05,
        647.0: 8.43e-05,
        648.0: 7.57e-05,
        649.0: 6.8e-05,
        650.0: 6.1e-05,
        651.0: 5.46e-05,
        652.0: 4.88e-05,
        653.0: 4.36e-05,
        654.0: 3.89e-05,
        655.0: 3.46e-05,
        656.0: 3.08e-05,
        657.0: 2.74e-05,
        658.0: 2.43e-05,
        659.0: 2.16e-05,
        660.0: 1.92e-05,
        661.0: 1.7e-05,
        662.0: 1.52e-05,
        663.0: 1.35e-05,
        664.0: 1.21e-05,
        665.0: 1.07e-05,
        666.0: 9.5e-06,
        667.0: 8.4e-06,
        668.0: 7.5e-06,
        669.0: 6.6e-06,
        670.0: 5.8e-06,
        671.0: 5.1e-06,
        672.0: 4.5e-06,
        673.0: 4e-06,
        674.0: 3.5e-06,
        675.0: 3.1e-06,
        676.0: 2.7e-06,
        677.0: 2.3e-06,
        678.0: 2e-06,
        679.0: 1.7e-06,
        680.0: 1.5e-06,
        681.0: 1.2e-06,
        682.0: 1e-06,
        683.0: 8e-07,
        684.0: 7e-07,
        685.0: 5e-07,
        686.0: 4e-07,
        687.0: 3e-07,
        688.0: 3e-07,
        689.0: 2e-07,
        690.0: 2e-07,
        691.0: 1e-07,
        692.0: 1e-07,
        693.0: 1e-07,
        694.0: 1e-07,
        695.0: 0.0,
        696.0: 0.0,
        697.0: 0.0,
        698.0: 0.0,
        699.0: 0.0,
        700.0: 0.0,
        701.0: 0.0,
        702.0: 0.0,
        703.0: 0.0,
        704.0: 0.0,
        705.0: 0.0,
        706.0: 0.0,
        707.0: 0.0,
        708.0: 0.0,
        709.0: 0.0,
        710.0: 0.0,
        711.0: 0.0,
        712.0: 0.0,
        713.0: 0.0,
        714.0: 0.0,
        715.0: 0.0,
        716.0: 0.0,
        717.0: 0.0,
        718.0: 0.0,
        719.0: 0.0,
        720.0: 0.0,
        721.0: 0.0,
        722.0: 0.0,
        723.0: 0.0,
        724.0: 0.0,
        725.0: 0.0,
        726.0: 0.0,
        727.0: 0.0,
        728.0: 0.0,
        729.0: 0.0,
        730.0: 0.0,
        731.0: 0.0,
        732.0: 0.0,
        733.0: 0.0,
        734.0: 0.0,
        735.0: 0.0,
        736.0: 0.0,
        737.0: 0.0,
        738.0: 0.0,
        739.0: 0.0,
        740.0: 0.0,
        741.0: 0.0,
        742.0: 0.0,
        743.0: 0.0,
        744.0: 0.0,
        745.0: 0.0,
        746.0: 0.0,
        747.0: 0.0,
        748.0: 0.0,
        749.0: 0.0,
        750.0: 0.0,
        751.0: 0.0,
        752.0: 0.0,
        753.0: 0.0,
        754.0: 0.0,
        755.0: 0.0,
        756.0: 0.0,
        757.0: 0.0,
        758.0: 0.0,
        759.0: 0.0,
        760.0: 0.0,
        761.0: 0.0,
        762.0: 0.0,
        763.0: 0.0,
        764.0: 0.0,
        765.0: 0.0,
        766.0: 0.0,
        767.0: 0.0,
        768.0: 0.0,
        769.0: 0.0,
        770.0: 0.0,
        771.0: 0.0,
        772.0: 0.0,
        773.0: 0.0,
        774.0: 0.0,
        775.0: 0.0,
        776.0: 0.0,
        777.0: 0.0,
        778.0: 0.0,
        779.0: 0.0,
        780.0: 0.0,
        781.0: 0.0,
        782.0: 0.0,
        783.0: 0.0,
        784.0: 0.0,
        785.0: 0.0,
        786.0: 0.0,
        787.0: 0.0,
        788.0: 0.0,
        789.0: 0.0,
        790.0: 0.0,
        791.0: 0.0,
        792.0: 0.0,
        793.0: 0.0,
        794.0: 0.0,
        795.0: 0.0,
        796.0: 0.0,
        797.0: 0.0,
        798.0: 0.0,
        799.0: 0.0,
        800.0: 0.0,
        801.0: 0.0,
        802.0: 0.0,
        803.0: 0.0,
        804.0: 0.0,
        805.0: 0.0,
        806.0: 0.0,
        807.0: 0.0,
        808.0: 0.0,
        809.0: 0.0,
        810.0: 0.0,
        811.0: 0.0,
        812.0: 0.0,
        813.0: 0.0,
        814.0: 0.0,
        815.0: 0.0,
        816.0: 0.0,
        817.0: 0.0,
        818.0: 0.0,
        819.0: 0.0,
        820.0: 0.0,
        821.0: 0.0,
        822.0: 0.0,
        823.0: 0.0,
        824.0: 0.0,
        825.0: 0.0,
        826.0: 0.0,
        827.0: 0.0,
        828.0: 0.0,
        829.0: 0.0,
        830.0: 0.0},
    'b_bar': {
        360.0: 5.7e-06,
        361.0: 6.4e-06,
        362.0: 7.2e-06,
        363.0: 8e-06,
        364.0: 9e-06,
        365.0: 1.02e-05,
        366.0: 1.14e-05,
        367.0: 1.28e-05,
        368.0: 1.44e-05,
        369.0: 1.62e-05,
        370.0: 1.82e-05,
        371.0: 2.04e-05,
        372.0: 2.28e-05,
        373.0: 2.56e-05,
        374.0: 2.88e-05,
        375.0: 3.26e-05,
        376.0: 3.72e-05,
        377.0: 4.25e-05,
        378.0: 4.83e-05,
        379.0: 5.43e-05,
        380.0: 6.03e-05,
        381.0: 6.63e-05,
        382.0: 7.25e-05,
        383.0: 7.95e-05,
        384.0: 8.81e-05,
        385.0: 9.87e-05,
        386.0: 0.0001119,
        387.0: 0.0001278,
        388.0: 0.0001458,
        389.0: 0.0001659,
        390.0: 0.0001876,
        391.0: 0.0002106,
        392.0: 0.0002358,
        393.0: 0.0002646,
        394.0: 0.0002984,
        395.0: 0.0003388,
        396.0: 0.0003877,
        397.0: 0.0004444,
        398.0: 0.0005063,
        399.0: 0.0005706,
        400.0: 0.0006348,
        401.0: 0.0006968,
        402.0: 0.0007612,
        403.0: 0.0008341,
        404.0: 0.0009219,
        405.0: 0.0010309,
        406.0: 0.0011658,
        407.0: 0.0013256,
        408.0: 0.001509,
        409.0: 0.0017144,
        410.0: 0.0019403,
        411.0: 0.0021862,
        412.0: 0.0024568,
        413.0: 0.0027577,
        414.0: 0.0030947,
        415.0: 0.0034736,
        416.0: 0.0038937,
        417.0: 0.0043545,
        418.0: 0.0048619,
        419.0: 0.0054216,
        420.0: 0.0060397,
        421.0: 0.0067216,
        422.0: 0.0074534,
        423.0: 0.0082124,
        424.0: 0.0089758,
        425.0: 0.0097205,
        426.0: 0.0104345,
        427.0: 0.0111186,
        428.0: 0.01177,
        429.0: 0.0123856,
        430.0: 0.0129626,
        431.0: 0.0134962,
        432.0: 0.0139842,
        433.0: 0.0144275,
        434.0: 0.0148269,
        435.0: 0.0151831,
        436.0: 0.015496,
        437.0: 0.0157663,
        438.0: 0.0159962,
        439.0: 0.0161881,
        440.0: 0.0163441,
        441.0: 0.0164656,
        442.0: 0.0165552,
        443.0: 0.0166173,
        444.0: 0.0166563,
        445.0: 0.0166766,
        446.0: 0.0166801,
        447.0: 0.0166682,
        448.0: 0.0166448,
        449.0: 0.0166136,
        450.0: 0.0165785,
        451.0: 0.0165424,
        452.0: 0.016503,
        453.0: 0.0164553,
        454.0: 0.0163947,
        455.0: 0.0163164,
        456.0: 0.0162178,
        457.0: 0.016099,
        458.0: 0.0159594,
        459.0: 0.0157985,
        460.0: 0.0156157,
        461.0: 0.015413,
        462.0: 0.0151874,
        463.0: 0.0149311,
        464.0: 0.0146365,
        465.0: 0.0142957,
        466.0: 0.0139029,
        467.0: 0.013467,
        468.0: 0.0130026,
        469.0: 0.0125242,
        470.0: 0.0120461,
        471.0: 0.0115764,
        472.0: 0.0111124,
        473.0: 0.0106534,
        474.0: 0.0101986,
        475.0: 0.0097472,
        476.0: 0.0093009,
        477.0: 0.0088626,
        478.0: 0.0084333,
        479.0: 0.0080139,
        480.0: 0.0076053,
        481.0: 0.0072084,
        482.0: 0.0068241,
        483.0: 0.0064543,
        484.0: 0.0061006,
        485.0: 0.0057647,
        486.0: 0.0054478,
        487.0: 0.0051493,
        488.0: 0.0048679,
        489.0: 0.0046025,
        490.0: 0.0043519,
        491.0: 0.0041156,
        492.0: 0.0038935,
        493.0: 0.0036849,
        494.0: 0.003489,
        495.0: 0.0033052,
        496.0: 0.0031327,
        497.0: 0.0029708,
        498.0: 0.0028191,
        499.0: 0.0026772,
        500.0: 0.0025446,
        501.0: 0.0024213,
        502.0: 0.0023059,
        503.0: 0.0021963,
        504.0: 0.0020905,
        505.0: 0.0019861,
        506.0: 0.001882,
        507.0: 0.0017786,
        508.0: 0.0016767,
        509.0: 0.0015769,
        510.0: 0.00148,
        511.0: 0.0013859,
        512.0: 0.0012945,
        513.0: 0.0012068,
        514.0: 0.0011233,
        515.0: 0.001045,
        516.0: 0.0009721,
        517.0: 0.0009043,
        518.0: 0.0008418,
        519.0: 0.0007844,
        520.0: 0.000732,
        521.0: 0.0006849,
        522.0: 0.0006425,
        523.0: 0.000604,
        524.0: 0.0005687,
        525.0: 0.0005356,
        526.0: 0.0005043,
        527.0: 0.0004747,
        528.0: 0.0004467,
        529.0: 0.00042,
        530.0: 0.0003944,
        531.0: 0.0003696,
        532.0: 0.0003455,
        533.0: 0.0003224,
        534.0: 0.0003002,
        535.0: 0.0002792,
        536.0: 0.0002592,
        537.0: 0.0002404,
        538.0: 0.0002225,
        539.0: 0.0002057,
        540.0: 0.0001899,
        541.0: 0.0001751,
        542.0: 0.0001613,
        543.0: 0.0001484,
        544.0: 0.0001364,
        545.0: 0.0001254,
        546.0: 0.0001151,
        547.0: 0.0001057,
        548.0: 9.71e-05,
        549.0: 8.91e-05,
        550.0: 8.19e-05,
        551.0: 7.52e-05,
        552.0: 6.91e-05,
        553.0: 6.35e-05,
        554.0: 5.84e-05,
        555.0: 5.38e-05,
        556.0: 4.96e-05,
        557.0: 4.58e-05,
        558.0: 4.24e-05,
        559.0: 3.93e-05,
        560.0: 3.65e-05,
        561.0: 3.39e-05,
        562.0: 3.15e-05,
        563.0: 2.94e-05,
        564.0: 2.75e-05,
        565.0: 2.57e-05,
        566.0: 2.42e-05,
        567.0: 2.28e-05,
        568.0: 2.16e-05,
        569.0: 2.06e-05,
        570.0: 1.96e-05,
        571.0: 1.89e-05,
        572.0: 1.82e-05,
        573.0: 1.77e-05,
        574.0: 1.72e-05,
        575.0: 1.68e-05,
        576.0: 1.65e-05,
        577.0: 1.63e-05,
        578.0: 1.6e-05,
        579.0: 1.57e-05,
        580.0: 1.54e-05,
        581.0: 1.51e-05,
        582.0: 1.46e-05,
        583.0: 1.42e-05,
        584.0: 1.36e-05,
        585.0: 1.31e-05,
        586.0: 1.25e-05,
        587.0: 1.19e-05,
        588.0: 1.13e-05,
        589.0: 1.07e-05,
        590.0: 1.03e-05,
        591.0: 1e-05,
        592.0: 9.8e-06,
        593.0: 9.7e-06,
        594.0: 9.6e-06,
        595.0: 9.4e-06,
        596.0: 9.1e-06,
        597.0: 8.7e-06,
        598.0: 8.3e-06,
        599.0: 7.9e-06,
        600.0: 7.5e-06,
        601.0: 7.1e-06,
        602.0: 6.8e-06,
        603.0: 6.4e-06,
        604.0: 6e-06,
        605.0: 5.6e-06,
        606.0: 5.1e-06,
        607.0: 4.6e-06,
        608.0: 4.1e-06,
        609.0: 3.6e-06,
        610.0: 3.2e-06,
        611.0: 2.9e-06,
        612.0: 2.6e-06,
        613.0: 2.5e-06,
        614.0: 2.4e-06,
        615.0: 2.2e-06,
        616.0: 2.1e-06,
        617.0: 2.1e-06,
        618.0: 2e-06,
        619.0: 1.9e-06,
        620.0: 1.8e-06,
        621.0: 1.6e-06,
        622.0: 1.5e-06,
        623.0: 1.3e-06,
        624.0: 1.1e-06,
        625.0: 9e-07,
        626.0: 8e-07,
        627.0: 7e-07,
        628.0: 6e-07,
        629.0: 5e-07,
        630.0: 5e-07,
        631.0: 4e-07,
        632.0: 4e-07,
        633.0: 3e-07,
        634.0: 3e-07,
        635.0: 3e-07,
        636.0: 3e-07,
        637.0: 2e-07,
        638.0: 2e-07,
        639.0: 2e-07,
        640.0: 2e-07,
        641.0: 2e-07,
        642.0: 2e-07,
        643.0: 1e-07,
        644.0: 1e-07,
        645.0: 1e-07,
        646.0: 1e-07,
        647.0: 1e-07,
        648.0: 0.0,
        649.0: 0.0,
        650.0: 0.0,
        651.0: 0.0,
        652.0: 0.0,
        653.0: 0.0,
        654.0: 0.0,
        655.0: 0.0,
        656.0: 0.0,
        657.0: 0.0,
        658.0: 0.0,
        659.0: 0.0,
        660.0: 0.0,
        661.0: 0.0,
        662.0: 0.0,
        663.0: 0.0,
        664.0: 0.0,
        665.0: 0.0,
        666.0: 0.0,
        667.0: 0.0,
        668.0: 0.0,
        669.0: 0.0,
        670.0: 0.0,
        671.0: 0.0,
        672.0: 0.0,
        673.0: 0.0,
        674.0: 0.0,
        675.0: 0.0,
        676.0: 0.0,
        677.0: 0.0,
        678.0: 0.0,
        679.0: 0.0,
        680.0: 0.0,
        681.0: 0.0,
        682.0: 0.0,
        683.0: 0.0,
        684.0: 0.0,
        685.0: 0.0,
        686.0: 0.0,
        687.0: 0.0,
        688.0: 0.0,
        689.0: 0.0,
        690.0: 0.0,
        691.0: 0.0,
        692.0: 0.0,
        693.0: 0.0,
        694.0: 0.0,
        695.0: 0.0,
        696.0: 0.0,
        697.0: 0.0,
        698.0: 0.0,
        699.0: 0.0,
        700.0: 0.0,
        701.0: 0.0,
        702.0: 0.0,
        703.0: 0.0,
        704.0: 0.0,
        705.0: 0.0,
        706.0: 0.0,
        707.0: 0.0,
        708.0: 0.0,
        709.0: 0.0,
        710.0: 0.0,
        711.0: 0.0,
        712.0: 0.0,
        713.0: 0.0,
        714.0: 0.0,
        715.0: 0.0,
        716.0: 0.0,
        717.0: 0.0,
        718.0: 0.0,
        719.0: 0.0,
        720.0: 0.0,
        721.0: 0.0,
        722.0: 0.0,
        723.0: 0.0,
        724.0: 0.0,
        725.0: 0.0,
        726.0: 0.0,
        727.0: 0.0,
        728.0: 0.0,
        729.0: 0.0,
        730.0: 0.0,
        731.0: 0.0,
        732.0: 0.0,
        733.0: 0.0,
        734.0: 0.0,
        735.0: 0.0,
        736.0: 0.0,
        737.0: 0.0,
        738.0: 0.0,
        739.0: 0.0,
        740.0: 0.0,
        741.0: 0.0,
        742.0: 0.0,
        743.0: 0.0,
        744.0: 0.0,
        745.0: 0.0,
        746.0: 0.0,
        747.0: 0.0,
        748.0: 0.0,
        749.0: 0.0,
        750.0: 0.0,
        751.0: 0.0,
        752.0: 0.0,
        753.0: 0.0,
        754.0: 0.0,
        755.0: 0.0,
        756.0: 0.0,
        757.0: 0.0,
        758.0: 0.0,
        759.0: 0.0,
        760.0: 0.0,
        761.0: 0.0,
        762.0: 0.0,
        763.0: 0.0,
        764.0: 0.0,
        765.0: 0.0,
        766.0: 0.0,
        767.0: 0.0,
        768.0: 0.0,
        769.0: 0.0,
        770.0: 0.0,
        771.0: 0.0,
        772.0: 0.0,
        773.0: 0.0,
        774.0: 0.0,
        775.0: 0.0,
        776.0: 0.0,
        777.0: 0.0,
        778.0: 0.0,
        779.0: 0.0,
        780.0: 0.0,
        781.0: 0.0,
        782.0: 0.0,
        783.0: 0.0,
        784.0: 0.0,
        785.0: 0.0,
        786.0: 0.0,
        787.0: 0.0,
        788.0: 0.0,
        789.0: 0.0,
        790.0: 0.0,
        791.0: 0.0,
        792.0: 0.0,
        793.0: 0.0,
        794.0: 0.0,
        795.0: 0.0,
        796.0: 0.0,
        797.0: 0.0,
        798.0: 0.0,
        799.0: 0.0,
        800.0: 0.0,
        801.0: 0.0,
        802.0: 0.0,
        803.0: 0.0,
        804.0: 0.0,
        805.0: 0.0,
        806.0: 0.0,
        807.0: 0.0,
        808.0: 0.0,
        809.0: 0.0,
        810.0: 0.0,
        811.0: 0.0,
        812.0: 0.0,
        813.0: 0.0,
        814.0: 0.0,
        815.0: 0.0,
        816.0: 0.0,
        817.0: 0.0,
        818.0: 0.0,
        819.0: 0.0,
        820.0: 0.0,
        821.0: 0.0,
        822.0: 0.0,
        823.0: 0.0,
        824.0: 0.0,
        825.0: 0.0,
        826.0: 0.0,
        827.0: 0.0,
        828.0: 0.0,
        829.0: 0.0,
        830.0: 0.0}}

ACES_RICD = RGB_ColourMatchingFunctions('ACES RICD', ACES_RICD_DATA)
"""
*ACES Reference Input Capture Device* spectral sensitivities.

ACES_RICD : RGB_ColourMatchingFunctions
"""