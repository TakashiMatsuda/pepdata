# Copyright (c) 2014. Mount Sinai School of Medicine
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import print_function, division, absolute_import


TCGA_SOURCES = {}

TCGA_SERVER = "https://tcga-data.nci.nih.gov"
TCGA_BASE_DIR = "/tcgafiles/ftp_auth/distro_ftpusers/anonymous/tumor/"


# Bladder Urothelial Carcinoma
TCGA_SOURCES['blca'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "blca/gsc/broad.mit.edu/illuminaga_dnaseq/mutations/"
    "broad.mit.edu_BLCA.IlluminaGA_DNASeq.Level_2.1.3.0/"
    "BLCA-28-original.aggregated.tcga.somatic.maf"
)

# Pancreatic Adenocarcinoma
TCGA_SOURCES['paad'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "paad/gsc/broad.mit.edu/illuminaga_dnaseq/mutations/"
    "broad.mit.edu_PAAD.IlluminaGA_DNASeq.Level_2.0.3.0/"
    "PR_TCGA_PAAD_PAIR_Capture_All_Pairs_QCPASS_v3.aggregated.capture.tcga.uuid.somatic.maf"
)

# Head and Neck Squamous Carcinoma
TCGA_SOURCES['hnsc'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "hnsc/gsc/broad.mit.edu/illuminaga_dnaseq/mutations/"
    "broad.mit.edu_HNSC.IlluminaGA_DNASeq.Level_2.1.0.0/"
    "PR_TCGA_HNSC_PAIR_Capture_TP-NT_TP-NB.aggregated.capture.tcga.uuid.somatic.maf"
)

# Glioblastoma
TCGA_SOURCES['gbm'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "gbm/gsc/broad.mit.edu/illuminaga_dnaseq/mutations/"
    "broad.mit.edu_GBM.IlluminaGA_DNASeq.Level_2.100.1.0/"
    "step4_gbm_liftover.aggregated.capture.tcga.uuid.maf2.4.migrated.somatic.maf"
)

# Adenoid Cystic Carcinoma
TCGA_SOURCES['acc'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "acc/gsc/broad.mit.edu/illuminaga_dnaseq_curated/"
    "mutations/broad.mit.edu_ACC.IlluminaGA_DNASeq_curated.Level_2.1.0.0/"
    "An_TCGA_ACC_External_capture_All_Pairs.aggregated.capture.tcga.uuid.curated.somatic.maf"
)

TCGA_SOURCES['brca'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "brca/gsc/genome.wustl.edu/illuminaga_dnaseq_curated/mutations/"
    "genome.wustl.edu_BRCA.IlluminaGA_DNASeq_curated.Level_2.1.1.0/"
    "genome.wustl.edu_BRCA.IlluminaGA_DNASeq.Level_2.1.1.0.curated.somatic.maf"
)

TCGA_SOURCES['cesc'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "cesc/gsc/broad.mit.edu/illuminaga_dnaseq/mutations/"
    "broad.mit.edu_CESC.IlluminaGA_DNASeq.Level_2.1.4.0/"
    "PR_TCGA_CESC_PAIR_Capture_All_Pairs.aggregated.capture.tcga.uuid.somatic.maf"
)

# Colorectal adenocarcinoma
TCGA_SOURCES['coad'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "coad/gsc/hgsc.bcm.edu/solid_dnaseq/mutations/"
    "hgsc.bcm.edu_COAD.SOLiD_DNASeq.Level_2.1.7.0/"
    "hgsc.bcm.edu_COAD.SOLiD_DNASeq.1.somatic.maf"
)

TCGA_SOURCES['kich'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "kich/gsc/hgsc.bcm.edu/mixed_dnaseq_curated/mutations/"
    "hgsc.bcm.edu_KICH.Mixed_DNASeq_curated.Level_2.1.0.0/"
    "hgsc.bcm.edu_KICH.IlluminaGA_DNASeq.1.somatic.maf"
)

TCGA_SOURCES['kirc'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "kirc/gsc/hgsc.bcm.edu/mixed_dnaseq/mutations/"
    "hgsc.bcm.edu_KIRC.Mixed_DNASeq.Level_2.1.2.0/"
    "hgsc.bcm.edu_KIRC.Mixed_DNASeq.1.somatic.maf"
)

TCGA_SOURCES['kirp'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "kirp/gsc/broad.mit.edu/illuminaga_dnaseq_curated/mutations/"
    "broad.mit.edu_KIRP.IlluminaGA_DNASeq_curated.Level_2.1.1.0/"
    "An_TCGA_KIRP_MultiCenterCalling_capture_All_Pairs.aggregated"
    ".capture.tcga.uuid.curated.somatic.maf"
)

TCGA_SOURCES['laml'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "laml/gsc/genome.wustl.edu/illuminaga_dnaseq/mutations/"
    "genome.wustl.edu_LAML.IlluminaGA_DNASeq.Level_2.2.16.0/"
    "genome.wustl.edu_LAML.IlluminaGA_DNASeq.Level_2.2.13.0.somatic.maf"
)

TCGA_SOURCES['lgg'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "lgg/gsc/broad.mit.edu/illuminaga_dnaseq_curated/mutations/"
    "broad.mit.edu_LGG.IlluminaGA_DNASeq_curated.Level_2.1.2.0/"
    "TCGA_FREEZE_FINAL_ULTRAMUT_REMOVED.aggregated.capture.tcga.uuid.curated.somatic.maf"
)

TCGA_SOURCES['luag'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "luad/gsc/broad.mit.edu/illuminaga_dnaseq/mutations/"
    "broad.mit.edu_LUAD.IlluminaGA_DNASeq.Level_2.0.2.0/"
    "LUAD.exome.cleaned.somatic.maf"
)

TCGA_SOURCES['lusc'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "lusc/gsc/broad.mit.edu/illuminaga_dnaseq/mutations/"
    "broad.mit.edu_LUSC.IlluminaGA_DNASeq.Level_2.1.5.0/"
    "LUSC_Paper_v8.aggregated.tcga.somatic.maf"
)

TCGA_SOURCES['prad'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "prad/gsc/broad.mit.edu/illuminaga_dnaseq_curated/mutations/"
    "broad.mit.edu_PRAD.IlluminaGA_DNASeq_curated.Level_2.1.3.0/"
    "PR_TCGA_PRAD_PAIR_Capture_All_Pairs_QCPASS_v4_curated."
    "aggregated.capture.tcga.uuid.curated.somatic.maf"
)

TCGA_SOURCES['skcm'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "skcm/gsc/broad.mit.edu/illuminaga_dnaseq/mutations/"
    "broad.mit.edu_SKCM.IlluminaGA_DNASeq.Level_2.1.5.0/"
    "skcm_clean_pairs.aggregated.capture.tcga.uuid.somatic.maf"
)

TCGA_SOURCES['stad'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "stad/gsc/broad.mit.edu/illuminaga_dnaseq_curated/mutations/"
    "broad.mit.edu_STAD.IlluminaGA_DNASeq_curated.Level_2.1.3.0/"
    "QCv5_blacklist_Pass.aggregated.capture.tcga.uuid.curated.somatic.maf"
)

TCGA_SOURCES['tcha'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "thca/gsc/broad.mit.edu/illuminaga_dnaseq/mutations/"
    "broad.mit.edu_THCA.IlluminaGA_DNASeq.Level_2.1.5.0/"
    "AN_TCGA_THCA_PAIR_Capture_ALLQC_14Aug2013_429.aggregated.capture.tcga.uuid.somatic.maf"
)

TCGA_SOURCES['ucec'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "ucec/gsc/genome.wustl.edu/illuminaga_dnaseq/mutations/"
    "genome.wustl.edu_UCEC.IlluminaGA_DNASeq.Level_2.1.7.0/"
    "genome.wustl.edu_UCEC.IlluminaGA_DNASeq.Level_2.1.7.somatic.maf"
)

TCGA_SOURCES['ucs'] = TCGA_SERVER + TCGA_BASE_DIR + (
    "ucs/gsc/broad.mit.edu/illuminaga_dnaseq_curated/mutations/"
    "broad.mit.edu_UCS.IlluminaGA_DNASeq_curated.Level_2.1.0.0/"
    "AN_TCGA_UCS_PAIR_Capture_56.aggregated.capture.tcga.uuid.curated.somatic.maf"
)
