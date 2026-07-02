use axum::{
    routing::{get, post},
    Router,
};

use crate::services::analyzer::{analyze, health};

pub fn create_router() -> Router {

    Router::new()

        .route("/health", get(health))

        .route("/analyze", post(analyze))
}