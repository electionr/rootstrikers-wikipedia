import csv
import string 
import legislators_current as leg
import dump

fecs = {}
legs= leg.load()
for x in sorted(legs['wp'].keys()):
    obj= legs['wp'][x]
    idsobj= obj['id'] 
    name = obj['name']['official_full'] 
    if 'fec' in idsobj:
        for fec in idsobj['fec']:
            #print "fec",fec
            fecs[fec]=obj

filename= "maplight-convert/FEC2012c2.csv"
fieldnames=[ "TransactionTypeCode","TransactionType","ElectionCycle","ReportingCommitteeMLID","ReportingCommitteeFECID","ReportingCommitteeName","ReportingCommitteeNameNormalized","PrimaryGeneralIndicator","TransactionID","FileNumber","RecordNumberML","RecordNumberFEC","TransactionDate","TransactionAmount","RecipientName","RecipientNameNormalized","RecipientCity","RecipientState","RecipientZipCode","RecipientCommitteeMLID","RecipientCommitteeFECID","RecipientCommitteeName","RecipientCommitteeNameNormalized","RecipientCommitteeTreasurer","RecipientCommitteeDesignationCode","RecipientCommitteeDesignation","RecipientCommitteeTypeCode","RecipientCommitteeType","RecipientCommitteeParty","RecipientCandidateMLID","RecipientCandidateFECID","RecipientCandidateName","RecipientCandidateNameNormalized","RecipientCandidateParty","RecipientCandidateICO","RecipientCandidateStatus","RecipientCandidateOfficeState","RecipientCandidateOffice","RecipientCandidateDistrict","RecipientCandidateGender","DonorName","DonorNameNormalized","DonorCity","DonorState","DonorZipCode","DonorEmployer","DonorEmployerNormalized","DonorOccupation","DonorOccupationNormalized","DonorOrganization","DonorEntityTypeCode","DonorEntityType","DonorCommitteeMLID","DonorCommitteeFECID","DonorCommitteeName","DonorCommitteeNameNormalized","DonorCommitteeTreasurer","DonorCommitteeDesignationCode","DonorCommitteeDesignation","DonorCommitteeTypeCode","DonorCommitteeType","DonorCommitteeParty","DonorCandidateMLID","DonorCandidateFECID","DonorCandidateName","DonorCandidateNameNormalized","DonorCandidateParty","DonorCandidateICO","DonorCandidateStatus","DonorCandidateOfficeState","DonorCandidateOffice","DonorCandidateDistrict","DonorCandidateGender","UpdateTimestamp" ]

fec_dict_reader = csv.DictReader(open(filename), delimiter=',', quotechar='"', restkey=100, fieldnames=fieldnames)
from collections import defaultdict
matrix = defaultdict(dict)
#print fec_dict_reader.fieldnames

f = open(filename + ".xml", 'w')
for line in fec_dict_reader:
    for k in fieldnames :
        d = line[k]
        if (isinstance( d, int )):
            d= str(d)
        if d is not None  and d != '':           

            val = line['TransactionAmount']
            if (val == 'TransactionAmount'):
                continue
            if (len(val)> 0):
                try:
                    val = int(val)
                except:
                    print "'%s'" % val, "failed"
            else:
                val = 0
            if string.find(k,"CandidateFECID") > 0:
                if d not in fecs:
                    fecs[d]= {}
                    fecs[d]["fec_2012_2total"] =val
                else:
                    if "fec_2012_2total" in fecs[d]:
                        fecs[d]["fec_2012_2total"] = fecs[d]["fec_2012_2total"] + val 
                    else:
                        fecs[d]["fec_2012_2total"] = val                  

dump.dump(fecs)
