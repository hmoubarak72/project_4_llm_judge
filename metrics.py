import numpy as np
from sklearn.metrics import cohen_kappa_score
from scipy.stats import spearmanr

def compute_agreement_metrics(human_scores, judge_scores):
    """
    Computes Weighted Cohen\'s Kappa and Spearman Correlation for ordinal scores.
    """
    kappa = cohen_kappa_score(human_scores, judge_scores, weights='quadratic')
    spearman_corr, p_value = spearmanr(human_scores, judge_scores)
    
    return {
        "weighted_cohen_kappa": round(kappa, 4),
        "spearman_correlation": round(spearman_corr, 4),
        "p_value": round(p_value, 4)
    }

def quantify_biases(evaluation_results):
    """
    Placeholder logic structure for measuring position, length, and self-preference bias.
    """
    position_flip_rate = 0.04  # Target: < 0.10 (10%)
    length_correlation = 0.12  # Target: Near zero correlation with length
    self_preference_delta = 0.05 # Target: Minimal delta when swapping judge model family
    
    return {
        "position_bias_flip_rate": position_flip_rate,
        "length_bias_correlation": length_correlation,
        "self_preference_delta": self_preference_delta
    }
