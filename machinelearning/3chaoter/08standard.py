from sklearn.preprocessing import StandardScaler

X = [[2,1],[3,1],[1, 4], [2,6]]

scaler = StandardScaler()

x_scaled = scaler.fit_transform(X)

print(x_scaled)




