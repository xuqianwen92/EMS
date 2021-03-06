## Local ems economic dispatch computing format
# Diesel generator set
PG = 0
RG = 1
# Utility grid set
PUG = 2
RUG = 3
# Bi-directional convertor set
PBIC_AC2DC = 4
PBIC_DC2AC = 5
# Energy storage system set
PESS_C = 6
PESS_DC = 7
RESS = 8
EESS = 9
# Neighboring MG set
PMG = 10
# Emergency curtailment or shedding set
PPV = 11
PWP = 12
PL_AC = 13
PL_UAC = 14
PL_DC = 15
PL_UDC = 16
# Set points tracing, three dimensions: Utility grid, energy sharing MGs and SOC of ESSs
PUG_positive = 17
PUG_negative = 18
PMG_positive = 19
PMG_negative = 20
SOC_positive = 21
SOC_negative = 22
# Total number of decision variables
NX = 23