import sys, datetime, csv, json
sys.path.append('..')
from common.getServiceClient import GetServiceClient
#Google API Client
from apiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials

class UpdateGoals:
    def __init__(self, data_file_name):
        self.data_file_name = data_file_name

    def getData(self):
        with open(self.data_file_name, newline='') as csvfile:
            print("opened csv: ", self.data_file_name)
            rows = csv.reader(csvfile, delimiter=',', quotechar='"')

            goals = []
            index = 0
            for row in rows:
                goal = {}
                if index ==0:
                    pass
                else:
                    row_values = row
                    print("---row_values: ", row_values)

                    goal["param"] = {
                        "accountId": row_values[0],
                        "webPropertyId": row_values[1],
                        "profileId": row_values[2],
                        "id": row_values[3],
                    }
                    goal["body"] = {
                        "name": row_values[4],
                        "value": row_values[5],
                        "active": row_values[6],
                        "type": row_values[7],
                    }
                    if goal["body"]["type"] == "URL_DESTINATION":
                        steps_parsed = json.loads(row_values[12].replace("'",'"'))
                        goal["body"]["urlDestinationDetails"] = {
                            "url": row_values[8],
                            "caseSensitive": row_values[9],
                            "matchType": row_values[10],
                            "firstStepRequired": row_values[11],
                            "steps": steps_parsed,
                        }
                    elif goal["body"]["type"] == "EVENT":
                        eventConditions_parsed = json.loads(row_values[13].replace("'",'"'))
                        goal["body"]["eventDetails"] = {
                            "eventConditions": eventConditions_parsed,
                            "useEventValue": row_values[14],
                        }

                    elif goal["body"]["type"] == "VISIT_NUM_PAGES":
                        goal["body"]["visitNumPagesDetails"] = {
                            "comparisonType": row_values[15],
                            "comparisonValue": row_values[16],
                        }
                    elif goal["body"]["type"] == "VISIT_TIME_ON_SITE":
                        goal["body"]["visitTimeOnSiteDetails"] = {
                            "comparisonType": row_values[17],
                            "comparisonValue": row_values[18],
                        }
                    print("---get parsed goals: ", index, goals)
                    print("---eventConditions: ", index, row_values[13])
                    print("---useEventValue: ", index, row_values[14])
                    goals.insert(index, goal)
                index += 1
#            print(goals)
            return goals

    def updateGoal(self, goal):
        try:
            service = GetServiceClient.get()
            service.management().goals().update(
                accountId = goal["param"]["accountId"],
                webPropertyId = goal["param"]["webPropertyId"],
                profileId = goal["param"]["profileId"],
                goalId = goal["param"]["id"],
                body = goal["body"],
          ).execute()

        except TypeError as error:
            # Handle errors in constructing a query.
            print('There was an error in constructing your query : %s' % error )
        # except HttpError as error:
        #   # Handle API errors.
        #   print ('There was an API error : %s : %s' %
        #          (error.resp.status, error.resp.reason))

    def updateGoals(self):
        goals = self.getData()
        for goal in goals:
            print("start put a goal setting: ", goal)
            self.updateGoal(goal)

if __name__ == "__main__":
    print("input data file name")
    data_file_name = "input_file/" + input()
    UpdateGoals(data_file_name).updateGoals()
