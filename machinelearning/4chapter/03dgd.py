from  sklearn.linear_model import SGDRegressor

X = [[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]]
y = [55, 65, 70, 75, 85, 50, 60, 72, 80, 58]

model = SGDRegressor(
    loss="squared_error",
    max_iter=10000,
    eta0=0.1,
    learning_rate="constant",
    tol=1e-8,
)


model.fit(X, y)
print(model.coef_)
print(model.intercept_)



