import numpy as np

X = np.array([[0.20254159, 0.14335428],
              [0.93962017, 0.29357231],
              [0.49345428, 0.66472471],
              [0.1059487 , 0.28996985],
              [0.93080426, 0.98414732],
              [0.40833746, 0.37462837],
              [0.81710841, 0.92314003],
              [0.52580199, 0.54352896],
              [0.71293764, 0.2760392 ],
              [0.51775029, 0.46275193],
              [0.4772603 , 0.69384608],
              [0.4709946 , 0.2758965 ]])

Y = np.array([0.26434052,0.0010701,0.97343155,0.88110122,0.92970109,0.0223773,0.82652964,0.77435743,0.21022685,0.18160785,0.81438324,0.68551095])

L = 0.29764259048756436



def closed_form(X, Y, lambda_factor):
    identity_matrix = np.identity(X.shape[1])
    theta_calculation = np.linalg.inv(X.transpose().dot(X) + (L * identity_matrix)).dot(X.transpose()).dot(Y)
    return theta_calculation

theta = closed_form(X, Y, L)
print(theta)

# Submission output: [-0.03521336  1.00961557]
