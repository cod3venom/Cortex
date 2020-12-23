import json

from Core.DataOperations.Logger.Logger import Logger, EMPTY
from Core.Security.Global import levels
from Core.DataOperations.StringBuilder import StringBuilder


class EkwNumbersListTObject:

    def __init__(self, ID: int, USER_ID: str, EKW_NUMBERS_PACK_ID: str, EKW_NUMBER_ID: str, FIRST_PART: str,
                 SECOND_PART: str, THIRD_PART: str, DATE: str):
        self.ID = ID
        self.USER_ID = USER_ID
        self.EKW_NUMBERS_PACK_ID = EKW_NUMBERS_PACK_ID
        self.EKW_NUMBER_ID = EKW_NUMBER_ID
        self.FIRST_PART = FIRST_PART
        self.SECOND_PART = SECOND_PART
        self.THIRD_PART = THIRD_PART
        self.DATE = DATE

    @classmethod
    def TO(cls, jsData: str):
        try:
            if jsData != EMPTY:
                return cls(**json.loads(jsData))
            else:
                return cls(
                    **{'ID': 'empty', 'USER_ID': 'empty', 'EKW_NUMBERS_PACK_ID': 'empty', 'EKW_NUMBER_ID': 'empty',
                       'FIRST_PART': 'empty', 'SECOND_PART': 'empty', 'THIRD_PART': 'empty', 'DATE': 'empty'})
        except KeyError as KeyErr:
            Logger(True, 3, levels.Error)

    def __repr__(self):
        buffer = StringBuilder()
        buffer.append("<EkwNumbersListTObject:")
        buffer.append(" ID=" + str(self.ID))
        buffer.append(" USER_ID=" + self.USER_ID)
        buffer.append(" EKW_NUMBERS_PACK_ID=" + self.EKW_NUMBERS_PACK_ID)
        buffer.append(" EKW_NUMBER_ID=" + self.EKW_NUMBER_ID)
        buffer.append(" FIRST_PART=" + self.FIRST_PART)
        buffer.append(" SECOND_PART=" + self.SECOND_PART)
        buffer.append(" THIRD_PART=" + self.THIRD_PART)
        buffer.append(" DATE=" + self.DATE)
        buffer.append(">")
        return buffer.string
