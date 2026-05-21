from itertools import combinations

total_features = ["n", "p", "k", "ph", "ec"]
static_features = []

def feature_combination(total_features, static_features, combination_size):
    if combination_size > len(total_features):
        raise ValueError("Combination size cannot be greater than the total number of features.")
    if combination_size is None:
        combination_size = len(total_features)
    if static_features is not None:
        dynamic_features = [feature for feature in total_features if feature not in static_features]
    else:
        dynamic_features = total_features
    
    combination_size =  combination_size - len(static_features)
    
    comb = list(combinations(dynamic_features, combination_size))
    
    for i in range(len(comb)):
        comb[i] = list(comb[i]) + static_features
    
    return comb

comb = feature_combination(total_features=total_features, static_features=static_features, combination_size=3)

print(comb)
       