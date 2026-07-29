import numpy as np
import pandas as pd

arr = np.array([1, 2, 3, 4, 5])

print("NumPy Version:", np.__version__)
print("Array:", arr)

df = pd.DataFrame({
    "Name": ["Yogesh", "Aman"],
    "Marks": [95, 89]
})

print(df)