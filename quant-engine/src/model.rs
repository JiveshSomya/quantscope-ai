use serde::{Deserialize, Serialize};

#[derive(Debug, Deserialize)]
pub struct Holding {
    pub ticker: String,
    pub shares: f64,
    pub buy_price: f64,
    pub current_price: f64,
}

#[derive(Debug, Deserialize)]
pub struct Portfolio {
    pub holdings: Vec<Holding>,
}

#[derive(Debug, Serialize)]
use std::collections::HashMap;

#[derive(Debug, Serialize)]
pub struct Analysis {
    pub portfolio_value: f64,
    pub total_profit: f64,
    pub risk: String,
    pub volatility: f64,
    pub allocation: HashMap<String, f64>,
}