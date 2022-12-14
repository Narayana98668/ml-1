"from sklearn.model_selection import train_test_split\n",
"from sklearn.neighbors import KNeighborsClassifier\n",
"\n",
"X=[(1,0),(2,0),(3,0),(6,0),(6,0),(7,0),(10,0),(11,0)]\n",
"y=[\"dot\",\"dot\",\"cross\",\"cross\",\"cross\",\"dot\",\"dot\",\"dot\"]\n",
"# dividing into two equal parts\n",
"X_train,X_test,y_train,y_test = train_test_split(X, y,test_size=0.5,random_state=2)  \n",
"\n",
"knn = KNeighborsClassifier(n_neighbors=3) # given 3 as neigbours in the questioin 10\n",
"\n",
"knn.fit(X_train,y_train)\n",
"\n",
"predict = knn.predict(X_test)\n",
"\n",
"print(\"--Predicted--\")\n",
"for i,j in zip(X_test,predict):\n",
"  print(i,\":\",j)\n",
"\n",
"from sklearn.metrics import accuracy_score\n",
"from sklearn.metrics import classification_report\n",
"from sklearn.metrics import confusion_matrix\n",
"\n",
"print(\"\\nAccuracy=\",accuracy_score(y_test,predict))\n",
"\n",
"print(\"\\nConfusison Matrix =\\n\",confusion_matrix(y_test,predict))\n",
"\n",
"tn, fp, fn, tp = confusion_matrix(y_test, predict).ravel()\n",
"specificity = tn / (tn+fp)\n",
"print(\"\\nspecificity=\",specificity)\n",
"\n",
"sensitivity=tp/(tp+fn)\n",
"print(\"\\nsensitivity\",sensitivity)"