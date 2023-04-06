import numpy as np

#  F[GHz]
f = np.array(
    [118.7503, 56.2648, 62.4863, 58.4466, 60.3061, 59.591, 59.1642, 60.4348, 58.3239, 61.1506, 57.6125, 61.8002,
     56.9682, 62.4112, 56.3634, 62.998, 55.7838, 63.5685, 55.2214, 64.1278, 54.6712, 64.6789, 54.13, 65.2241, 53.5958,
     65.7648, 53.0669, 66.3021, 52.5424, 66.8368, 52.0214, 67.3696, 51.5034, 67.9009, 50.9877, 68.431, 50.4742, 68.9603,
     233.9461, 368.4982, 401.7398, 424.763, 487.2493, 566.8956, 715.3929, 731.1866, 773.8395, 834.1455, 895.071])
#  S(T_0)[Hz*cm2]
s300 = np.array(
    [2.906e-15, 7.957e-16, 2.444e-15, 2.194e-15, 3.301e-15, 3.243e-15, 3.664e-15, 3.834e-15, 3.588e-15, 3.947e-15,
     3.179e-15, 3.661e-15, 2.59e-15, 3.111e-15, 1.954e-15, 2.443e-15, 1.373e-15, 1.784e-15, 9.013e-16, 1.217e-15,
     5.545e-16, 7.766e-16, 3.201e-16, 4.651e-16, 1.738e-16, 2.619e-16, 8.88e-17, 1.387e-16, 4.272e-17, 6.923e-17,
     1.939e-17, 3.255e-17, 8.301e-18, 1.445e-17, 3.356e-18, 6.049e-18, 1.28e-18, 2.394e-18, 3.287e-17, 6.463e-16,
     1.334e-17, 7.049e-15, 3.011e-15, 1.797e-17, 1.826e-15, 2.193e-17, 1.153e-14, 3.974e-15, 2.512e-17])
#  (Elow+hf)/kT_0 [unitless]
be = np.array(
    [0.01, 0.014, 0.083, 0.083, 0.207, 0.207, 0.387, 0.387, 0.621, 0.621, 0.91, 0.91, 1.255, 1.255, 1.654, 1.654, 2.109,
     2.109, 2.618, 2.618, 3.182, 3.182, 3.8, 3.8, 4.474, 4.474, 5.201, 5.201, 5.983, 5.983, 6.819, 6.819, 7.709, 7.709,
     8.653, 8.653, 9.651, 9.651, 0.019, 0.048, 0.045, 0.044, 0.049, 0.084, 0.145, 0.136, 0.141, 0.145, 0.201])
#  gamma(T_0) [MHZ/mb == GHz/bar]
wb300 = 0.56
x = 0.8
w300 = np.array(
    [1.688, 1.703, 1.513, 1.491, 1.415, 1.408, 1.353, 1.339, 1.295, 1.292, 1.262, 1.263, 1.223, 1.217, 1.189, 1.174,
     1.134, 1.134, 1.089, 1.088, 1.037, 1.038, 0.996, 0.996, 0.955, 0.955, 0.906, 0.906, 0.858, 0.858, 0.811, 0.811,
     0.764, 0.764, 0.717, 0.717, 0.669, 0.669, 1.65, 1.64, 1.64, 1.64, 1.6, 1.6, 1.6, 1.6, 1.62, 1.47, 1.47])
# y(t_0) [unitless]
y300 = np.append(
    [-0.036, 0.2547, -0.3655, 0.5495, -0.5696, 0.6181, -0.4252, 0.3517, -0.1496, 0.043, 0.064, -0.1605, 0.2906,
     -0.373, 0.4169, -0.4819, 0.4963, -0.5481, 0.5512, -0.5931, 0.6212, -0.6558, 0.692, -0.7208, 0.7312, -0.755,
     0.7555, -0.7751, 0.7914, -0.8073, 0.8307, -0.8431, 0.8676, -0.8761, 0.9046, -0.9092, 0.9416, -0.9423],
    np.tile(0.0, (1, 11)))
# v(t_0) [unitless]
v = np.append(
    [0.0079, -0.0978, 0.0844, -0.1273, 0.0699, -0.0776, 0.2309, -0.2825, 0.0436, -0.0584, 0.6056, -0.6619, 0.6451,
     -0.6759, 0.6547, -0.6675, 0.6135, -0.6139, 0.2952, -0.2895, 0.2654, -0.259, 0.375, -0.368, 0.5085, -0.5002,
     0.6206, -0.6091, 0.6526, -0.6393, 0.664, -0.6475, 0.6729, -0.6545, 0.68, -0.66, 0.685, -0.665],
    np.tile(0.0, (1, 11)))
# 2016/11/30 *********************************************************
