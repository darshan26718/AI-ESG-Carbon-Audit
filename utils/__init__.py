"""
AI-ESG-Predictive-Maintenance
============================

Utils Package Initialization

This file exposes all utility modules used across:

- ESG Dashboard
- Carbon Forecasting
- Predictive Maintenance
- SHAP Explainability
- ESG Scoring
- AI Sustainability Advisor
- Net Zero Planner
- ESG Benchmarking
- Climate Risk Assessment
- Green Investment Analyzer
- Circular Economy Optimizer

Author:
--------
AI-ESG-Predictive-Maintenance
"""

# ==========================================================
# CORE UTILITIES
# ==========================================================

from .data_preprocessing import *
from .feature_engineering import *

# ==========================================================
# MACHINE LEARNING
# ==========================================================

from .predictive_models import *
from .model_evaluation import *
from .maintenance_analysis import *

# ==========================================================
# ESG & CARBON
# ==========================================================

from .carbon_calculator import *
from .esg_scoring import *

# ==========================================================
# EXPLAINABLE AI
# ==========================================================

from .shap_analysis import *

# ==========================================================
# AI RECOMMENDATION ENGINE
# ==========================================================

from .recommendation_engine import *

# ==========================================================
# NET ZERO PLANNER
# ==========================================================

from .net_zero_planner import *

# ==========================================================
# CLIMATE RISK
# ==========================================================

from .climate_risk import *

# ==========================================================
# GREEN INVESTMENT
# ==========================================================

from .investment_analysis import *

# ==========================================================
# CIRCULAR ECONOMY
# ==========================================================

from .circular_economy import *

# ==========================================================
# REPORT GENERATION
# ==========================================================

from .report_generator import *

# ==========================================================
# PACKAGE VERSION
# ==========================================================

__version__ = "1.0.0"

# ==========================================================
# AVAILABLE MODULES
# ==========================================================

__all__ = [

    # Core
    "data_preprocessing",
    "feature_engineering",

    # ML
    "predictive_models",
    "model_evaluation",
    "maintenance_analysis",

    # ESG
    "carbon_calculator",
    "esg_scoring",

    # Explainability
    "shap_analysis",

    # Recommendation
    "recommendation_engine",

    # Net Zero
    "net_zero_planner",

    # Climate Risk
    "climate_risk",

    # Investment
    "investment_analysis",

    # Circular Economy
    "circular_economy",

    # Reporting
    "report_generator"
]
