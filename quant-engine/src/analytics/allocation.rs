use std::collections::HashMap;

use crate::models::Holding;

pub fn calculate_allocation(
    holdings: &Vec<Holding>,
) -> HashMap<String, f64> {

    let mut allocation = HashMap::new();

    let total_value: f64 = holdings
        .iter()
        .map(|h| h.current_price * h.shares)
        .sum();

    if total_value == 0.0 {
        return allocation;
    }

    for stock in holdings {

        let value =
            stock.current_price * stock.shares;

        allocation.insert(
            stock.ticker.clone(),
            (value / total_value) * 100.0,
        );
    }

    allocation
}