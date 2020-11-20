# Segmentation of Pap Smear Images



## Aims

**Segmentation.**
Use classical (non-deep-learning) imaging techniques to develop an image segmentation method that separates each image into a regions corresponding to the nucleus, cytoplasm and background.

**Validation.**
Use the DICE coefficient to compare the segmentations with the reference data.



## Possible Extensions

**Classification.** Calculate a set to features that are based on Gray-Level Co-Occurrence Matrix features and develop a classifier. Only calculate on GLCM of the classes normal columnar and severe dysplastic. Use 10 images from each class. Use a scatter plot or any other suitable statistics to see if the feature statistic of the two classes is different.



## Repository Contents

- data:
  - Pap-smear Benchmark Data For Pattern Classification: https://www.researchgate.net/publication/265873515_Pap-smear_Benchmark_Data_For_Pattern_Classification

- notebooks:
  - papsmear-data-eda.ipynb
  - papsmear-data-01-manual-thresholding.ipynb
  - papsmear-data-02-otsu-thresholding-with-median-filter.ipynb
  - papsmear-data-02-otsu-thresholding-with-different-filters.ipynb

- presentation:
  - .pdf and .pptx presentations of the results
