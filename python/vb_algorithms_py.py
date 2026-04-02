"""
Variational Bayes and Gibbs Sampling Algorithms
M1: Simple Linear Regression (no random effects)

Based on Dr John Holmes' R implementation
Python conversion: 2026-03-05
"""

import numpy as np
from scipy import stats
from scipy.special import digamma


class SimpleLinearVB:
    """
    Variational Bayes for Simple Linear Regression.
    Model: y = Xβ + ε, ε ~ N(0, τₑ⁻¹I)
    
    Mean-field approximation:
        q(β, τₑ) = q(β) q(τₑ)
        q(β) = N(μ_β, Σ_β)
        q(τₑ) = Gamma(a_e, b_e)
    """
    
    def __init__(self, X, y, alpha_e=0, gamma_e=0):
        """
        Initialise VB algorithm.
        
        Args:
            X: np.array (n, p), design matrix
            y: np.array (n,), response vector  
            alpha_e: float, Gamma prior shape for τₑ (0 = flat)
            gamma_e: float, Gamma prior rate for τₑ (0 = flat)
        """
        self.X = X
        self.y = y
        self.n, self.p = X.shape
        self.alpha_e = alpha_e
        self.gamma_e = gamma_e
        
        # Precompute X^T X and X^T y
        self.XTX = X.T @ X
        self.XTy = X.T @ y
        
        # Initialise
        if alpha_e > 0 and gamma_e > 0:
            self.tau_e = alpha_e / gamma_e
        else:
            self.tau_e = 1.0
        
        self.mu_beta = np.zeros(self.p)
        self.Sigma_beta = np.eye(self.p)
        
    def fit(self, max_iter=100, tol=1e-5, track_history=True):
        """
        Run coordinate ascent VB algorithm.
        
        Args:
            max_iter: int, maximum iterations
            tol: float, convergence tolerance
            track_history: bool, track E[τₑ] and ELBO
        
        Returns:
            dict with results
        """
        # History storage
        if track_history:
            tau_e_history = np.zeros(max_iter)
            elbo_history = np.zeros(max_iter)
        
        for i in range(max_iter):
            # Store old values for convergence check
            if i > 0:
                mu_beta_old = self.mu_beta.copy()
                Sigma_beta_old = self.Sigma_beta.copy()
                tau_e_old = self.tau_e
            
            # Update q(β): Normal distribution
            self.Sigma_beta = np.linalg.inv(self.tau_e * self.XTX)
            self.mu_beta = self.tau_e * self.Sigma_beta @ self.XTy
            
            # Compute residuals and trace term
            err = self.y - self.X @ self.mu_beta
            Tr_XTX_Sigma = np.trace(self.XTX @ self.Sigma_beta)
            
            # Update q(τₑ): Gamma distribution
            a_e_new = self.alpha_e + 0.5 * self.n
            b_e_new = self.gamma_e + 0.5 * np.sum(err**2) + 0.5 * Tr_XTX_Sigma
            self.tau_e = a_e_new / b_e_new
            
            # Store history
            if track_history:
                tau_e_history[i] = self.tau_e
                
                # Compute ELBO (simplified)
                elbo = -0.5 * self.n * np.log(2 * np.pi)
                elbo += 0.5 * self.n * (digamma(a_e_new) - np.log(b_e_new))
                elbo_history[i] = elbo
            
            # Check convergence
            if i > 0:
                diff_mu = np.sqrt((self.mu_beta - mu_beta_old)**2) / (np.abs(self.mu_beta) + 0.01)
                diff_tau = np.abs(self.tau_e - tau_e_old) / (self.tau_e + 0.01)
                diff_Sigma = np.sqrt((np.diag(self.Sigma_beta) - np.diag(Sigma_beta_old))**2) / np.diag(self.Sigma_beta)
                
                max_diff = np.max(np.concatenate([diff_mu, [diff_tau], diff_Sigma]))
                
                if max_diff < tol:
                    print(f"VB converged after {i+1} iterations")
                    break
        else:
            print(f"VB reached max iterations ({max_iter})")
        
        # Prepare results
        results = {
            'mu_beta': self.mu_beta,
            'Sigma_beta': self.Sigma_beta,
            'E_tau_e': self.tau_e,
            'a_e_new': a_e_new,
            'b_e_new': b_e_new,
            'iterations': i + 1
        }
        
        if track_history:
            results['E_tau_e_history'] = tau_e_history[:i+1]
            results['elbo_history'] = elbo_history[:i+1]
        
        return results


class SimpleLinearGibbs:
    """
    Blocked Gibbs Sampler for Simple Linear Regression.
    Model: y = Xβ + ε, ε ~ N(0, τₑ⁻¹I)
    
    Samples from full conditionals:
        β | τₑ, y ~ N(μ, Σ)
        τₑ | β, y ~ Gamma(a, b)
    """
    
    def __init__(self, X, y, alpha_e=0, gamma_e=0):
        """
        Initialise Gibbs sampler.
        
        Args:
            X: np.array (n, p), design matrix
            y: np.array (n,), response vector
            alpha_e: float, Gamma prior shape for τₑ
            gamma_e: float, Gamma prior rate for τₑ
        """
        self.X = X
        self.y = y
        self.n, self.p = X.shape
        self.alpha_e = alpha_e
        self.gamma_e = gamma_e
        
        # Precompute X^T X and X^T y
        self.XTX = X.T @ X
        self.XTy = X.T @ y
    
    def sample(self, n_iter=5000, n_burnin=1000, n_chains=3, tau_e_init=None):
        """
        Run Gibbs sampler with multiple chains.
        
        Args:
            n_iter: int, iterations per chain
            n_burnin: int, burn-in iterations
            n_chains: int, number of chains
            tau_e_init: list of floats, initial τₑ for each chain (or None for default)
        
        Returns:
            dict with combined samples from all chains
        """
        # Default initialisations (matching R code)
        if tau_e_init is None:
            tau_e_init = [3.0, 0.5, 1.0]  # High, low, medium precision guesses
        
        all_samples = []
        
        for chain_idx in range(n_chains):
            print(f"  Chain {chain_idx + 1}/{n_chains}...")
            
            # Initialise
            tau_e = tau_e_init[chain_idx]
            beta = np.random.randn(self.p)
            
            # Storage
            samples_beta = np.zeros((n_iter, self.p))
            samples_tau_e = np.zeros(n_iter)
            
            # Gibbs iterations
            for i in range(n_iter):
                # Sample β | τₑ, y from multivariate normal
                Prec = self.XTX * tau_e
                Sigma = np.linalg.inv(Prec)
                mu = tau_e * Sigma @ self.XTy
                beta = np.random.multivariate_normal(mu, Sigma)
                
                # Sample τₑ | β, y from Gamma
                err = self.y - self.X @ beta
                shape = self.alpha_e + 0.5 * self.n
                rate = self.gamma_e + 0.5 * np.sum(err**2)
                tau_e = np.random.gamma(shape, 1.0 / rate)  # NumPy uses scale = 1/rate
                
                # Store samples
                samples_beta[i, :] = beta
                samples_tau_e[i] = tau_e
            
            # Remove burn-in
            samples_beta = samples_beta[n_burnin:, :]
            samples_tau_e = samples_tau_e[n_burnin:]
            
            # Combine into single array
            chain_samples = np.column_stack([samples_beta, samples_tau_e])
            all_samples.append(chain_samples)
        
        # Combine all chains
        combined_samples = np.vstack(all_samples)
        
        # Create column names
        col_names = [f'beta{i}' for i in range(self.p)] + ['tau_e']
        
        return {
            'samples': combined_samples,
            'col_names': col_names,
            'n_samples': combined_samples.shape[0]
        }


def run_vb_simple_linear(X, y, alpha_e=0, gamma_e=0, max_iter=100, tol=1e-5):
    """
    Convenience function to run VB for simple linear regression.
    
    Args:
        X: np.array (n, p), design matrix
        y: np.array (n,), response vector
        alpha_e: float, Gamma prior shape for τₑ
        gamma_e: float, Gamma prior rate for τₑ
        max_iter: int, maximum iterations
        tol: float, convergence tolerance
    
    Returns:
        dict with VB results
    """
    vb = SimpleLinearVB(X, y, alpha_e, gamma_e)
    results = vb.fit(max_iter=max_iter, tol=tol, track_history=True)
    return results


def run_gibbs_simple_linear(X, y, alpha_e=0, gamma_e=0, n_iter=5000, 
                            n_burnin=1000, n_chains=3):
    """
    Convenience function to run Gibbs for simple linear regression.
    
    Args:
        X: np.array (n, p), design matrix
        y: np.array (n,), response vector
        alpha_e: float, Gamma prior shape for τₑ
        gamma_e: float, Gamma prior rate for τₑ
        n_iter: int, iterations per chain
        n_burnin: int, burn-in iterations
        n_chains: int, number of chains
    
    Returns:
        dict with Gibbs samples
    """
    gibbs = SimpleLinearGibbs(X, y, alpha_e, gamma_e)
    results = gibbs.sample(n_iter=n_iter, n_burnin=n_burnin, n_chains=n_chains)
    return results


def compute_sd_ratios(vb_results, gibbs_results, p):
    """
    Compute SD ratios (VB / Gibbs) for under-dispersion detection.
    
    Args:
        vb_results: dict from VB
        gibbs_results: dict from Gibbs
        p: int, number of beta parameters
    
    Returns:
        dict with SD ratios
    """
    samples = gibbs_results['samples']
    
    sd_ratios = {}
    
    # Beta parameters
    for i in range(p):
        vb_sd = np.sqrt(vb_results['Sigma_beta'][i, i])
        gibbs_sd = np.std(samples[:, i], ddof=1)
        sd_ratios[f'beta{i}'] = vb_sd / gibbs_sd
    
    # Tau_e parameter
    vb_sd_tau = np.sqrt(vb_results['a_e_new'] / (vb_results['b_e_new']**2))
    gibbs_sd_tau = np.std(samples[:, -1], ddof=1)
    sd_ratios['tau_e'] = vb_sd_tau / gibbs_sd_tau
    
    return sd_ratios
