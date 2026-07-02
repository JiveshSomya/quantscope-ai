def generate_report(summary, analysis):

    return {
        "report": f"""
Portfolio Health Report

Total Value: ${analysis['portfolio_value']}

Profit: ${analysis['total_profit']}

Risk: {analysis['risk']}

Volatility: {analysis['volatility']}

Recommendation:

Your portfolio appears healthy.
Consider increasing diversification if your future holdings become concentrated in one sector.
"""
    }