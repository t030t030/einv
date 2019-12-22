import sys

class _const:

    class ConstError(TypeError):
        pass

    def __setattr__(self, name, value):

        if name in self.__dict__:
            raise self.ConstError("Cannot rebind const(%S)" % name)

        self.__dict__[name] = value

sys.modules[__name__] = _const()

import const

const.EdinetEndpoint = "https://disclosure.edinet-fsa.go.jp/api/v1/documents.json"
const.EdinetDocType = 2
const.EdinetJsonKeysmetadata = 'metadata'
const.EdinetJsonKeysstatus = 'status'
const.EdinetJsonKeysresults = 'results'
const.EdinetJsonKeysdocID = 'docID'
const.EdinetJsonKeyssecCode = 'secCode'
const.EdinetJsonKeysdocDescription = 'docDescription'
const.YukashokenDir = "./stat/yukashoken/pdf/"