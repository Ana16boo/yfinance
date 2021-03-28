|                                 |                  GENERAL INFORMATION                                                                           |
|---------------------------------|----------------------------------------------------------------------------------------------------------------|
| Test Stage:                     | ⬛️ Unit ☐ Functionality ☐ Performance ☐ Regression ☐ Integration ☐ Acceptance ☐ System ☐ Pilot ☐ Interface |
| Test Date:                      | 03/26/2021                                                                                                     |
| System Date, if applicable:     | N/A                                                                                                            |
| Tester:                         | Xiyuan Shen                                                      |
| Test Case Number:               | 2                                                                                                              |
| Test Case Description:          | This test checks if the code handles when the variable ‘cal’ gets a pandas DataFrame that contains only NaNs.  |
| Results:                        | ☐ Pass ⬛️ Fail                                                                                                 |
| Incident Number, if applicable: | Not applicable                                                        |


|                              |                     INTRODUCTION                                                                                                                                      |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requirement(s) to be tested: | To test if the code can handle when the 'cal' variables get DataFrame that only have NaNs/None                                  |
| Roles and Responsibilities:  | xiyuan1 |
| Set Up Procedures:           | create a mock dataframe, then set the data as None. After setting up, check if the code can handle the None/NaNs in panda DataFrame                                                                                      |
| Stop Procedures:             | If correct, then it stop it will go through all the test. If not, then it will stop.                                                                                                     |


|                          |                     ENVIRONMENTAL NEEDS                                                                                                  |
|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Hardware:                | None                                            |
| Software:                | python and yfinance library  |
| Procedural Requirements: | have all the file in floder                                                      |


|                           |                     TEST                                                                                                                                                                                                      |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Test Items and Features:  | Check if the 'event' can handle the problem when the 'cal' is with panda DataFrame of None/NaNs                                                                                                                                       |
| Input Specifications:     | None type data                                                                                                                  |
| Procedural Steps:         | after get the input, check if the 'cal' is correct tye in 'event'                                                                                                                          |
| Expected Results of Case: | pass                                                                                                                                               |


|                        |                     ACTUAL RESULTS                                                                                                |
|------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| Output Specifications: | Failed the test                                    |



