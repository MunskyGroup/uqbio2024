#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 08:04:38 2024

@author: munsky
"""

import numpy as np

def chooseMember(students, probs):
    if np.sum(probs)==0:
        print('All probabilities are zero - Nothing to choose!')
        return [], []
        
    # Ensure that probabilities sum to 1
    probs = probs / np.sum(probs)
    
    # Randomly select an entry based on the probability mass function
    student = np.random.choice(students, p=probs)
    
    # Get the index of the chosen entry
    index = students.index(student)
    
    return student, index

def spring2024Students():
    return ['Shelby Ardehali',
              'Becca Balliew',
              'Shelby Bauer',
              'Sarah Bermingham',
              'Nicole Blais',
              'Carley Boulger',
              'Cassandra Buffington',
              'Alex Cerullo',
              'Mikayla Cox',
              'Alex David',
              'Zoe Fiedler',
              'Lauren Frueh',
              'Keigan Garrity',
              'Sydney Graul',
              'Ethan Harrell',
              'Kanita Hrustanovic',
              'Zabiba Husen',
              'Austin Jones',
              'Mitchell Knutsen',
              'Isabelle Lemma',
              'Sherly Manoharan',
              'Mark Metheny',
              'Anika OBrian',
              'Abbie Tangen',
              'Vivia Van De Mark']

def geneRegulationTopics():
    return ['Signal Transduction and Cellular Signaling - Receptor-Mediated Signaling: Activation of gene expression in response to extracellular signals.',
'Signal Transduction and Cellular Signaling - Intracellular Signaling Cascades: Series of molecular events triggered by signaling molecules.',
'Signal Transduction and Cellular Signaling - Second Messenger Systems: Involvement of molecules like cAMP, cGMP, and calcium ions.',
'Signal Transduction and Cellular Signaling - Phosphorylation/Dephosphorylation: Post-translational modification of proteins to activate or deactivate signaling pathways.',
'Signal Transduction and Cellular Signaling - G-protein Coupled Receptors (GPCRs): Activation of gene expression through GPCR-mediated pathways.',
'Chromatin Remodeling and Epigenetic Regulation - Histone Modification: Acetylation, methylation, phosphorylation of histone proteins.',
'Chromatin Remodeling and Epigenetic Regulation - DNA Methylation: Addition of methyl groups to DNA, influencing gene expression.',
'Chromatin Remodeling and Epigenetic Regulation - Chromatin Remodeling Complexes: Alteration of chromatin structure to allow or restrict transcription.',
'Chromatin Remodeling and Epigenetic Regulation - Non-Coding RNAs (ncRNAs): Involvement of microRNAs (miRNAs) and long non-coding RNAs (lncRNAs).',
'Promoter Activation and Transcription Initiation - Promoter Binding Proteins: Transcription factors binding to gene promoters.',
'Promoter Activation and Transcription Initiation - Enhancers and Silencers: DNA elements influencing transcription positively (enhancers) or negatively (silencers).',
'Promoter Activation and Transcription Initiation - Transcriptional Coactivators/Co-repressors: Proteins that enhance or inhibit transcriptional activity.',
'Promoter Activation and Transcription Initiation - RNA Polymerase Recruitment: Binding of RNA polymerase to gene promoters.',
'Promoter Activation and Transcription Initiation - Mediator Complex: Bridges between transcription factors and RNA polymerase.',
'Transcription Elongation and Termination - Elongation Factors: Proteins facilitating RNA polymerase movement along the DNA.',
'Transcription Elongation and Termination - Pausing and Anti-Pausing Factors: Regulation of RNA polymerase pausing and elongation.',
'Transcription Elongation and Termination - Terminator Sequences: Signals marking the end of transcription.',
'RNA Processing and Modification - RNA Splicing: Removal of introns and joining of exons.',
'RNA Processing and Modification - Polyadenylation: Addition of poly-A tail to mRNA.',
'RNA Processing and Modification - RNA Editing: Alteration of nucleotide sequence in RNA transcripts.',
'mRNA Transport and Localization - Nuclear Export: Transport of mature mRNA from the nucleus to the cytoplasm.',
'mRNA Transport and Localization - mRNA Localization Signals: Sequences directing mRNA to specific cellular locations.',
'Translation Initiation and Elongation - Ribosome Binding Sites: Recognition of mRNA by ribosomes.',
'Translation Initiation and Elongation - Initiator tRNA: tRNA carrying the first amino acid in translation.',
'Translation Initiation and Elongation - eIFs (Eukaryotic Initiation Factors): Proteins facilitating translation initiation.',   
'Translation Initiation and Elongation - Termination Factors: Proteins involved in translation termination.',
'Post-Translational Modification - Protein Phosphorylation: Addition of phosphate groups to proteins.',
'Post-Translational Modification - Ubiquitination: Addition of ubiquitin molecules for protein degradation.',
'Post-Translational Modification - Acetylation/Deacetylation: Addition or removal of acetyl groups to regulate protein function.', 
'Post-Translational Modification - Glycosylation: Addition of sugar moieties to proteins.',
'Protein Folding and Stability - Chaperone Proteins: Assist in proper protein folding.',    
'Protein Folding and Stability - Proteasomal Degradation: Targeted degradation of proteins by the proteasome.',
'Cellular Localization - Nuclear Localization Signals (NLS): Sequences directing proteins to the nucleus.',    
'Cellular Localization - Mitochondrial Targeting Signals: Sequences directing proteins to mitochondria.',    
'Cellular Localization - Endoplasmic Reticulum (ER) Targeting Signals: Sequences directing proteins to the ER.',
'Feedback Regulation and Feedback Inhibition - Negative Feedback Loops: Mechanisms to dampen excessive gene expression.',    
'Feedback Regulation and Feedback Inhibition - miRNA-mediated Regulation: Post-transcriptional regulation by microRNAs.',
'Environmental and Metabolic Regulation - Nutrient Availability: Availability of nutrients influencing gene expression.',
'Environmental and Metabolic Regulation - Oxygen and Redox Regulation: Cellular oxygen levels affecting gene expression.', 
'Environmental and Metabolic Regulation - Metabolite Sensing: Cellular metabolite levels impacting gene regulation.',
'Stress Response - Heat Shock Proteins (HSPs): Induction in response to cellular stress.',
'Stress Response - DNA Damage Response: Activation of repair mechanisms in response to DNA damage.',
'Hormonal Regulation - Steroid Hormones: Influence gene expression through nuclear receptors.',    
'Hormonal Regulation - Peptide Hormones: Signaling cascades activated by peptide hormones.',
'Epistasis and Genetic Interaction - Genetic Interactions: Interaction between genes influencing expression patterns.',    
'Epistasis and Genetic Interaction - Epistasis: Gene interaction where the effect of one gene depends on the presence of another.',
'Non-Genetic Inheritance - Transgenerational Epigenetic Inheritance: Inheritance of epigenetic marks across generations.',
'Cell Cycle Regulation - Cyclins and Cyclin-Dependent Kinases (CDKs): Regulate gene expression during the cell cycle.',
'Cellular Differentiation - Master Regulator Genes: Genes controlling cell fate determination and differentiation.',   
'Cell Signaling Gradients - Gradients of signaling molecules influencing gene expression patterns.']
