# team01 of topic02 


# Deep Mutational Scan Analysis of TEM-1 Beta-Lactamase
## What is this about?
TEM-1 Beta-Lactamase is an enzyme which enables bacteria, like *Escherichia coli* to gain resistance against Beta-Lactam antibiotics. Based on a collection of Deep-Mutational-Scan (DMS) datasets (Notin et al., 2022) providing fitness scores for single mutants for every position of TEM-1 Beta-Lactamse an analysis of the enzyme was performed. The goals were to gain deeper understanding about the influence of different DMS-methods and to assess the mutational robustness or fragility for each residue and the connection between conservation and DMS-data. Three hypotheses were formulated for the analysis:

I.) High fragility conditions higher conservation of a residue.

II.) Conservation occurs only when necessary, thus at fragile residues.

III.) Thus, high robustness conditions lower conservation. 

## Structure
[Final_Cleanup_Normalization_PositionEffects.ipynb](Final_Cleanup_Normalization_PositionEffects.ipynb) and [Final_Alignment.ipynb](Final_Alignment.ipynb) contain the main functions.
The "Extended" files contain the main functions & further explorations.

## Datasets
### DMS-datasets
The Analysis was performed based on three datasets. The DMS-methods which were used to create these datasets can be divided in two types:
#### "growth method"
* Stiffler et al.
* Firnberg et al.
#### “resistance method”
* Deng et al.

The fitness values from the original csv files are not normalized.
Find the original csv files [here](dataSources/DMS_datasets).

### MSA-datasets
Find the original files for the MSA [here](dataSources/MSA_datasets).

### Handovers
Handovers are .csv or .pkl files, that are created through the code and are used to communicate processed data between the notebkooks. Therefor they are stored in the directory "[handovers](dataSources/handovers)".

## Main Features
* [Data Cleaning](Final_Cleanup_Normalization_PositionEffects.ipynb)
* [Evaluation of normalization methods](Final_Cleanup_Normalization_PositionEffects.ipynb): Based on a visual analysis by heatmaps and a Wilcoxon Signed Ranked Test between the datasets, different normalization methods were evaluated.
* [Normaliztaion](Final_Cleanup_Normalization_PositionEffects.ipynb): Z-normalization was performed for all datasets
* [Creation and evaluation of different Position Effect models](Final_Cleanup_Normalization_PositionEffects.ipynb): Three Position Effect Models were created (Mean DMS-score Mode, Quantile Model, Area Under Curve Model) and evaluated based on the correlation between the model-value and conservation.
* [Multiple Sequence Alignment (MSA)](Final_Alignment.ipynb) : Based on the RefSeq library an MSA was performed. Conservation Scores are calculated with two different models (Pei & Grishin conservation, Shannon entropy). The models are compared to each other. For the evaluation of the three hypotheses which were stated to judge the accuracy of the DMS-datasets, all residues were categorized by DMS-Scores and Conservation. After creation of consensus sequences with different methods (self-calculated consensus sequence, EMBOSS Consensus Alignment), the types of mismatches between the consensus sequences and the wild type sequence were examined to evaluate the hypotheses.

## Necessary Packages
All the necessary packages can be found in the [enviroment.yml](enviroment.yml) file.



