# Model Usage Documents

## Contents

- [feature_engineering class](#feature_engineering)

---

## feature_engineering

- `feature_engineering` class is a class that creates a dataframe composed of new feature combinations.
- You **must implement `__preprocessing__`** method. If not implement, class raise the `NotImplementedError`
- `__preprocessing__` method must return the dataframe type

### Example

```python
import pandas as pd
from feature_engineering import FeatureEngineering

class MyFE(FeatureEngineering):
    def __init__(self, df):
        self.df = df

    def __preprocessing__(self):
        self.df["new_feature1"] = self.df["old_feature"] + 1

        return self.df

df = pd.DataFrame(data={
    "old_feature": [1, 2, 3]
})

fe = MyFE(df)
new_df = fe() # just object call, return the new dataframe
```