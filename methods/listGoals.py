#Usage: "$XXX.py <accountId> <webPropertyId>"

import sys, datetime
sys.path.append('..')
from common.getServiceClient import GetServiceClient
from common.writeCsv import WriteCsv
from listViews import ListViews
#Google API Client
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

class ListGoals:
    def __init__(self, accountId, webPropertyId):
#        now = datetime.datetime.now()
#        timestamp = now.strftime("%Y%m%d%H%M%S")

        self.accountId = accountId
        self.webPropertyId = webPropertyId
#        self.output_file_name = "get_goals_"+ str(timestamp) + ".csv"
        self.output_file_name = "list_goals.csv"
        self.view_id_column_name = "ビューID"

    def get(self, service, view_id):
        try:
            goals = service.management().goals().list(
                accountId = self.accountId,
                webPropertyId = self.webPropertyId,
                profileId = view_id
            ).execute()
            print("start get view goal - view id: ", view_id) #debug
        except TypeError as error:
            print('There was an error in constructing your query : %s' % error)

        return goals

    def parse(self, view_id):
        service = GetServiceClient.get()
        goals = self.get(service, view_id)

        accountId = []
        webPropertyId = []
        profileId = []
        id = []
        name = []
        value = []
        active = []
        type = []
        page_url = []
        page_caseSensitive = []
        page_matchType = []
        page_firstStepRequired = []
        page_steps = []
        event_eventConditions = []
        event_useEventValue = []
        pv_comparisonType = []
        pv_comparisonValue = []
        time_comparisonType = []
        time_comparisonValue = []
        created = []
        updated = []
        goals_parsed = {
            "accountId": accountId,
            "webPropertyId": webPropertyId,
            "profileId": profileId,
            "id": id,
            "name": name,
            "value": value,
            "active": active,
            "type": type,
#            "詳細": detail,
            "page_url": page_url,
            "page_caseSensitive": page_caseSensitive,
            "page_matchType": page_matchType,
            "page_firstStepRequired": page_firstStepRequired,
            "page_steps": page_steps,
            "event_eventConditions": event_eventConditions,
            "event_useEventValue": event_useEventValue,
            "pv_comparisonType": pv_comparisonType,
            "pv_comparisonValue": pv_comparisonValue,
            "time_comparisonType": time_comparisonType,
            "time_comparisonValue": time_comparisonValue,
            "created": created,
            "updated": updated,
        }

        index = 0
        for goal in goals.get('items', []):
            accountId.insert(index, goal.get('accountId'))
            webPropertyId.insert(index, goal.get('webPropertyId'))
            profileId.insert(index, goal.get('profileId'))
            id.insert(index, goal.get('id'))
            name.insert(index, goal.get('name'))
            value.insert(index, goal.get('value'))
            active.insert(index, goal.get('active'))
            type.insert(index, goal.get('type'))
            created.insert(index, goal.get('created'))
            updated.insert(index, goal.get('updated'))

            # Print the goal details depending on the type of goal.
            if goal.get('urlDestinationDetails'):
                page_detail = goal.get('urlDestinationDetails')
                page_url.insert(index,page_detail.get('url'))
                page_caseSensitive.insert(index, page_detail.get('caseSensitive'))
                page_matchType.insert(index, page_detail.get('matchType'))
                page_firstStepRequired.insert(index, page_detail.get('firstStepRequired'))
                page_steps.insert(index, page_detail.get('steps'))
            else:
                page_url.insert(index,False)
                page_caseSensitive.insert(index, False)
                page_matchType.insert(index, False)
                page_firstStepRequired.insert(index, False)
                page_steps.insert(index, False)

            if goal.get('eventDetails'):
                event_detail = goal.get('eventDetails')
                event_eventConditions.insert(index, event_detail.get('eventConditions'))
                event_useEventValue.insert(index, event_detail.get('useEventValue'))
            else:
                event_eventConditions.insert(index, False)
                event_useEventValue.insert(index, False)

            if goal.get('visitNumPagesDetails'):
                pv_detail = goal.get('visitNumPagesDetails')
                pv_comparisonType.insert(pv_detail.get('comparisonType'))
                pv_comparisonValue.insert(pv_detail.get('comparisonValue'))
            else:
                pv_detail = goal.get('visitNumPagesDetails')
                pv_comparisonType.insert(index, False)
                pv_comparisonValue.insert(index, False)

            if goal.get('visitTimeOnSiteDetails'):
                time_detail = goal.get('visitTimeOnSiteDetails')
                time_comparisonType.insert(time_detail.get('comparisonType'))
                time_comparisonValue.insert(time_detail.get('comparisonValue'))
            else:
                time_comparisonType.insert(index, False)
                time_comparisonValue.insert(index, False)

            index += 1

        return goals_parsed
    def outputCsv(self, view_id):
        data_parsed = self.parse(view_id)
        WriteCsv.write(data_parsed, self.output_file_name)

    def outputCsvLoop(self):
        views_parsed = ListViews(self.accountId,self.webPropertyId).parse()
        view_ids = views_parsed[self.view_id_column_name]
        for id in view_ids:
            print("outputCsvLoop start - view id: ", id) #debug
            self.outputCsv(id)

if __name__ == '__main__':
    argc = len(sys.argv)
    try:
        accountId = sys.argv[1]
        webPropertyId = sys.argv[2]
        ListGoals(accountId, webPropertyId).outputCsvLoop()
    except IndexError as error:
        print("Usage: $py XXX.py <account id> <property id> ")
