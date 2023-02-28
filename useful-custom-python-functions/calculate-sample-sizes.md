# Calculate sample sizes

This function can be used to calculate survey target response rates based on required sample sizes for a degree of statistical certainty.

```python
def get_sample_size(population_size, margin_of_error=0.05, confidence_level=0.95, z_score=1.96, p=0.5):

  """Based on a given population size, calculate the optimum sample size to achieve the given margin of error and confidence level.
  Sample size formula is based on n = (Z^2 * p * (1 - p)) / E^2

  Parameters
  ----------------------
  population_size : int
    The population size of the survey.
  
  margin_of_error : float
    The required margin of error, defaults to 0.05 or 5 percent.
  
  confidence_level : float
    The required confidence level, defaults to 0.95 or 95 percent. It is the degree of confidence that the true value is within the range of margin of error, plus or minus.
    
  z_score : float
    The Z-score associated with a 95% confidence level, which is 1.96 for a 95 percent confidence level. Defaults to 1.96.
  
  p : float
    The maximum variation in the population, defaults to 0.5 or 50 percent.
  """
  sample_size = (z_score ** 2 * p * (1 - p) * population_size) / ((z_score ** 2 * p * (1 - p)) + ((population_size - 1) * margin_of_error ** 2))
  sample_size = math.ceil(sample_size) # round up to nearest integer
  return sample_size
```