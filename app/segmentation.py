from django.http import JsonResponse
from sklearn.tree import DecisionTreeRegressor
from sklearn.cluster import KMeans

def segmentation(request):
    if request.method == 'POST':
        jsonDf = request.POST.get('jsonDf')
        df = pd.read_json(StringIO(jsonDf))
        main_col = request.POST.get('main_col')
        index_col = request.POST.get('index_col')
        
        features = [col for col in df.columns if col not in [index_col, main_col]]
        estimator = DecisionTreeRegressor().fit(df[features], df[main_col])
        feature_importance = {feature: importance for feature, importance in zip(features, estimator.feature_importances_)}
        
        kmeans = KMeans(n_clusters=4)
        df['cluster'] = kmeans.fit_predict(df[features])
        
        return JsonResponse({'feature_importance': feature_importance, 'clusters': df['cluster'].tolist()})
    return render(request, 'segmentation.html')
