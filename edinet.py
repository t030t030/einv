import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

import const
from datetime import date
from datetime import timedelta

def get_data_from_edinet(dt):
  p = {'date': dt.isoformat(), 'type': const.EdinetDocType}
  r = requests.get(const.EdinetEndpoint, params=p, verify=False)
  dic = r.json()
  if dic[const.EdinetJsonKeysmetadata][const.EdinetJsonKeysstatus] == '200':
    return dic[const.EdinetJsonKeysresults]
  else:
    return None

def get_matched_docID(dic, s=None):
  if dic is None:
    return None
  else:
    if s is None:
      return [d[const.EdinetJsonKeysdocID] for d in dic]
    else:
      return [d[const.EdinetJsonKeysdocID] for d in dic if s in d[const.EdinetJsonKeysdocDescription]]

# print(get_matched_docID(get_data_from_edinet(date.today()-timedelta(days=3)), "有価証券報告書"))

def save_yukashoken_pdf_each_day(dt):
  l = get_matched_docID(get_data_from_edinet(dt), "有価証券報告書")
  if l is not None:
    for ll in l:
