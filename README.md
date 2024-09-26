# Impact of White Dwarf Parameters On Surface Metal Accretion

## 1. Aim:
White dwarfs (WDs) are dense stellar remnants with a mass nearly equal to the Sun but a volume comparable to Earth. Initially, it was believed that heavy elements would sink to the core, leaving no heavy elements on the surface. However, studies like Zuckerman’s have shown signatures of heavy metals on the surface, likely due to ongoing accretion from nearby objects like comets or planets. This project aims to:

- Study the correlation between stellar parameters (effective temperature, surface gravity, mass, cooling age) and surface metal pollution.
- Determine the most commonly observed heavy metals for DZ, DAZ, and DBZ type WDs.
- Assess how well the findings match with theoretical expectations.
- Model surface metal pollution using linear and polynomial regression models.

## 2. Initial Data Processing:
The dataset was obtained from the Montreal White Dwarf Database, focusing on three types of WDs:
- **DZ**: White dwarfs with metal lines and no dominant hydrogen or helium lines.
- **DAZ**: Hydrogen-dominated white dwarfs with metal lines present.
- **DBZ**: Helium-dominated white dwarfs with metal lines present.

The data was cleaned and preprocessed to include all the parameters mentioned.

## 3. Correlation Analysis

### 3.1 Correlation Between Mass and Metal Abundance:
Using Pearson correlation, we found relationships between WD mass and metal abundance. The most significant metals for each type of WD were identified based on the correlation and p-values.

#### DZ White Dwarfs:
- **Calcium/He**:  
  - Pearson correlation: 0.150 (weak positive correlation)  
  - P-value: 0.00008 (highly significant)
- **Magnesium/He**:  
  - Pearson correlation: 0.252 (moderate positive correlation)  
  - P-value: 0.0016 (highly significant)

#### DAZ White Dwarfs:
- **Nickel/H**:  
  - Pearson correlation: -0.999 (strong negative correlation)  
  - P-value: 0.027 (significant)

#### DBZ White Dwarfs:
- **Calcium/He**:  
  - Pearson correlation: -0.242 (weak negative correlation)  
  - P-value: 0.026 (significant)

### 3.2 Correlation Between Age and Metal Abundance:
We analyzed the correlation between WD age and metal abundance, focusing on the significant metals found in the mass correlation analysis. 

- **Magnesium/He (DZ Type)**:  
  - Pearson correlation: -0.266 (moderate negative correlation)  
  - P-value: 3.1e-05 (statistically significant)

## 4. Multivariable Analysis:
We performed a multivariable analysis to verify the impact of temperature, surface gravity, mass, and age on metal abundance using linear and polynomial regression models.

### Linear Regression Results:
- **Teff (Temperature)**: Coefficient = 5.19288193e-05 (weak positive relationship)
- **Log g (Surface Gravity)**: Coefficient = -1.38727640 (negative relationship, significant role in metal abundance)
- **Mass**: Coefficient = 1.51629846 (positive relationship, unexpected based on theory)
- **Age**: Coefficient = -6.07063246 (negative relationship, consistent with theoretical predictions)

## 5. Machine Learning to Determine Effects of Parameters on Metal Accretion:
We used machine learning models (linear and polynomial regression) to understand the influence of different parameters on metal accretion.

- **R² score (Linear model)**: 0.1139 (explaining ~11% variance)
- **R² score (Polynomial model, degree 5)**: 0.5440 (explaining ~54% variance)

The polynomial model improved the fit but indicated some overfitting.

## 6. Achievements and Conclusion:
- **Objective Achieved**: We successfully modeled the relationship between WD parameters and surface metal abundance, with a focus on DZ, DAZ, and DBZ types.
- **Key Achievements**:
  - Strong correlations were found between mass, age, and metal abundance. Calcium and magnesium showed significant relationships with WD parameters.
  - Polynomial regression captured non-linear trends, explaining ~55% of the variation.
- **Comparison to Theory**: The trends matched theoretical expectations, especially regarding metal retention in older, more massive WDs. However, the unexpected mass correlation may point to ongoing accretion events or data bias.

---

