#Usage: "$XXX.py <accountId> <webPropertyId>"

import sys, datetime
sys.path.append('..')
from common.getServiceClient import GetServiceClient
from common.writeCsv import WriteCsv
#Google API Client
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

class ListViews:
    def __init__(self, accountId, webPropertyId):
#        now = datetime.datetime.now()
#        timestamp = now.strftime("%Y%m%d%H%M%S")

        self.accountId = accountId
        self.webPropertyId = webPropertyId
        self.output_file_name = "list_views.csv"
#        self.output_file_name = "get_views_"+ str(timestamp) + ".csv"

    def get(self,service):
        try:
            views = service.management().profiles().list(
                accountId = self.accountId,
                webPropertyId = self.webPropertyId
            ).execute()

        except TypeError as error:
            print ('There was an error in constructing your query : %s' )% error
        return views

    def parse(self):
        service = GetServiceClient.get()
        views = self.get(service)

        accountId = []
        webPropertyId = []
        id = []
        name = []
        defaultPage = []
        websiteUrl = []
        siteSearchQueryParameters = []
        stripSiteSearchQueryParameters = []
        siteSearchCategoryParameters = []
        stripsiteSearchCategoryParameters = []
        botFilteringEnabled = []
        currency = []
        timezone = []
        eCommerceTracking = []
        enhancedECommerceTracking = []
        created = []
        updated = []
        views_parsed = {
            "アカウントID": accountId,
            "プロパティID": webPropertyId,
            "ビューID": id,
            "名前": name,
            "デフォルトのページ": defaultPage,
            "ウェブサイトURL": websiteUrl,
            "検索クエリ": siteSearchQueryParameters,
            "検索クエリの除外": stripSiteSearchQueryParameters,
            "検索カテゴリ": siteSearchCategoryParameters,
            "検索カテゴリの除外": stripsiteSearchCategoryParameters,
            "ボットのフィルタ": botFilteringEnabled,
            "通貨": currency,
            "タイムゾーン": timezone,
            "eコマース": eCommerceTracking,
            "拡張eコマース": enhancedECommerceTracking,
            "作成日時": created,
            "更新日時": updated,
        }

        index = 0
        for view in views.get('items', []):
            accountId.insert(index, view.get("accountId"))
            webPropertyId.insert(index, view.get("webPropertyId"))
            id.insert(index, view.get("id"))
            name.insert(index, view.get("name"))
            defaultPage.insert(index, view.get("defaultPage"))
            websiteUrl.insert(index, view.get("websiteUrl"))
            siteSearchQueryParameters.insert(index, view.get("siteSearchQueryParameters"))
            stripSiteSearchQueryParameters.insert(index, view.get("stripSiteSearchQueryParameters"))
            siteSearchCategoryParameters.insert(index, view.get("siteSearchCategoryParameters"))
            stripsiteSearchCategoryParameters.insert(index, view.get("stripsiteSearchCategoryParameters"))
            botFilteringEnabled.insert(index, view.get("botFilteringEnabled"))
            currency.insert(index, view.get("currency"))
            timezone.insert(index, view.get("timezone"))
            eCommerceTracking.insert(index, view.get("eCommerceTracking"))
            enhancedECommerceTracking.insert(index, view.get("enhancedECommerceTracking"))
            created.insert(index, view.get("created"))
            updated.insert(index, view.get("updated"))

            index += 1
#        print(views_parsed)
        return views_parsed

    def outputCsv(self):
        data_parsed = self.parse()
        WriteCsv.write(data_parsed, self.output_file_name)

if __name__ == '__main__':
    argc = len(sys.argv)
    try:
        accountId = sys.argv[1]
        webPropertyId = sys.argv[2]
        ListViews(accountId,webPropertyId).outputCsv()
    except IndexError as error:
        print("Usage: $py XXX.py <account id> <property id> ")
