use axum::Json;

use crate::models::{Analysis, Portfolio};
use crate::analytics::allocation::calculate_allocation;

pub async fn health() -> &'static str {

    "Rust Quant Engine OK"
}

pub async fn analyze(

    Json(portfolio): Json<Portfolio>,

) -> Json<Analysis> {

    let mut value = 0.0;

    let mut profit = 0.0;

    let allocation =calculate_allocation(&portfolio.holdings);

    for stock in portfolio.holdings {

        value += stock.current_price * stock.shares;

        profit +=
            (stock.current_price - stock.buy_price)
            * stock.shares;
    }

    let volatility =
        if value > 10000.0 {

            18.5

        } else {

            9.4
        };

    let risk =
        if volatility > 15.0 {

            "High".to_string()

        } else {

            "Low".to_string()
        };

    Json(

        Analysis {

            portfolio_value: value,

            total_profit: profit,

            risk,

            volatility,
        }
    )
}