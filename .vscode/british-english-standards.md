# British English Coding Standards

**Agent Instructions for ENEL445 Project**

## Code Comments

All comments in code must use **British English** spelling and conventions:

- Use British spellings: "optimise" (not "optimize"), "colour" (not "color"), "behaviour" (not "behavior")
- Comments should be **phrases, not sentences**
- No full stops at the end of comments unless multiple sentences
- Examples:
  ```python
  # Compute gradient for variational parameters
  # Initialise covariance matrix
  # Optimisation loop with convergence check
  ```

## Variable Names

All user-defined variable names must use **British English** spelling:

- `optimiser` (not `optimizer`)
- `initialise()` (not `initialize()`)
- `colour_map` (not `color_map`)
- `behaviour_params` (not `behavior_params`)
- `centre` (not `center`)
- `analyse()` (not `analyze()`)

**Note**: Standard library functions retain their original spelling (e.g., `scipy.optimize.minimize`), but wrapper variables should use British English:
```python
# Correct
optimiser_result = scipy.optimize.minimize(...)

# Incorrect
optimizer_result = scipy.optimize.minimize(...)
```

## Documentation and Responses

All documentation strings, markdown files, and responses to user prompts must use **British English**:

- Spelling: British conventions throughout
- Date format: DD/MM/YYYY (e.g., 17/03/2026)
- Terminology: "whilst" (acceptable), "amongst" (acceptable)

## Examples

### Good
```python
def initialise_variational_params(n_features):
    """
    Initialise variational parameters for VI optimisation
    
    Args:
        n_features: Number of predictors in regression model
    
    Returns:
        Dictionary containing initialised parameters
    """
    # Initialise mean vector
    mu_beta = np.zeros(n_features)
    
    # Initialise covariance as identity
    sigma_beta = np.eye(n_features)
    
    return {'mu': mu_beta, 'sigma': sigma_beta}


def optimise_elbo(params, data, optimiser='BFGS'):
    """Run optimisation algorithm to maximise ELBO"""
    # Gradient-based optimisation loop
    pass
```

### Bad
```python
def initialize_variational_params(n_features):  # American spelling
    """Initialize variational parameters."""  # American spelling
    # Initialize mean vector.  # Sentence with full stop
    mu_beta = np.zeros(n_features)
    return mu_beta


def optimize_elbo(params, data, optimizer='BFGS'):  # American spelling
    """Run optimization algorithm."""  # American spelling
    pass
```

## Agent Behaviour

When generating code, documentation, or responding to user queries:

1. **Always use British English spelling** in all user-facing text
2. **Code comments are phrases** (no full stops unless multiple sentences)
3. **Variable names follow British spelling** where applicable
4. **Respect standard library naming** but wrap with British-spelled variables
5. **Consistency is critical** - one spelling standard throughout

## Common British vs American Spellings

| British English | American English |
|----------------|------------------|
| optimise       | optimize         |
| initialise     | initialize       |
| analyse        | analyze          |
| colour         | color            |
| behaviour      | behavior         |
| centre         | center           |
| metre          | meter            |
| programme*     | program          |
| whilst         | while            |
| amongst        | among            |

*Note: "program" is acceptable in British English for computer programs, but "programme" for other contexts

## Summary

This is a **strict requirement** for the ENEL445 project:
- Code comments: British English phrases
- Variable names: British English spelling
- All responses: British English
