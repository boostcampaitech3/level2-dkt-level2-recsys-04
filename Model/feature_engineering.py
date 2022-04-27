import pandas as pd


class FeatureEngineering:
    """
    This is base feature engineering class

    You must implement __preprocessing__ method.

    Do any feature engineering you want and be sure to return the completed dataframe.
    
    Example)
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
    """
    def __init__(self):
        self.tmp = None

    def __call__(self, *args, **kwargs):
        """
        class call method
        :param args: (None)
        :param kwargs: (None)
        :return: (pandas.dataframe) feature engineering dataframe
        """
        return self.__preprocessing__()

    def __preprocessing__(self):
        """
        Make feature engineering part
        You must implement this part
        :return: (pandas.dataframe) feature engineering dataframe
        """
        raise NotImplementedError


class FeatExample(FeatureEngineering):
    def __init__(self, df):
        super(FeatExample, self).__init__()
        self.df = df

    def __preprocessing__(self):
        self.df.sort_values(by=["userID", "Timestamp"], inplace=True)

        self.df["user_correct_answer"] = self.df.groupby("userID")["answerCode"].transform(lambda x: x.cumsum().shift(1))
        self.df["user_total_answer"] = self.df.groupby("userID")["answerCode"].cumcount()
        self.df["user_acc"] = self.df["user_correct_answer"] / self.df["user_total_answer"]

        # make your feature
        self.df["test_L"] = self.df["assessmentItemID"].apply(lambda x: int(x[2]))
        self.df["test_M"] = self.df["assessmentItemID"].apply(lambda x: int(x[4:7]))
        self.df["test_S"] = self.df["assessmentItemID"].apply(lambda x: int(x[-3:]))
        self.df["month"] = self.df["Timestamp"].dt.month
        self.df["hour"] = self.df["Timestamp"].dt.hour

        correct_t = self.df.groupby(["testId"])["answerCode"].agg(["mean", "sum"])
        correct_t.columns = ["test_mean", "test_sum"]
        correct_k = self.df.groupby(["KnowledgeTag"])["answerCode"].agg(["mean", "sum"])
        correct_k.columns = ["tag_mean", "tag_sum"]

        self.df = pd.merge(self.df, correct_t, on=["testId"], how="left")
        self.df = pd.merge(self.df, correct_k, on=["KnowledgeTag"], how="left")

        return self.df
