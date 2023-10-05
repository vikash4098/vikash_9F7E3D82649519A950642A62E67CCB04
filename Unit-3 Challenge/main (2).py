def linear_search_product(products, target):
  indices = []
  for i in range(len(products)):
    if products[i] == target:
      indices.append(i)
  return indices


products = ["shoes", "boot", "loafer", "shoes", "sandal", "shoes"]
target = "shoes"
result = linear_search_product(products, target)
print(result)
