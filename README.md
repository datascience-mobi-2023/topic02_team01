# team01 of topic02 

 This is the GitHub repository for team01 of the topic02.  
 To refresh your memory on how to manage GitHub, you can find commonly used commands [here](https://github.com/joshnh/Git-Commands). 

# Deep Mutational Scan Analysis of TEM-1 Beta-Lactamase
## What is this about?
TEM-1 Beta-Lactamase is an enzyme which enables Bacteria, like *Escherichia Coli*. Based on a dataset (Notin et al., 2022) providing fitness scores for aminoacid-substitutions for every Position of TEM-1 Beta-Lactamse an analysis was performed. The targets were to understand more about the infuence of different DMS-methods, assessment of the mutational robustness or fragility for each residue and the connection between conservation and DMS-data.

### Datasets
The Analysis was performed based on three datasets. The DMS-methods which were used to create these datasets can be divided in two types:
#### "growth method"
* Stiffler et al.
* Firnberg et al.
#### “resistance method”
* Deng et al.

The fitness values from the ofiginal csv files are not normalized.
Find the original csv files [here]("Link zu den CSV Dateien einfügen")

### Main Features
* Data Cleaning ["Hier namen für die Datei einfügen auf die man Klicken muss, um zum Data Cleaning zu kommen"]("Hier den path dazu"):
* Evaluation of normalization methods ["Hier namen für die Datei einfügen auf die man Klicken muss, um zur Normalization evaluation zu kommen"]("Hier den path dazu"): Based on a Wilcoxon Signed Ranked Test bwtween the Stiffler and Firnberg dataset, it was evaluated if Z-normalization or Min-Max-normalization should be performed
* Normaliztaion ["Hier namen für die Datei einfügen auf die man Klicken muss, um zur Normalization zu kommen"]("Hier den path dazu"): z-normalization was performed for all datasets
* Creation and evaluation of different Position Effect models ["Hier namen für die Datei einfügen auf die man Klicken muss, um zu den Position effects zu kommen"]("Hier den path dazu"): Three Position Effect Models were created (Mean DMS-score Mode, Quantile Model, Area Under Curve Model) and evaluated based on the correlation between the model-value and conservation.
* Multiple Sequence Alignment (MSA) ["Hier namen für die Datei einfügen auf die man Klicken muss, um zur MSA zu kommen"]("Hier den path dazu"): Based on the RefSeq library an MSA was performed. Conservation Scores are calculated with two different models (Pei & Grishin conservation, SHannon entropy). The models are compared to each other. For the evaluation of three hipotheses which were stated to judge the performance of the Position Effect Models all residues were categorized by DMS-Scores and Conservation. After creation of consensus sequences with different methods (self-calculated consensus sequence, EMBOSS Consensus Alignment), the mismatch positions between the consensus sequence and the wild type sequence were examined for their categorization to evaluate the hypotheses.

### Necessary Packages
All the necessary packages can be found in the [enviroment.yml](enviroment.yml) file.

### Discussion