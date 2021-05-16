class DataWrangler:

    def data_correcting(data_):
        """ In dataset some values for fixed acidity, volatile acidity,
        citric acid, residual sugar, chlorides, pH, sulphates are missing.
        Solve this problem by filling null values with mean values of train dataframe.
         irst of all we need to change text values of wine type to the 0 and 1.
        Then we need to get train data and Fill Nan values by this data mean."""

        data_["type"].replace({"red": 0, "white": 1}, inplace=True)  # "RED": 0, "WHITE": 1
        data_.fillna(data_.mean(axis=0), inplace=True)

        return data_

    def oversampling_data(data_):
        """ Share of white wines is 75%. So we deside to oversampling data with random choosen red wine data.
        As in the future we can have other share of white and red wines, we get this solution for all possible cases. """

        red_count = data_.loc[data_['type'] == 0].count()[0]
        print(f"red_count: {red_count}")
        white_count = data_.loc[data_['type'] == 1].count()[0]
        print(f"white_count: {white_count}")
        if white_count > red_count:
            for i in range((white_count - red_count)):
                df1 = data_.loc[data_['type'] == 0].sample()
                data_ = data_.append(df1)
        else:
            for i in range((red_count - white_count)):
                df1 = data_.loc[df['type'] == 1].sample()
                data_ = data_.append(df1)

        """ Now combining fixed acidity, volatile acidity and citric acid into one variable total_acidity
        and our target variable into two classes: low quality-->0 (3, 4, 5)  and high quality-->1 (6,7,8,9)"""

        data_["total_acidity"] = data_['fixed acidity'] + data_['volatile acidity'] + data_['citric acid']
        quaity_mapping = {3: 0, 4: 0, 5: 0, 6: 1, 7: 1, 8: 1, 9: 1}
        data_["quality"] = data_["quality"].map(quaity_mapping)

        """You can check that it works by this
        dups_color = df.pivot_table(index=['type'], aggfunc='size')
        dups_color
        Now we have 4898 of red and 4898 of white wines data """

        return data_

    def lst_of_dataframes(df):

        """ list of dataframe_1 and dataframe_2 """

        df_list = [df]
        for i in range(len(df_list)):
            df_ = df_list[i]
            df_final = df_[["total_acidity", "chlorides", "pH", "sulphates", "alcohol", "quality"]]
            df_list[i] = df_final

        return df_list[0]


if __name__ == "__main__":
    main = DataWrangler()