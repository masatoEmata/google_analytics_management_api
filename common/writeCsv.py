#https://expenblog.com/4138.html
#https://note.nkmk.me/python-pandas-to-csv/

import locale
import pandas as pd

class WriteCsv:
    def write(data, file_name):
        encoding = locale.getpreferredencoding()
        df = pd.DataFrame(data)
#        df.to_csv(file_name, encoding = encoding, mode="w")
        df.to_csv(file_name, encoding = encoding, mode="a", header=False)

if __name__ == "__main__":
    sample_file_name = "sample.csv"
    sample_data = {'id': '192634958', 'kind': 'analytics#profile', 'selfLink': 'https://www.googleapis.com/analytics/v3/management/accounts/137429915/webproperties/UA-137429915-1/profiles/192634958', 'accountId': '137429915', 'webPropertyId': 'UA-137429915-1', 'internalWebPropertyId': '197891938', 'name': 'All Web Site Data', 'currency': 'JPY', 'timezone': 'Asia/Tokyo', 'websiteUrl': 'https://myfirsraccount.firebaseapp.com', 'siteSearchQueryParameters': 'test1,test2,test3', 'stripSiteSearchQueryParameters': True, 'type': 'WEB', 'permissions': {'effective': ['COLLABORATE', 'EDIT', 'READ_AND_ANALYZE']}, 'created': '2019-04-01T09:11:27.694Z', 'updated': '2020-03-12T07:45:18.069Z', 'eCommerceTracking': True, 'enhancedECommerceTracking': True, 'botFilteringEnabled': False, 'parentLink': {'type': 'analytics#webproperty', 'href': 'https://www.googleapis.com/analytics/v3/management/accounts/137429915/webproperties/UA-137429915-1'}, 'childLink': {'type': 'analytics#goals', 'href': 'https://www.googleapis.com/analytics/v3/management/accounts/137429915/webproperties/UA-137429915-1/profiles/192634958/goals'}}
    sample_data_parsed = {
        "ビューID": [sample_data["id"]],
        "名前": [sample_data["name"]],
        "プロパティID": [sample_data["webPropertyId"]],
        "通貨": [sample_data["currency"]],
        "タイムゾーン": [sample_data["timezone"]],
        "ウェブサイトURL": [sample_data["websiteUrl"]],
        "検索クエリ": [sample_data["siteSearchQueryParameters"]],
        "検索クエリの除外": [sample_data["stripSiteSearchQueryParameters"]],
        "eコマース": [sample_data["eCommerceTracking"]],
        "拡張eコマース": [sample_data["enhancedECommerceTracking"]],
        "ボットのフィルタ": [sample_data["botFilteringEnabled"]],
    }

    WriteCsv.write(sample_data_parsed, sample_file_name)