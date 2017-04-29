X_train = [];
Y_train = [];
X_test = [];
Y_test = [];
for i = 1:8
    l = 4000; % size(X{i},1);
    X_train = [X_train; datasample(X{i}, floor(0.8*l))];
    Y_train = [Y_train; repmat([i], floor(0.8*l), 1)];
    X_test = [X_test; datasample(X{i}, floor(0.2*l))];
    Y_test = [Y_test; repmat([i], floor(0.2*l), 1)];
end

model = fitcecoc(X_train,Y_train);
label = predict(model,X_test);
accuracy = sum(label == Y_test) / length(Y_test);
disp(accuracy);
