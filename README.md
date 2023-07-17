# team01 of topic02 


# Deep Mutational Scan Analysis of TEM-1 Beta-Lactamase
## What is this about?
TEM-1 Beta-Lactamase is an enzyme which enables bacteria, like *Escherichia Coli* to gain resistance against Beta-Lactam antibiotics. Based on a collection of Deep-Mutational-Scan (DMS) datasets (Notin et al., 2022) providing fitness scores for single mutants for every position of TEM-1 Beta-Lactamse an analysis was performed. The goals were to understand more about the infuence of different DMS-methods, assessment of the mutational robustness or fragility for each residue and the connection between conservation and DMS-data.

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
* [Evaluation of normalization methods](Final_Cleanup_Normalization_PositionEffects.ipynb): Based on a Wilcoxon Signed Ranked Test between the Stiffler and Firnberg dataset, it was evaluated if Z-normalization or Min-Max-normalization should be performed
* [Normaliztaion](Final_Cleanup_Normalization_PositionEffects.ipynb): z-normalization was performed for all datasets
* [Creation and evaluation of different Position Effect models](Final_Cleanup_Normalization_PositionEffects.ipynb): Three Position Effect Models were created (Mean DMS-score Mode, Quantile Model, Area Under Curve Model) and evaluated based on the correlation between the model-value and conservation.
* [Multiple Sequence Alignment (MSA)](Final_Alignment.ipynb) : Based on the RefSeq library an MSA was performed. Conservation Scores are calculated with two different models (Pei & Grishin conservation, Shannon entropy). The models are compared to each other. For the evaluation of three hypotheses which were stated to judge the performance of the Position Effect Models all residues were categorized by DMS-Scores and Conservation. After creation of consensus sequences with different methods (self-calculated consensus sequence, EMBOSS Consensus Alignment), the types of mismatches between the consensus sequences and the wild type sequence were examined to evaluate the hypotheses.

## Necessary Packages
All the necessary packages can be found in the [enviroment.yml](enviroment.yml) file.



