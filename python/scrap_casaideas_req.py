import requests

# no resulta porque se intenta scrapear la memoria del frontend 
# 200 OK (from service worker) dice que no es servidor real, endpoint no existe publicamente

headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Mobile Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.casaideas.cl/"
}

productos = []

#url = "https://ecom-be.casaideas.cl/graphql?query=query%20productSearch(%24search%3AString!%24pageSize%3AInt%3D10%24currentPage%3AInt%3D0%24sort%3AProductAttributeSortInput%3D%7B%7D)%7BproductSearch(phrase%3A%24search%20page_size%3A%24pageSize%20current_page%3A%24currentPage%20sort%3A%24sort)%7B__typename%20aggregations%7Battribute_code%20label%20options%7Blabel%20value%20count%7D%7Dsort_fields%7Bdefault%20options%7Blabel%20value%20__typename%7D%7Ditems%7B__typename%20name%20sku%20canonical_url%20price_range%7B__typename%20minimum_price%7B__typename%20regular_price%7B__typename%20value%20currency%7Dfinal_price%7B__typename%20value%20currency%7Ddiscount%7B__typename%20amount_off%7D%7Dmaximum_price%7B__typename%20regular_price%7B__typename%20value%20currency%7Dfinal_price%7B__typename%20value%20currency%7Ddiscount%7B__typename%20amount_off%7D%7D%7Dsmall_image%7B__typename%20url%7D%7Dpage_info%7B__typename%20total_pages%20current_page%7Dtotal_count%7D%7D&operationName=productSearch&variables=%7B%22currentPage%22%3A1%2C%22pageSize%22%3A12%2C%22search%22%3A%22maceteros%22%2C%22sort%22%3A%7B%7D%7D"
url= "https://ecom-be.casaideas.cl/graphql?query=query%20productSearch(%24search%3AString!%24pageSize%3AInt%3D10%24currentPage%3AInt%3D0%24sort%3AProductAttributeSortInput%3D%7B%7D)%7BproductSearch(phrase%3A%24search%20page_size%3A%24pageSize%20current_page%3A%24currentPage%20sort%3A%24sort)%7B__typename%20aggregations%7Battribute_code%20label%20options%7Blabel%20value%20count%7D%7Dsort_fields%7Bdefault%20options%7Blabel%20value%20__typename%7D%7Ditems%7B__typename%20name%20sku%20canonical_url%20price_range%7B__typename%20minimum_price%7B__typename%20regular_price%7B__typename%20value%20currency%7Dfinal_price%7B__typename%20value%20currency%7Ddiscount%7B__typename%20amount_off%7D%7Dmaximum_price%7B__typename%20regular_price%7B__typename%20value%20currency%7Dfinal_price%7B__typename%20value%20currency%7Ddiscount%7B__typename%20amount_off%7D%7D%7Dsmall_image%7B__typename%20url%7D%7Dpage_info%7B__typename%20total_pages%20current_page%7Dtotal_count%7D%7D&operationName=productSearch&variables=%7B%22currentPage%22%3A2%2C%22pageSize%22%3A12%2C%22search%22%3A%22maceteros%22%2C%22sort%22%3A%7B%7D%7D" 
r = requests.get(url, headers= headers)

print(r.status_code)
print(type(r))